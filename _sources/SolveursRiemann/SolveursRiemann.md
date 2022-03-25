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




(content:BC:labels)=
## Conditions aux bords transmissives dans le cas des équations Euler unidimensionnelles.

(content:estimationsVitesse:labels)=
## Estimations de la vitesse des ondes directes