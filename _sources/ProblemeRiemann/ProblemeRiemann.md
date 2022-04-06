# Problème de Riemann associé aux équations d'Euler en 1D

Dans cette section, on présente la méthode de résolution du problème de Riemann pour les équations d'Euler en 1D pour des gaz parfaits.


## Procédure de résolution du problème de Riemann associé au système d'Euler unidimensionnelles dépendantes du temps

Dans cette sous-section, nous nous focalisons sur le système des équations d'Euler en coordonnées eulériennes. 
Dans un premier temps, nous allons prouver que les équations d'Euler forment un système strictement hyperbolique de lois de conservation. Nous donnerons ensuite la structure propre des équations, en particulier les valeurs propres. Enfin, nous étudierons la forme de la solution complète du problème de Riemann associé aux équations d'Euler 1D dépendantes du temps. 

On considère le système différentiel non linéaire de lois de conservation suivant :

:::{math}
\left\{
\begin{array}{r c l}
 \dfrac{\partial \rho}{\partial t} + \dfrac{\partial (\rho u)}{\partial x}  &=& 0 \, , \\
 \dfrac{\partial(\rho u)}{\partial t} + \dfrac{\partial(\rho u^2 + p)}{\partial x} &=& 0 \, , \\
 \dfrac{\partial\rho e}{\partial t} + \dfrac{\partial[(\rho e + p)u]}{\partial x} &=& 0 \, ,
\end{array} 
\right.
:::

qui s'écrit vectoriellement : 

:::{math}
:label: conservation law
 \boxed{\frac{\partial \pmb{U}}{\partial t} + \frac{\partial \pmb{F(U)}}{\partial x} = \pmb{0}} 
:::


où $\pmb{U}$ est le vecteur des variables conservatives et $\pmb{F(U)}$ le vecteur flux, définis par : 

:::{math}
:label: les vecteurs
\pmb{U}=\begin{pmatrix} \rho \\ \rho u \\ \rho e \end{pmatrix} = \begin{pmatrix} \rho \\ m \\ E \end{pmatrix}, \quad \pmb{F(U)}=\begin{pmatrix} \rho u \\ \rho u^2 + p \\ (\rho e + p)u \end{pmatrix} = \begin{pmatrix} m \\ \dfrac{m^2}{\rho} + p \\ (E + p)\dfrac{m}{\rho} \end{pmatrix}.
:::

Pour l'instant, le système {eq}`conservation law`-{eq}`les vecteurs` précédent est écrit sous sa **forme conservative**.

On cherche à réécrire ce système de lois de conservation {eq}`conservation law` - {eq}`les vecteurs` sous forme quasilinéaire, c'est-à-dire sous la forme non conservative : 

:::{math}
\partial_t \pmb{U} + \pmb{A(U)} \partial_x \pmb{U} = \pmb{0}
:::

où $\pmb{A(U)} = \partial_U(\pmb{F(U)}) \in M_{3 \times 3}(\mathbb{R})$ la matrice jacobienne de $\pmb{F(U)}$ :  



:::{math}
\pmb{A(U)} = \begin{pmatrix}
\displaystyle \frac{\partial F_1}{\partial \rho} & \frac{\partial F_1}{\partial m} & \frac{\partial F_1}{\partial E} \\
\displaystyle \frac{\partial F_2}{\partial \rho} & \frac{\partial F_2}{\partial m} & \frac{\partial F_2}{\partial E} \\
\displaystyle \frac{\partial F_3}{\partial \rho} & \frac{\partial F_3}{\partial m} & \frac{\partial F_3}{\partial E}
\end{pmatrix}.
:::


Pour cela, on exprime les composantes du flux $\pmb{F(U)}$ en fonction de celles de $\pmb{U}$ vecteur des variables conservatives. Comme nous étudions des gaz parfaits, on a l'équation d'état suivante : 
:::{math}
\epsilon = \frac{p}{(\gamma -1)\rho} \, ,
::: 

où $\gamma=\dfrac{c_p}{c_v}$ le rapport des capacités thermique $c_p$ à pression constante et $c_v$ à volume constant.
On peut alors exprimer la pression en fonction des composantes du vecteur $\pmb{U}$. 

On rappelle que $e=\epsilon + \frac{1}{2} u^2 \Leftrightarrow{\epsilon = e-\frac{1}{2} u^2}$.
:::{math}
\begin{align*}
p(\pmb{U})=(\gamma - 1)\rho \epsilon &= (\gamma - 1) \rho (e - \frac{1}{2} u^2) \\ &= (\gamma - 1)(\rho e - \frac{1}{2} \rho u^2) \\ 
&= (\gamma - 1)\left(E - \frac{1}{2} \frac{m^2}{\rho}\right)
\end{align*}
:::

On a directement que $F_1=m$.

:::{math}
\begin{align*}
F_2 &= \frac{m^2}{\rho} + p(\pmb{U}) \\
   &= \frac{m^2}{\rho} + (\gamma - 1)\left(E - \frac{1}{2} \frac{m^2}{\rho}\right) \\
   &= \frac{3}{2} \frac{m^2}{\rho} + (\gamma - 1)E - \frac{1}{2} \gamma \frac{m^2}{\rho} \\ 
   &= \frac{(3-\gamma)}{2} \frac{m^2}{\rho} + (\gamma - 1)E
\end{align*}
:::

:::{math}
\begin{align*}
F_3 &= (\rho e + p(\pmb{U}))u \\
  &= \left(E + (\gamma - 1)\left(E - \frac{1}{2} \frac{m^2}{\rho}\right) \right) \frac{m}{\rho} \\
  &= \left(\gamma E - \frac{(\gamma - 1)}{2} \frac{m^2}{\rho} \right) \frac{m}{\rho}
\end{align*}
:::

Donc le vecteur flux exprimé avec les variables conservatives est : 

:::{math}
\pmb{F(U)} = 
\begin{pmatrix}
m \\ 
\dfrac{(3-\gamma)}{2} \dfrac{m^2}{\rho} + (\gamma - 1)E \\ 
\left(\gamma E - \dfrac{(\gamma - 1)}{2} \dfrac{m^2}{\rho} \right) \dfrac{m}{\rho},
\end{pmatrix}.
:::
Maintenant, on calcule la matrice jacobienne $\pmb{A(U)}$ de $\pmb{F(U)}$ en variables conservatives : 
 
:::{math}
\pmb{A(U}) = \begin{pmatrix}
	0 & 1 & 0 \\
	\dfrac{\gamma - 3}{2}\dfrac{m^2}{\rho^2} & (3 - \gamma)\dfrac{m}{\rho} & \gamma - 1 \\
	(\gamma - 1) \dfrac{m^3}{\rho^3} - \dfrac{\gamma E m}{\rho^2} & - \dfrac{3}{2}(\gamma - 1) \dfrac{m^2}{\rho^2} + \dfrac{\gamma E}{\rho} & \dfrac{\gamma m}{\rho} 
	\end{pmatrix}.
:::
Après, en utilisant que le moment $m=\rho u$, que l'énergie totale $E=\rho e$ puis que la vitesse du son $a = \sqrt{\dfrac{\gamma p}{\rho}}$, 

 


:::{math}
\pmb{A(U)} = \begin{pmatrix}
		0 & 1 & 0 \\
		\dfrac{\gamma - 3}{2} u^2 & (3- \gamma)u & \gamma - 1 \\
		(\gamma - 1)u^3 - \gamma e u & - \dfrac{3}{2} (\gamma - 1)u^2 + \gamma e & \gamma u 
		\end{pmatrix} 
		=
		\begin{pmatrix}
		0 & 1 & 0 \\
		\dfrac{\gamma - 3}{2} u^2 & (3- \gamma)u & \gamma - 1 \\
		\dfrac{1}{2}(\gamma - 2)u^3 - \dfrac{a^2 u}{\gamma - 1} & \dfrac{3 - 2 \gamma}{2} u^2 + \dfrac{a^2}{\gamma - 1} & \gamma u
		\end{pmatrix}
:::



Le système d'équation {eq}`conservation law`-{eq}`les vecteurs` s'écrit alors sous la forme souhaitée : 

:::{math}
:label: conservation law
\boxed{\partial_t \pmb{U} + \pmb{A(U)} \, \partial_x \pmb{U} = \pmb{0}}
\label{}
:::

Or, on sait que si $\pmb{A(U)}$ est diagonalisable à valeurs propres réelles alors le système est *hyperbolique*. De plus, si les valeurs propres sont distinctes, on dit que le système est *strictement hyperbolique*. C'est le cas du système des équations d'Euler 1D, dépendantes en temps pour les gaz parfaits.
En effet, des calculs fastidieux (calculer le polynôme caractéristique à partir de la dernière expression obtenue pour la matrice $\pmb{A(U)}$) donnent l'existence de trois valeurs propres réelles distinctes : $\lambda_1 = u-a$, $\lambda_2=u$ et $\lambda_3 = u+a$ (valeurs propres réelles distinctes tant que la vitesse du son $a >0$). 
 
$\pmb{A}$ se décompose telle que : 

:::{math}
\pmb{A}=\pmb{P} \pmb{\Lambda} \pmb{P}^{-1}
::: 
où : 
:::{math}
\pmb{\Lambda} = \textbf{diag(}\lambda_1, \lambda_2, \lambda_3 \textbf{)}
:::
et
:::{math}
\pmb{P} = \left[\pmb{V_1} | \pmb{V_2} | \pmb{V_3} \right].
:::
la matrice de passage formée des vecteurs propres à droite de la matrice $\pmb{A(U)}$.

C'est-à-dire : 

:::{math}
\pmb{AV_k}=\lambda_k \pmb{V_k} \quad k=1,..,3 
:::

L'équation {eq}`conservation law` se réécrit alors : 

:::{math}
\partial_t \pmb{U} + \pmb{P} \pmb{\Lambda} \pmb{P}^{-1} \, \partial_x \pmb{U} = \pmb{0}
:::

Puis en multipliant par $\pmb{P}^{-1}$, on a : 

:::{math}
\partial_t \pmb{P}^{-1} \pmb{U} + \pmb{\Lambda} \, \partial_x \pmb{P}^{-1} \pmb{U} = \pmb{0}
:::

En posant $\pmb{R}=\pmb{P}^{-1} \pmb{U}$, où les $R_i$, $i=1..3$ sont les *invariants de Riemann*. Cela revient à : 

:::{math}
\partial_t \pmb{R} + \pmb{\Lambda} \, \partial_x \pmb{R} = \pmb{0}
:::

Comme $\pmb{\Lambda}$ est une matrice diagonale, on a un système composé de 3 équations de transport à coefficients variables. Il y a 3 courbes caractéristiques; celle associée à la $k^{\text{ième}}$ valeur propre est solution de : 

:::{math}
\left\{
\begin{array}{ll}
\dfrac{d x(t)}{dt} = \lambda_k(\pmb{U}(x(t),t) \, , \\[4mm]
x(0) = x_0.
\end{array}
\right.
:::
pour tout $x_0$; on décide de prendre $x_0=0$.
Les trois courbes caractéristiques présentes dans la solution exacte du problème de Riemann sont tracées sur la figure {numref}`structure de la solution`.

:::{figure} ./figures/solution_Riemann.png
:name: structure de la solution
Structure de la solution du problème de Riemann dans le plan $(x,t)$ pour les équations d'Euler 1D dépendantes du temps. Les trois ondes sont associées aux valeurs propres $u-a$, $u$ et $u+a$ respectivement.
:::

(content:analyseDesOndes:labels)=
## Analyse des ondes élémentaires du problème de Riemann

%%{ref}`content:analysedesondes:labels`

Maintenant, on va décrire la structure complète de la solution du problème de Riemann sous forme d'un ensemble d'ondes élémentaires telles que des ondes de détente, des discontinuités de contact et des ondes de choc. Des relations classiques existent entre ces ondes et nous seront utiles dans la sous-section qui suit pour relier les états inconnus aux états donnés et donc pour trouver la solution complète du problème de Riemann. 

 
 Le problème de Riemann dans le cas des équations d'Euler unidimensionnelles, dépendantes en temps {eq}`conservation law` - {eq}`les vecteurs` avec la condition initiale à deux états $(\pmb{U_L}, \pmb{U_R})$ est donné par : 
 
 :::{math}
 :label: solution_Riemann
 \left.
 \begin{array}{ll}
 \pmb{U}_t + \pmb{F(U)}_x = 0 , \\ 
 \pmb{U}(x,0) = \pmb{U}^{(0)}(x) = \left\{
 \begin{array}{ll}
\pmb{ U_L} \quad \text{si} \; x<0, \\ 
 \pmb{U_R} \quad \text{si} \; x>0.
 \end{array} 
 \right. \\ 
 \end{array} \right\}
:::

:::{figure} ./figures/fig2_2.png
:name: structure de la solution2
Structure de la solution autosimilaire du problème de Riemann pour les équations d'Euler unidimensionnelles.
:::

Avant de continuer, introduisons la notion de *champs caractéristique*. Comme nous considérons un système hyperbolique de lois de conservation avec des valeurs propres réelles $\lambda_k(\pmb{U})$, la vitesse caractéristique $\lambda_k(\pmb{U})$ définit un *champs caractéristique*. Suivant la numérotation de la vitesse caractéristique, on parle de $k^{eme}$ champ caractéristique.
 Ici, il apparaît trois ondes associées à trois champs caractéristiques définis par les vitesses caractéristiques $\lambda_1 = u-a$, $\lambda_2 = u$ et $\lambda_3=u+a$ respectivement. Les trois ondes séparent quatre états constants. Comme nous l'avons dit précédemment, on a trois types d'ondes dans la solution qui sont respectivement : des ondes de détente, des discontinuités de contact et des ondes de choc. Afin, d'analyser le type de chacune des ondes présentes dans la solution du problème de Riemann, il faut étudier la nature des champs caractéristiques. 
La nature des champs caractéristiques nous informent sur le type des ondes présentes dans la solution. 



L'onde associé au $2^{eme}$ champ caractéristique est une discontinuité de contact et celles associées aux $1^{er}$ et $3^{eme}$ champs caractéristiques seront soit des ondes de raréfaction (lisses) soit des ondes de choc (discontinues). On ne peut donc pas savoir en avance les types des ondes présentes dans la solution exacte du problème de Riemann, à l'exception de l'onde du milieu qui sera toujours une discontinuité de contact.


 Il est important de noter qu'à travers des ondes de raréfaction ou de choc les variables primitives changeront. Ce qui fait la différence c'est que dans le cas d'une onde de détente, les variables primitives changent mais sont continues tandis que dans le cas d'une onde de choc, elles changent et sont discontinues ; lors de l'étude d'un choc, on utilisera les conditions de Rankine-Hugoniot. Enfin, une discontinuité de contact est une onde discontinue à travers de laquelle la pression et la vitesse particulaire restent constantes mais avec un saut en densité. Donc, les variables dépendants de la densité seront aussi discontinues comme par exemple la température et la vitesse du son.  

 ## Procédure de résolution du problème de Riemann associé au système d'Euler unidimensionnelles dépendantes du temps

 Après l'étude de l'ensemble des ondes élémentaires présentes dans la structure de la solution du problème de Riemann associé aux équations d'Euler monodimensionnelles, dépendantes du temps ; on connaît les propriétés qu'auront les variables primitives à travers chacune de ces ondes. De plus, on a vu que dans le cas des équations d'Euler, on peut voir le problème de Riemann comme une généralisation du problème dit du tube à choc, problème physique fondamental en dynamique des gaz. Pour une description détaillée du problème des tubes à choc, voir le livre de Courant et Friedrichs {cite}`[97]`. Nous allons présenter dès à présent, une procédure de résolution du problème de Riemann pour le système d'Euler unidimensionnelles dépendantes du temps. 
 
 
Pour l'étude du problème de Riemann associé au système d'équations d'Euler 1D, on se ramène à la forme conservative des équations :
 
:::{math}
:label: loi_conservation
\
 \left\{
    \begin{array}{ll}
        
  \frac{\partial \pmb{U}}{\partial t} + \frac{\partial \pmb{F(U)}}{\partial t} = 0, 
  
  
 \\ \\ 
 \pmb{U} = \begin{pmatrix}
 \rho \\
 \rho u \\
 \rho e \\
 \end{pmatrix}, \quad \pmb{F(U)}= \begin{pmatrix}
 \rho u \\
 \rho u^2 + p \\
 u(\rho e + p) \\
 \end{pmatrix}.
      
    \end{array}
\right. 
:::

On ajoute la condition initiale à deux états suivante :  

:::{math}
:label: condition_init
\pmb{U}(x,0) = \pmb{U}^{(0)}(x) =
\left\{
\begin{array}{ll}
 \pmb{U_L} \quad \text{si} \quad x<0 \\
 \pmb{U_R} \quad \text{si} \quad x>0 
\end{array}
\right.
:::

On se place dans le plan $(x,t)$ avec $t>0$ et $x \in \mathbb{R}$. On considère un intervalle borné en espace $[x_L;x_R]$ centré en $x=0$. Pour la résolution du problème de Riemann {eq}`loi_conservation`- {eq}`condition_init`, on utilisera les variables primitives plutôt que les variables conservatives. On notera le vecteur des variables primitives : 
:::{math}
\pmb{W} = \begin{pmatrix}
\rho \\
u \\
p
\end{pmatrix}
:::
La condition initiale correspond alors aux deux états constants suivants: 

:::{math}
\pmb{W}(x,0)=\pmb{W^{(0)}}(x) = \left\{ \begin{array}{ll}
 \pmb{W_L} = \begin{pmatrix} 
 \rho_L \\
 u_L \\ 
 p_L 
 \end{pmatrix} \quad \text{si} \quad x<0 \\ \\ 
 \pmb{W_R} = \begin{pmatrix} 
 \rho_R \\
 u_R \\ 
 p_R \end{pmatrix} \quad \text{si} \quad x>0 
\end{array}
\right.
:::

Par la sous-section {ref}`analyseDesOndes`, on sait que ces deux états constants seront toujours séparés pas une discontinuité de contact en $x=0$. De plus, à travers de celle-ci la vitesse particulaire et la pression du fluide seront constantes. D'où l'intérêt de travailler avec les variables primitives. Cette propriété va simplifier notre problème. 

On cherche une solution $\pmb{W}(x,t)$ autosimilaire car ne dépendant que de $\dfrac{x}{t}$. 

On a également vu que la solution du problème de Riemann associé aux équations d'Euler monodimensionnelles présentera toujours une discontinuité de contact (onde du milieu) et deux ondes non linéaires qui, chacune peut être soit un choc soit une onde de détente. Dans notre mémoire, on se restreint aux cas où il n'y a pas de vide (cas où on a une densité nulle). 

 Ainsi, ces trois ondes séparent quatre états constants (voir la figure {numref}`fig`})  

:::{figure} ./figures/figmem1.png
:name: fig
Forme de la solution du problème de Riemann pour les équations d'Euler 1D dépendantes du temps.
:::

On appelle la zone comprenant les états intermédiaires du problème de Riemann, la zone étoilée. Dans celle-ci, deux nouveaux états constants apparaissent : $\pmb{W_L^*}$ et $\pmb{W_R^*}$. 

Étant donné que les ondes non linéaires peuvent être soit un choc soit une onde de détente, il suffira de considérer les quatre configurations d'ondes possibles de la figure {numref}`lesQuatreCasPossibles` pour l'élaboration d'un schéma numérique de la solution pour le problème de Riemann :  


* onde de choc - discontinuité de contact - onde de choc,  
* onde de détente - discontinuité de contact - onde de choc, 
* onde de choc - discontinuité de contact - onde de détente, 
* onde de détente - discontinuité de contact - onde de détente


Cependant, il y a beaucoup plus de cas possibles que ceux présentés sur la figure {numref}`lesQuatreCasPossibles`. En effet, la répartition des ondes dépend du signe des vitesses caractéristiques $\lambda_i$ pour $i=1,...,3$. Les ondes peuvent soit être du même côté, soit de part et d'autre de l'axe $t$.

:::{figure} ./figures/figmodeles.png
:name: lesQuatreCasPossibles
Les 4 systèmes d'ondes possibles dans la solution du problème de Riemann.
:::

On rappelle qu'à travers la discontinuité de contact, la vitesse particulaire $u^*$ et la pression $p^*$ sont constantes; par contre la densité $\rho^*$ est discontinue. 

Ainsi, 

:::{math}
\rho^* = \left\{
\begin{array}{ll}
\rho_L^* \quad \text{si} \quad x \in ]u-a;u[ \\ \\ 
\rho_R^* \quad \text{si} \quad x \in  ]u; u+a[ 
\end{array} \right.
:::

De cette façon, comme la densité est discontinue dans la zone étoilée; il en est de même pour toutes les variables qui en dépendent (énergie interne spécifique, température, vitesse du son $a$, entropie...). 

En pratique, le calcul de $u^*$ peut se ramener à une unique équation non linéaire en $p^*$ qui peut se résoudre à l'aide d'une méthode itérative (méthode de Newton, méthode du point fixe...). Donc une fois $p^*$ connue, on peut déduire $u^*$, $\rho_L^*$ et $\rho_R^*$. 


Mais au vue du nombre de situations possibles et de la complexité de la relation non linéaire qui relie $u^*$ et $p^*$, en pratique on utilisera plutôt des solveurs de Riemann approchés.
