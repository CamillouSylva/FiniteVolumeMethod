(content:solveurs:labels)=
# Les solveurs de Riemann approchés Rusanov, HLL et HLLC

On considère le problème avec condition initiale et conditions aux bords transmissives (voir la section {numref}`content:BC:labels`) suivant : 

:::{math}
:label: problème général
\left\{ 
\begin{array}{l l l}
\displaystyle \dfrac{\partial \pmb{U}}{\partial t} + \dfrac{\partial \pmb{F(U)}}{\partial x} = \pmb{0} \, ,\\[4mm] 
\displaystyle \pmb{U}(x,0) = \pmb{U}^{(0)}(x) \quad \forall \ x \in [x_L;x_R] \, ,\\ 
\end{array} 
\right.
:::

où $\pmb{U}$ le vecteur des variables conservatives et $\pmb{U^{(0)}}$ défini comme dans {eq}`condition_init`.

Au lieu d'utiliser toutes les situations possibles on va se restreindre à des cas plus simples. Considérons la solution exacte du problème de Riemann {eq}`problème général` dans le cas des équations d'Euler 1D schématisée sur la figure \ref{solution exacte}. A 
Ici on simplifie en considérant que les ondes non linéaires sont des chocs.  $S_L$ et $S_R$ correspondent aux vitesse de propagation des chocs qui perturbent les états initiaux $\pmb{U_L}$ et $\pmb{U_R}$ respectivement. Sur le schéma on considère le cas où $S_L < 0 < S_R$. 

:::{figure} ./figures/fig_sol.png
:name: solutionExacte
Problème de Riemann complet pour les équations d'Euler 1D, avec volume de contrôle $[x_L;x_R] \times [0;T]$ dans le cas où $S_L < 0 < S_R$.
:::

## Les solveurs de Riemann approché Rusanov et Harten-Lax-Van Leer (HLL)

Harten, Lax et Van Leer \cite{[164]} ont défini le solveur de Riemann approché suivant : 

:::{math}
:label: solution approchée uhll
\pmb{U}_h(x,t) = \left\{\begin{array}{lll}
\pmb{U_L} \quad \quad \text{si} \; \dfrac{x}{t} \leq S_L \\
\pmb{U}^{hll} \quad \quad \text{si} \; S_L \leq \dfrac{x}{t} \leq S_R \\ 
\pmb{U_R} \quad \quad \text{si} \; \dfrac{x}{t} \geq S_R 
\end{array}
\right. 
:::

Les vitesses $S_L$ et $S_R$ sont supposées connues et l'état intermédiaire $\pmb{U}^{hll}$ constant. 

La structure de la solution approchée du problème de Riemann \eqref{problème général}, appelée \textbf{solveur HLL} de Riemann est schématisée sur la figure \ref{solution hll}.

:::{figure} ./figures/figHLL.png
:name: solution hll
Structure du solveur de Riemann approché HLL
:::

Cette approximation présente trois états constants séparés par deux ondes non linéaires de vitesses $S_L$ et $S_R$ respectivement. La zone étoilée est décrite par un unique état constant $\pmb{U}^{hll}$ que nous allons définir dans la suite.


**Formulations intégrales du problème de Riemann**

La formulation intégrale des lois de conservation dans \eqref{problème général}, dans le volume de contrôle $[x_L;x_R] \times [0;T]$ est : \\ 

:::{math}
\dfrac{d}{dt} \int_{x_L}^{x_R} \pmb{U}(x,t)dx = - \int_{x_L}^{x_R} \partial_x \pmb{F(U}(x,t))dx = -\pmb{F(U}(x_R,t)) + \pmb{F(U}(x_L,t))
:::

:::{math}
:label: integrale
\Rightarrow \int_{x_L}^{x_R} \pmb{U}(x,T)dx = \int_{x_L}^{x_R} \pmb{U}(x,0)dx + \int_{0}^{T} \pmb{F(U}(x_L,t))dt - \int_{0}^{T} \pmb{F(U}(x_R,t))dt 
:::

Puis en utilisant la condition initiale à deux états {ref}`condition_init` on a : 

:::{math}
\int_{x_L}^{x_R} \pmb{U}(x,T)dx = \int_{x_L}^{0} \pmb{U_L}dx + \int_{0}^{x_R} \pmb{U_R}dx + \int_{0}^{T} \pmb{F(U_L)}dt - \int_{0}^{T} \pmb{F(U_R})dt
:::

i.e 
:::{math}
:label: condition de consistance
\int_{x_L}^{x_R} \pmb{U}(x,T)dx = x_R \pmb{U_R} - x_L \pmb{U_L} + T(\pmb{F_L} - \pmb{F_R})
:::

où $\pmb{F_L}=\pmb{F(U_L)}$ et $\pmb{F_R}=\pmb{F(U_R)}$ les flux à gauche et à droite respectivement.

 Cette relation ainsi obtenue correspond à la **condition de consistance** du schéma numérique que l'on définira ultérieurement (section \ref{VF}). 
 
 Ensuite, en écrivant l'intégrale du terme de gauche de l'égalité {ref}`integrale` tel que : 

:::{math}
\int_{x_L}^{x_R} \pmb{U}(x,T)dx = \int_{x_L}^{T S_L} \pmb{U}(x,T)dx  + \int_{T S_L}^{T S_R} \pmb{U}(x,T)dx + \int_{T S_R}^{x_R} \pmb{U}(x,T)dx
::: 
Et en évaluant la première et la troisième intégrale du terme de droite, 

:::{math}
\int_{x_L}^{x_R} \pmb{U}(x,T)dx = \int_{x_L}^{T S_L} \pmb{U_L} dx + \int_{T S_L}^{T S_R} \pmb{U}(x,T)dx + \int_{T S_R}^{x_R} \pmb{U_R} dx 
:::

d'où : 

:::{math}
:label: égalité2
\int_{x_L}^{x_R} \pmb{U}(x,T)dx = \int_{T S_L}^{T S_R} \pmb{U}(x,T)dx + (T S_L - x_L)\pmb{U_L} + (x_R - T S_R)\pmb{U_R}
:::

Puis en utilisant {ref}`condition de consistance` et {ref}`égalité2`, on obtient : 

:::{math}
:label: dernière équation
\int_{T S_L}^{T S_R} \pmb{U}(x,T)dx = T(S_R \pmb{U_R} - S_L \pmb{U_L} + \pmb{F_L} - \pmb{F_R})
:::

Enfin, en divisant par $T(S_R-S_L)$ (base du triangle formé par les deux ondes non linéaires de la solution exacte au temps $T>0$) on a :

:::{math}
:label: intégrale moyenne
\dfrac{1}{T(S_R-S_L)} \int_{T S_L}^{T S_R} \pmb{U}(x,T)dx = \dfrac{S_R \pmb{U_R} - S_L \pmb{U_L} + \pmb{F_L} - \pmb{F_R}}{S_R - S_L}
:::

Ainsi, la valeur moyenne de la solution exacte du problème de Riemann entre l'onde la plus lente et l'onde la plus rapide à l'instant $T$ est une constante connue mais ce, seulement si les vitesses $S_L$ et $S_R$ le sont. Cette constante est exactement $\pmb{U}^{hll}$ :

:::{math}
:label: uhll
\boxed{\pmb{U}^{hll} = \dfrac{S_R \pmb{U_R} - S_L \pmb{U_L} + \pmb{F_L} - \pmb{F_R}}{S_R - S_L}}
:::

On souhaite maintenant trouver le flux qui lui est associé. 
En appliquant la formulation intégrale des lois de conservation sur la portion de gauche de la figure \ref{solution exacte} avec le volume de contrôle $[x_L;0] \times [0;T]$, on obtient : 

:::{math}
\int_{x_L}^{0} \pmb{U}(x,T)dx = \int_{x_L}^{0} \pmb{U}(x,0)dx + \int_{0}^{T} \pmb{F(U}(x_L,t))dt - \int_{0}^{T} \pmb{F(U}(0,t))dt
:::

:::{math}
\iff \int_{x_L}^{T S_L} \pmb{U}(x,T)dx + \int_{T S_L}^{0} \pmb{U}(x,T)dx = \int_{0}^{T} \pmb{U_L}dx + \int_{0}^{T}\pmb{F(U_L)}dt - \int_{0}^{T}\pmb{F_{0L}}dt
:::

:::{math}
\begin{align*}
\Rightarrow \int_{T S_L}^{0} \pmb{U}(x,T)dx &= - \int_{x_L}^{T S_L} \pmb{U}(x,T)dx + \int_{x_L}^{0} \pmb{U_L} dx + T(\pmb{F_L} - \pmb{F_{0L}}) \\ 
&= -\int_{0}^{T S_L} \pmb{U}(x,T)dx + T(\pmb{F_L} - \pmb{F_{0L}}) \\ 
&= -\int_{0}^{T S_L} \pmb{U_L} dx + T(\pmb{F_L} - \pmb{F_{0L}})
\end{align*} 
:::

D'où, 
:::{math}
:label: éq f0L
\int_{T S_L}^{0} \pmb{U}(x,T)dx = - T S_L \pmb{U_L} + T(\pmb{F_L} - \pmb{F_{0L}})
:::

où $\pmb{F_{0L}}$ est le flux $\pmb{F(U)}$ le long de l'axe t. Puis en isolant $\pmb{F_{0L}}$ dans {ref}`éq f0L` on a : 

:::{math}
:label: f0L
\pmb{F_{0L}} = \pmb{F_L} - S_L \pmb{U_L} - \dfrac{1}{T} \int_{T S_L}^{0} \pmb{U}(x,T)dx
:::

En procédant de la même manière; en évaluant la formulation intégrale sur le volume de contrôle $[0;x_R] \times [0;T]$ on a : 

:::{math}
\int_{T S_R}^{0} \pmb{U}(x,T)dx = -T S_R \pmb{U_R} + T(\pmb{F_R} - \pmb{F_{0R}})
:::

et 

:::{math} 
:label: f0R
\pmb{F_{0R}} = \pmb{F_R} - S_R \pmb{U_R} + \dfrac{1}{T} \int_{0}^{T S_R} \pmb{U}(x,T)dx
:::

On remarque que $\pmb{F_{0L}} = \pmb{F_{0R}}$ ; cela provient de la condition de consistance {ref}`condition de consistance` établie précédemment. 

De plus, toutes les relations que l'on vient de trouver sont exactes car on a supposé la solution exacte du problème de Riemann. 


 Le flux correspondant $\pmb{F}^{hll}$ à $\pmb{U}^{hll}$ le long de l'axe $t$ se trouve à l'aide des égalités \eqref{f0L} ou {ref}`f0R` en remplaçant la solution exacte $\pmb{U}$ sous l'intégrale par la solution approchée $\pmb{U}_h$ définie ci-dessus dans {ref}`solution approchée uhll`. 

Notons que nous ne prenons pas $\pmb{F}^{hll} = \pmb{F(U}^{hll})$. Le cas où $S_L < 0 < S_R$ sera le plus compliqué à étudier. Pour définir $\pmb{F}^{hll}$, on remplace l'intégrande de {ref}`f0L` ou {ref}`f0R` par $\pmb{U}^{hll}$ défini dans {ref}`uhll`. En utilisant, l'égalité {ref}`f0L` par exemple : 

:::{math}
\begin{align*}
\pmb{F}^{hll} &= \pmb{F_L} - S_L \pmb{U_L} - \dfrac{1}{T} \int_{T S_L}^{0} \pmb{U}_h(x,T)dx \\ 
&= \pmb{F_L} - S_L \pmb{U_L} - \dfrac{1}{T} \int_{T S_L}^{0} \pmb{U}^{hll} dx \\
&= \pmb{F_L} - S_L \pmb{U_L} - S_L \pmb{U}^{hll}
\end{align*}
:::

On obtient, avec l'égalité {ref}`f0L` l'expression du flux associé à l'état intermédiare $\pmb{U}^{hll}$ : 

:::{math}
:label: fhll avec f0L
\pmb{F}^{hll} = \pmb{F_L} - S_L(\pmb{U_L} - \pmb{U}^{hll})
:::

Ou, en utilisant l'égalité {ref}`f0R` : 

:::{math}
:label: fhll avec f0R
\pmb{F}^{hll} = \pmb{F_R} - S_R(\pmb{U_R} - \pmb{U}^{hll})
:::

Remarquons que {ref}`fhll avec f0L` et {ref}`fhll avec f0R` s'obtiennent aussi en appliquant les relations de Rankine-Hugoniot à travers les ondes de gauche et de droite respectivement. 

 En effet, pour l'onde de gauche on a : 

:::{math}
\pmb{F}^{hll} - \pmb{F_L} = S_L(\pmb{U}^{hll} - \pmb{U_L}) \iff \pmb{F}^{hll} = \pmb{F_L} - S_L(\pmb{U_L} - \pmb{U}^{hll})
:::

qui correspond exactement à \eqref{fhll avec f0L}. 

Finalement, en remplaçant $\pmb{U}^{hll}$ (voir \eqref{uhll}) dans {ref}`fhll avec f0L` : 

:::{math}
\begin{align*}
\pmb{F}^{hll} &= \pmb{F_L} - S_L \left(\pmb{U_L} - \dfrac{S_R \pmb{U_R} - S_L \pmb{U_L} + \pmb{F_L} - \pmb{F_R}}{S_R - S_L} \right) \\ 
	&= \pmb{F_L} - S_L \left( \dfrac{\pmb{U_L}(S_R - S_L) - S_R \pmb{U_R} + S_L \pmb{U_L} - \pmb{F_L} + \pmb{F_R}}{S_R - S_L} \right) \\ 
    &= \dfrac{\pmb{F_L}(S_R - S_L) - \pmb{U_L} S_R S_L + \pmb{U_R} S_R S_L + \pmb{F_L} S_L - \pmb{F_R} S_L}{S_R - S_L}
\end{align*}
:::
On obtient alors : 
:::{math}
\boxed{\pmb{F}^{hll} = \dfrac{S_R \pmb{F_L} - S_L \pmb{F_R} + S_L S_R(\pmb{U_R} - \pmb{U_L)}}{S_R - S_L} } 
:::

%Le flux numérique associée à la solution approchée $\pmb{U}_h$ au point %$x_{i + \dfrac{1}{2}}$, à l'instant $t^n$ pour la méthode volume finis de %Godunov \cite{[145]} est donnée par : 

Ainsi, le flux associé à la solution approchée $\pmb{U}_h$ est donné par : 

:::{math}
:label: flux hll
\pmb{F}^{HLL} = \left\{
\begin{array}{lll}
\pmb{F_L} \quad \text{si} \; 0 \leq S_L \\ 
\dfrac{S_R \pmb{F_L} - S_L \pmb{F_R} + S_L S_R(\pmb{U_R} - \pmb{U_L})}{S_R - S_L} \quad \text{si} \; S_L \leq 0 \leq S_R \\
\pmb{F_R} \quad \text{si} \;  0 \geq S_R 
\end{array}
\right.
:::

Le solveur de Rusanov \cite{[291]} est un cas particulier du solveur HLL. En effet, en prenant $S_L=-S^+$ et $S_R=S^+$, avec $S^+$ une vitesse positive connue, le solveur de Riemann approché Rusanov \cite{[291]} est défini par : 

:::{math}
:label: solution approchée uRusanov
\pmb{U}_h(x,t) = \left\{\begin{array}{lll}
\pmb{U_L} \quad \quad \text{si} \; \dfrac{x}{t} \leq -S^+ \\
\pmb{U}^{*} \quad \quad \text{si} \; -S^+ \leq \dfrac{x}{t} \leq S^+ \\ 
\pmb{U_R} \quad \quad \text{si} \; \dfrac{x}{t} \geq S^+ 
\end{array}
\right. 
:::

On donne la structure de la solution approché au problème de Riemann {ref}`problème général`, c'est-à-dire du solveur **Rusanov**, sur la figure {numref}`solutionRusanov` : 

:::{figure} ./figures/figRusanov.png
:name: solutionRusanov
Structure du solveur de Riemann approché Rusanov
:::

Et le flux associé à la solution $\pmb{U}_h$ est donné par : 

:::{math}
\pmb{F}^{Rusa} = \left\{
\begin{array}{lll}
\pmb{F_L} \quad \text{si} \; 0 \leq -S^+ \\ 
\dfrac{1}{2}(\pmb{F_L} + \pmb{F_R}) - \dfrac{1}{2} S^+(\pmb{U_R} - \pmb{U_L}) \quad \text{si} \; -S^+ \leq 0 \leq S^+ \\
\pmb{F_R} \quad \text{si} \;  0 \geq S^+ 
\end{array}
\right.
:::

Or, comme $S^+ \geq 0$, seul le cas où  $-S^+ \leq 0 \leq S^+$ se produit et donc le flux de Rusanov \cite{[291]} se réduit à : 

:::{math}
:label: flux Rusanov
\pmb{F}^{Rusa} = \dfrac{1}{2}(\pmb{F_L} + \pmb{F_R}) - \dfrac{1}{2} S^+(\pmb{U_R} - \pmb{U_L})
:::


Étant donné un algorithme calculant les vitesses $S_L$ et $S_R$, on a un flux numérique approché pour la forme conservative {ref}`formule conservative `du schéma de Godunov \cite{[145]}. Il existe des estimations des vitesses $S_L$ et $S_R$ que nous verrons dans la section {numref}`content:estimationsVitesse:labels`. Harten, Lax et Van Leer \cite{[164]} ont montré que le schéma de Godunov {ref}`formule conservative`, {ref}`flux hll` s'il converge, converge vers la solution faible des lois de conservation. Ils prouvèrent que la solution convergente est également la solution physique des lois de conservation. Leurs résultats sont applicables à bon nombre de solveurs de Riemann approchés. L'un des critères est la consistance avec la formulation intégrale des lois de conservation. En fait, une solution approchée $\pmb{U}_h(x,t)$ sera consistante si dans la condition de consistance {ref}`condition de consistance`, le terme de droite reste inchangé. 

Un inconvénient du schéma HLL vient de la discontinuité de contact d'équation $x=u$ schématisée sur la figure {numref}`fig`. On remarque que dans {ref}`intégrale moyenne`, on ne prend pas en considération les variations spatiales de la solution du problème de Riemann dans la zone étoilée. Tout ce qui compte est la valeur moyenne de la solution entre les deux ondes non linéaires à l'instant $T>0$. Harten, Lax et Van Leer \cite{[164]} évoquent une correction de ce défaut du schéma HLL en ajoutant l'onde manquante c'est-à-dire la discontinuité de contact. 

Toro, Spence et Speares \cite{[380]} ont proposé le prétendu **schéma HLLC** où C désigne Contact. Dans ce schéma l'onde du milieu manquante est placée dans la structure du solveur de Riemann approché HLLC.

## Le solveur de Riemann approché HLLC

On considère encore le cas simplifié de deux ondes de choc à gauche et à droite respectivement. 

En fait, le schéma \textbf{HLLC} est une modification du schéma HLL : on lui ajoute la discontinuité de contact manquante.


Considérons la structure de la solution du problème de Riemann à deux ondes (seules les ondes non linéaires) contenue dans un volume de contrôle $[x_L; x_R]\times[0\,; T]$ suffisamment large comme schématisé sur la figure {ref}`solution hll`.
À cela on ajoute une troisième onde au milieu de vitesse $S^*$ correspondant à la valeur propre $\lambda_2 = u$ et on a le système d'ondes schématisé sur la figure {numref}`fig_hllc` suivante :

:::{figure} ./figures/HLLC.png
:name: fig_hllc
Structure du solveur de Riemann approché HLLC
:::

La solution dans la zone étoilée se compose maintenant non plus d'un unique état constant mais de deux états constants $ \pmb{U_{L}^*}$ et $ \pmb{U_{R}^*}$ .


Le solveur de Riemann approché HLLC est donné par :

:::{math}
\pmb{U}_h(x,t) = \left\{ 
\begin{array}{l l}
  \pmb{U_L} & \quad \text{si\, $\frac{x}{t} \leq S_L$}\\
  \pmb{U_{L}^*}  & \quad \text{si\, $S_{L} \leq \frac{x}{t} \leq S^{*}$} \quad,\\ 
   \pmb{U_{R}^*}  & \quad \text{si\, $S^{*} \leq \frac{x}{t} \leq S_R$} \quad,\\ 
 \pmb{U_R} & \quad \text{si\, $\frac{x}{t} \geq S_R$} \\ \end{array} \right.\\
:::
Le flux HLLC pour la méthode approximative de Godunnov \cite{[145]} peut être écrit comme suit:
:::{math}
\pmb{F}^{HLLC}  = \left\{ 
\begin{array}{c c}
  \pmb{F_L} & \quad \text{si\, $0 \leq S_L$}\\
  \pmb{F_{L}^*} = \pmb{F_L} + S_L (\pmb{U_{L}^*} - \pmb{U_{L}}) & \quad \text{si\, $S_{L} \leq 0 \leq S^{*}$} \quad,\\ 
   \pmb{F_{R}^*} = \pmb{F_R} + S_R (\pmb{U_{R}^*} - \pmb{U_{R}}) & \quad \text{si\, $S^{*} \leq 0 \leq S_R$} \quad,\\ 
 \pmb{F_R} & \quad \text{si\, $0 \geq S_R$} \\ \end{array} \right. \\
 :::
avec $K=L$ ou $K=R$ : 

:::{math}
:label: U_K étoile
      \begin{aligned}        
        \pmb{U_{K}^*} = \rho_K \left(\frac{S_K - u_K}{S_K - S^*} \right)
\left[
\begin{array}{c c c}
1\\
S^*\\
\frac{E_K}{\rho_K} + (S^* - u_K) \left[S^* + \frac{p_K}{\rho_K \left(S_K - u_K\right)} \right]
\end{array}
\right]
      \end{aligned}

:::
où  $u_K$ est la vitesse particulaire et $S^*$ la vitesse de l'onde de contact.

(content:estimationsVitesse:labels)=
## Estimations de la vitesse des ondes directes
Estimer les vitesses minimale et maximale du signal présentes dans la solution du problème de Riemann consiste à trouver les vitesses d'onde $S_L$ et $S_R$.

Davis \cite{[103]} a proposé les estimations suivantes :
:::{math}
\ S_L=u_L-a_L,\quad S_R=u_R+a_R
:::

:::{math}
\ \text{et} \quad S_L=\min(u_L-a_L, u_R-a_R), \quad S_R=\max(u_L+a_L, u_R+a_R)
:::

Supposons maintenant que pour un problème de Riemann donné, nous puissions identifier une vitesse positive $S^+$. En choisissant $S_L$ = $-S^+$ et $S_R=S^+$ on se place comme dans le cas particulier du solveur Rusanov \cite{[291]}. Dans ce cas, pour l'estimation de la vitesse $S^+$, Davis \cite{[103]} a considéré : 


:::{math}
\ S^+ = \max{ \, \left\{ |u_L - a_L| \, , \, |u_R-a_R| \, , \, |u_L + a_L| \, , \, |u_R + a_R|\right\} \, } 
:::
La vitesse ci-dessus est inférieure ou égale à:
:::{math}
\ S^+ = \max{\left\{ |u_L| + a_L\, ,\,|u_R | + a_R \right\}} 
:::
Ce choix est susceptible de produire  un schéma plus robuste et est également plus simple que le choix de Davis.

## Estimations de la vitesse d'onde en fonction de la pression

Il existe plusieurs moyens de calculer la vitesse $S^*$ dans la région étoilée.
On se limitera au calcul de la vitesse d'onde moyenne $S^{*}$ dans le solveur de Riemann approché HLLC .\\

En supposant les solutions pour la pression dans la région étoilée données par :
:::{math}
p_{L}^* = p_L + \rho_L (S_L - u_L)(S_{L}^* - u_L)\quad ;\quad p_{R}^* = p_R + \rho_R(S_R - u_R)(S^* - u_R) 
:::

Nous imposons les conditions suivantes sur les approximations du solveur de Riemann :
:::{math}
\left.
    \begin{array}{lc}
        u_{L}^* = u_{R}^* = u^*   \\
        p_{L}^* = p_{R}^* = p^*    \\
       
    \end{array}
\right \} 
:::
D'après les conditions ci-dessus $p_{L}^* = p_{R}^*$, ce qui conduit à une expression de la vitesse $S^*$ uniquement en termes des vitesses supposées $S_L$ et $S_R$, à savoir:
:::{math}
S^* = \frac{p_R - p_L + \rho_L u_L(S_L - u_L) - \rho_R u_R(S_R - u_R)}{\rho_L (S_L - u_L) - \rho_R (S_R - u_R)}
:::

(content:VF:labels)=
## Méthode du schéma volume finis

On souhaite résoudre ce problème numériquement à l'aide d'une méthode volume finis. D'abord, on partitionne notre domaine d'étude $[x_L;x_R] \times [0;T]$ (où $T>0$ temps maximal). 

On discrétise en $m$ nœuds $x_i$ régulièrement espacés d'un pas $\Delta x$ l'intervalle $[x_L;x_R]$ (on a donc $m-1$ mailles en espace); de même l'intervalle de temps $[0;T]$ est discrétisé en $n$ nœuds  $t^k$ régulièrement espacés d'un pas $\Delta t$ (on a donc $n-1$ mailles en temps). On a : 


:::{math}
t^k=k \Delta t \quad \forall \ k = 1,...,n \quad \text{et} \quad x_{i+\frac{1}{2}} = x_i + \frac{\Delta x}{2} \quad \forall \ i = 1,...,m
:::


:::{figure} ./figures/fig_intervalle.png
:name: fig_hllc
Structure du solveur de Riemann approché HLLC
:::

Sur chaque sous-maille $I_i = [x_{i-\frac{1}{2}};x_{i+\frac{1}{2}}]$, on définit la valeur moyenne de $\pmb{U}(x,t^n)$ la solution exacte au temps $t^n$ par : 

:::{math}
\overline{\pmb{U}_i}^n = \frac{1}{\Delta x} \int_{x_{i-\frac{1}{2}}}^{x_{i+\frac{1}{2}}} \pmb{U}(x,t^n)dx 
:::
et le flux (physique) sur l'interface $x_{i+\frac{1}{2}}$ par : 
:::{math}
\overline{\textit{F}}_{i + \frac{1}{2}}^{\, n} = \frac{1}{\Delta t} \int_{t^n}^{t^{n+1}} \pmb{F(U}(x_{i+\frac{1}{2}}, t^n)dt
:::
On notera $\pmb{U}_i^n$ l'approximation de $\overline{\pmb{U}_i}^n$ et $\textit{F}_{i + \frac{1}{2}}^{\, n}$ l'approximation de $\overline{\textit{F}}_{i + \frac{1}{2}}^{ \, n}$ correspondant au flux numérique au point $x_{i + \frac{1}{2}}$, à l'instant $t^n$. Ainsi, on identifiera $\pmb{U}_h(x,t)$, la valeur approchée de la solution $\pmb{U}(x,t)$, à $\pmb{U}_i^n$ pour $x \in I_i$ et $t \in [t^n;t^{n+1}[$.\\ 
Et pour résoudre numériquement le problème \eqref{problème général}, on utilisera la formule conservative suivante : 
:::{math}
:label: formule conservative
\pmb{U}_i^{n+1} = \pmb{U}_i^{n} + \frac{\Delta t}{\Delta x}(\textit{F}_{i - \frac{1}{2}}^{\, n} - \textit{F}_{i + \frac{1}{2}}^{\, n})
:::
Le flux numérique associé au schéma de Godunov est donné par : 
:::{math}
\textit{F}_{i + \frac{1}{2}}^{\, n} = \pmb{F(U}_{i + \frac{1}{2}}^n(0))
:::
où $\pmb{U}_{i + \frac{1}{2}}^n(0)$ correspond à la solution autosimilaire $\pmb{U}_{i + \frac{1}{2}}^n(\frac{x}{t})$ (ne dépend que de $\frac{x}{t}$) du problème de Riemann évalué en $\frac{x}{t} = 0$ suivant : 

:::{math}
:label: loi de conservation
\left\{
\begin{array}{ll} 
\frac{\partial \pmb{U}}{\partial t} + \frac{\partial \pmb{F(U)}}{\partial x} = 0 \\ \\
\pmb{U}(x,0) = \left\{ \begin{array}{ll}
 \pmb{U_L} \quad \text{si} \quad x>0 \\ 
 \pmb{U_R} \quad \text{si} \quad x>0
\end{array}
\right.
\end{array}
\right.
:::

La droite d'équation $\frac{x}{t} = 0$ correspond à l'axe des $t$ ici. 

On rappelle que le schéma de Gondunov est conservatif, consistant et entropique. 

Pour l'estimation de la vitesse $S^+ \geq 0$ de l'onde présente dans le solveur Rusanov, un autre choix que dans dans la sous-section \ref{estimations vitesses} est possible : $S^+=S_{\max}^{n}$, la vitesse maximale de l'onde présente au moment approprié trouvée en imposant la condition de stabilité  de Courant.

La vitesse est liée à $\Delta t$ (pas de temps) et à l'espacement de la grille $\Delta x$ via la condition CFL :

:::{math}
:label: cfl
\ S_{\max}^{n} = \frac{C_{cfl}  \Delta x}{\Delta t}
:::
où $C_{cfl}$ est le coefficient du nombre de Courant, généralement choisi (empiriquement) comme étant $C_{cfl} \approx 0,9$. On sait que le pas de temps $\Delta t$ de notre schéma numérique ne sera pas constant.  \\ \\
Pour $C_{cfl} = 1$, on a $ S^+ = \frac{\Delta x}{\Delta t}$, ce qui donne le flux numérique de \textbf{Rusanov} : 
:::{math}
\ F_{i+\frac{1}{2}}^n = \frac{1}{2}(\pmb{F_L} + \pmb{F_R}) - \frac{1}{2} \frac{\Delta x}{\Delta t}(\pmb{U_R} - \pmb{U_L})
:::


Enfin, pour définir la solution du problème de Riemann {ref}`loi de conservation`, nous allons utiliser les solutions du problème de Riemann approché que nous avons introduites précédemment.

## Algorithmes pour les flux numériques des solveurs Rusanov, HLL et  HLLC

Pour les calculs des flux numériques, nous allons utiliser les solutions du problème de Riemann approché que nous avons définies précédemment.

Pour implémenter le solveur de Riemann approché Rusanov par la méthode de Godunov \cite{[145]}, on effectue les étapes suivantes :

**Étape 1** : À chaque interface, calculer les vitesses d'onde $S_L$ et $S_R$. 

**Étape 2** : Calculer une seule vitesse d'interface avec $ S^+ = \max(S_L, S_R)$.

**Étape 3** : Calculer le flux intercellulaire de Rusanov . 

$ F_{i+\frac{1}{2}}^{\, n} = \frac{1}{2}(\pmb{F_L} + \pmb{F_R}) - \frac{1}{2} S^+ (\pmb{U_R} - \pmb{U_L})$ et utilisez le dans la formule conservative :
\begin{center}
 $\pmb{U}_{i}^{n+1} = \pmb{U}_{i}^{n} + \frac{\Delta t}{\Delta x} \left(\textit{F}_{i-\frac{1}{2}}^{\, n} - \textit{F}_{i + \frac{1}{2}}^{\, n} \right)$ 
\end{center}  

Pour implémenter le solveur de Riemann approché HLL par la méthode de Godunov \cite{[145]}, on effectue les étapes suivantes:


**Étape 1** : Calculer les vitesses d'onde $S_L$ et $S_R$.

**Étape 2** : Calculer le flux HLL. 

:::{math}
F_{i+\frac{1}{2}}^{hll}  = \left\{ 
\begin{array}{c c}
  \pmb{F_L} & \quad \text{si\, $0 \leq S_L$}\\
  \frac{S_R \pmb{F_L} - S_L \pmb{F_R} + S_L S_R(\pmb{U_R}-\pmb{U_L)}}{S_R-S_L} & \quad \text{si\, $S_L \leq 0 \leq S_R$} \quad,\\ 
 \pmb{F_R} & \quad \text{si\, $0 \geq S_R$} \\ \end{array} \right.
 :::

utilisez-le dans la formule conservative : 
:::{math}
 $\pmb{U}_{i}^{n+1} = \pmb{U}_{i}^{n} + \frac{\Delta t}{\Delta x} \left(\textit{F}_{i-\frac{1}{2}}^{\, n} - \textit{F}_{i + \frac{1}{2}}^{\, n} \right)$ 
:::
Voici les trois étapes pour implémenter le solveur de Riemann approché HLLC par la méthode de Godunov \cite{[145]} : 

**Étape 1** : Calculer les vitesses d'onde $S_L$, $S^*$ et $S_R$. \\ 
**Étape 2** : Calculer les états $\pmb{U_L}$ et $\pmb{U_R}$ en utilisant \eqref{U_K étoile}.                                             \\
**Étape 3** : Calculer le flux HLLC. \\
:::{math}
F_{i+\frac{1}{2}}^{hllc}  = \left\{ 
\begin{array}{c c}
  \pmb{F_L} & \quad \text{si\, $0 \leq S_L$}\\
  \pmb{F_{L}^*} = \pmb{F_L} + S_L (\pmb{U_{L}^*} -\pmb{U_{L}}) & \quad \text{si\, $S_{L} \leq 0 \leq S^*$} \quad,\\ 
   \pmb{F_{R}^*} = \pmb{F_R} + S_R (\pmb{U_{R}^*} -\pmb{U_{R}}) & \quad \text{si\, $S^* \leq 0 \leq S_R$} \quad,\\ 
 \pmb{F_R} & \quad \text{si\, $0 \geq S_R$} \\ \end{array} \right.
:::

et utilisez le dans la formule conservative : 

:::{math}
 $\pmb{U}_{i}^{n+1} = \pmb{U}_{i}^{n} + \frac{\Delta t}{\Delta x} \left(\textit{F}_{i-\frac{1}{2}}^{\, n} - \textit{F}_{i + \frac{1}{2}}^{\, n} \right)$ 
:::


(content:BC:labels)=
## Conditions aux bords transmissives dans le cas des équations Euler unidimensionnelles.

Considérons l'intervalle en espace $[0;L] = [x_1;x_m]$ discrétisé en $m-1$ mailles de longueur $\Delta x$ et le même intervalle en temps que précédemment $[0;T]=[t^1;t^n]$. Nous avons besoin de définir des conditions aux bords en $x=0 \ ( \ =x_1)$ et en $x=L \ ( \ =x_m)$ comme dans la figure \ref{conditions aux bords} . En effet, numériquement ces conditions aux bords doivent nous permettre d'obtenir les flux numériques $\textit{F}_{\frac{1}{2}}^{\, n}$ et $\textit{F}_{m-\frac{1}{2}}^{\, n}$ impliqués dans la formule conservative du schéma de Godunov \cite{[145]} {ref}`formule conservative`. Ainsi, les solutions approchées $\pmb{U}_1^n$ et $\pmb{U}_m^n$ au temps $t=t^n$ pourront être calculées et nous pourrons réitérer ces opérations pour le calcul de la solution approchée au temps $t^{n+1}$,  $\pmb{U}_i^{n+1}$ constante par morceaux, pour $i=1,...,m$.

:::{figure} ./figures/condBord.png
:name: conditions aux bords
Conditions aux bords au temps $t=t^n$. Les flux manquants en dehors du domaine de calcul $[0;L]$ sont créés.
:::

Autrement dit, nous allons imposer des valeurs fictives dans les sous-mailles fictives $I_0$ et $I_m$, adjacentes à $I_1$ et $I_{m-1}$ respectivement. La figure {numref}`conditions aux bords` résume la situation. Ainsi, nous pourrons résoudre les problèmes de Riemann aux interfaces $x_1$ et $x_m$ avec les données à gauche et à droite qui sont $(\pmb{U}_0^n,\pmb{U}_1^n)$ et $(\pmb{U}_{m-1}^n,\pmb{U}_m^n)$ respectivement; les flux de Godunov \cite{[145]} correspondants $\textit{F}_{\frac{1}{2}}^{\, n}$ et $\textit{F}_{m-\frac{1}{2}}^{\, n}$  seront désormais calculables pour les mailles incluses dans notre domaine de calcul $[0;L]$.

L'imposition des conditions aux bords est essentiellement un problème physique. Il faut donc que l'implémentation numérique des conditions aux bords soit faite avec prudence. Ici, nous considérerons seulement des bords dits *transmissifs* ou encore *transparents*. 

Les bords *transmissifs* nécessitent un domaine de calcul suffisamment petit. les conditions aux bords correspondantes sont insensibles au passage des ondes traversant les bords. Il n'y a donc aucune modification possible des conditions aux bords. Ce type de bords suffit pour les problèmes unidimensionnel. Finalement, dans le cas des équations d'Euler 1D, dépendantes du temps, pour un bord droit transmissif on considère les conditions aux bords suivantes : 

:::{math}
 \rho_{m-1}^n = \rho_m^n, \quad m_{m-1}^n = m_m^n , \quad E_{m-1}^n = E_m^n
:::

Et pour un bord gauche transmissif, on considère les conditions aux bords : 

:::{math}
\rho_0^n = \rho_1^n, \quad m_0^n = m_1^n, \quad E_0^n=E_1^n
:::

produisant une problème de Riemann trivial. Dans la partie numérique, nous ne ferons que des cas tests où la solution restera inchangée aux bords.

