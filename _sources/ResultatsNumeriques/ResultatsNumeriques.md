# Résultats numériques

Dans cette section, nous allons tester nos fonctions écrites sur Matlab {\small\texttt{Euler.m}} et {\small{\texttt{fluxnum.m}}}, données à la section  {ref}`codes`, qui implémentent les trois solveurs de Riemann approchés précédemment introduits. On obtiendra ainsi une solution approchée aux 3 problèmes de Riemann considérés. Nos fonctions permettent de tracer la densité $\rho$, la vitesse $u$, la pression $p$ et l'énergie interne spécifique $\epsilon$ de la solution. Nous comparerons les résultats obtenus pour les différents cas tests des 3 solveurs.


On a sélectionné 3 cas tests définis dans le tableau {ref}`données` pour les équations d'Euler 1D avec $\gamma=1.4$. Ceux-ci ont des solutions exactes et permettent de vérifier si notre schéma numérique fonctionne bien. Ainsi, nous pourrons évaluer la performance des 3 solveurs de Riemann approchés par la méthode du premier ordre de Godunov \cite{[145]} en remarquant lequel approche le plus la solution exacte. De plus, ces tests permettent de représenter quelques modèles d'ondes résultants de la solution du problème de Riemann. On décide de représenter les solutions exactes et numériques sur l'intervalle en espace $[0,1]$. On prendra pour tous les cas tests un nombre de mailles $M=100$ et la condition CFL {ref}`cfl`; le coefficient du nombre de Courant $C_{cfl}=0.9$; les conditions aux bords seront transmissives. 


Les solutions exactes ont été obtenues en important et traçant sous Matlab les données des fichiers \textbf{.dat} qui nous ont été fournis.

```{list-table} Données des 3 cas tests
:header-rows: 1
:name: données
* - Test
  - $\rho_L$
  - $u_L$
  - $p_L$
  - $\rho_R$
  - $u_R$
  - $p_R$
* - 1
  - 1.0 
  - 0.0
  - 1.0
  - 0.125
  - 0.0
  - 0.1
* - 2
  - 1.0
  - -2.0
  - 0.4
  - 1.0
  - 2.0
  - 0.4
* - 3
  - 1.0
  - 0.0
  - 1000.0
  - 1.0
  - 0.0
  - 0.01
```

La solution exacte est représentée en trait rouge continu et la solution approchée est en pointillés noirs. 

Le cas test 1 correspond au problème de Sod \cite{[318]}. 

### Description des systèmes d'ondes résultants des solutions aux 3 problèmes de Riemann considérés :

Dans la sous-section {ref}`cas test 1`, on présente les résultats numériques obtenus pour le cas test 1 par la méthode de Godunov \cite{[145]} du premier ordre avec les trois solveurs de Riemann approchés Rusanov, HLL et HLLC. On voit que la solution se compose d'une onde de détente sonique à gauche, d'une onde de contact se déplaçant vers la droite et d'une onde de choc à droite.  


De même, dans la sous-section {ref}`cas test 2` on présente les résultats numériques obtenus pour le cas test 2. On voit que la solution consiste en deux ondes de détente symétriques et une discontinuité de contact. 


Enfin, dans la sous-section {ref}`cas test 3` on considère les résultats numériques obtenus pour le cas test 3. La solution consiste en une onde de détente à gauche, une discontinuité de contact et une onde de choc à droite. 


Avant confronter nos solveurs approchés, nous allons comparer la solution numérique avec la solution exacte pour un de nos trois solveurs, HLLC dans le cas test 1 par exemple. Sur le figure {ref}`convergence` on voit qu'en augmentant le nombre de mailles, la solution approchée converge bien vers la solution exacte.

:::{figure} ./figures/convergence.png
:name: convergence
Solution approchée obtenue par la méthode volume finis du premier ordre de Godunov pour le cas test 1. $\pmb{x_0}=0.5$ et $\pmb{T}=0.2$ et $M=1000$.
:::

**Cas test 1** : le solveur Rusanov approche moins bien la solution exacte que les solveurs HLL et HLLC. Mais le solveur HLL approche mieux la solution exacte que le solveur HLLC. 
**Cas test 2** : de même que dans le cas test 1, sauf que la différence est moins visible. Néanmoins, on remarque que les résultats numériques obtenus pour l'énergie interne ne sont pas satisfaisants.
**Cas test 3** : mêmes constatations que dans les autres cas tests sauf que HLLC approche mieux l'énergie interne que HLL.

Le *second principe de la thermodynamique* définit une nouvelle variable $s$, appelée l'entropie, via la relation suivante :

:::{math}
T \, ds = d \, \epsilon + p \, dv \, ,
:::

où $T$ correspond à la température et $v=\frac{V}{m}$ le volume spécifique avec $V$ le volume totale du système et $m$ sa masse.

On a donc la relation suivante :


:::{math}
d \, \epsilon = T \, ds - p \, dv
:::

Ainsi, l'énergie interne est conjointement liée à l'entropie. 

De plus, l'entropie d'un système isolé (ce qui est notre cas) ne peut qu'augmenter ou rester constante puisqu'il n'y a pas d'échange de chaleur avec le milieu extérieur. En effet :

* dans le cas d'une *transformation irréversible* tel qu'un choc, on a production d'entropie;

* dans le cas d'une *transformation réversible* tel qu'une discontinuité de contact, l'entropie est conservée. On parle de processus *isentropique*.


Par là, on peut comprendre pourquoi nos solveurs n'approchent pas bien l'énergie interne dans nos trois cas tests. En effet, dans nos trois solveurs de Riemann approchés on ne considère que des chocs donc il est compréhensible d'avoir des erreurs quand des ondes de détente apparaissent dans le modèle d'ondes de la solution du problème de Riemann considéré. On représente mal les ondes de détente. Or, dans les trois cas tests au moins une onde de détente est présente... En fait, la dissipation du schéma numérique présente dans la solution approchée obtenue pour l'énergie interne est directement liée à la création d'entropie à travers la détente. Ceci est dû au fait que l'entropie doit être conservée à travers une détente car la solution à travers une détente est régulière.

 De plus, le solveur Rusanov est le plus dissipatif car on pose $S_L=-S^+$ et $S_R=S^+$. On considère donc un cône formé par les ondes gauche et droite trop large et on perd en précision. Pour les solveurs HLL et HLLC, leur différence n'est pas notable. Ajoutons à cela qu'on travaille avec une méthode numérique d'ordre 1, on ne peut donc pas espérer des résultats ultra précis car plus l'ordre de la méthode est grand, plus l'erreur sera petite. 
 
 Enfin, pour avoir une meilleur approximation, il existe des solveurs qui prennent en compte la présence d'ondes de détente comme le solveur **TRRS** (voir page 303 du livre de E.F. Toro, Riemann Solvers and Numerical Methods for Fluid Dynamics , A Practical Introduction).

(content:cas test 1:labels)=
 ## Résultats numériques obtenus pour le cas test 1

:::{figure} ./figures/Rusanov1.png
:name: Rusanov1
Résultats obtenus par la méthode de Godunov avec le solveur de Riemann approché **Rusanov** pour le cas test $1$, avec $\pmb{x_0=0.5}$ au temps $\pmb{T=0.2}$.
:::

:::{figure} ./figures/HLL1.png
:name: HLL1
Résultats obtenus par la méthode de Godunov avec le solveur de Riemann approché **HLL** pour le cas test $1$, avec $\pmb{x_0=0.5}$ au temps $\pmb{T=0.2}$.
:::

