# Lois de conservation 

Dans cette section, on étudie les équations régissant la dynamique des fluides compressibles, en particulier les gaz pour lesquels on négligera les forces dues à la gravité, les contraintes de cisaillement et les flux de chaleur appliqués. On se restreindra aux gaz parfait (non visqueux). Ces équations forment le **système d'Euler**. Dans tout notre mémoire, on travaille en dimension un. D'abord, on trouve la formulation intégrale des équations d'Euler unidimensionnelles en coordonnées eulériennes et lagrangiennes respectivement. Ensuite, on écrit la formulation différentielle des équations d'Euler dépendantes du temps, unidimensionnelles. 

:::{note}
:class: dropdown
Deux types de variables sont possibles pour exprimer nos équations :

* Les **variables conservatives** : la densité $\rho$, le moment $m$ et l'énergie totale $E$ du gaz qui apparaissent dans la deuxième loi de Newton, les lois de conservation de la masse, de la quantité de mouvement et de l'énergie totale. 
* Les **variables primitives** ou variables physiques ($\rho$, $u$, $p$) où $u$ est la vitesse particulaire et $p$ la pression du gaz.
:::

Ici, nous allons exprimer les équations d'Euler en variables conservatives en supposant que les quantités impliquées c'est-à-dire la densité $\rho$, le moment $m=\rho u$ et l'énergie totale $E=\rho e$, où $e$ est l'énergie totale spécifique soient suffisamment régulières pour que la différentiation soit possible. Cependant, lorsqu'on considérera le cas d'un choc par exemple, on retirera cette hypothèse pour pouvoir définir des solutions discontinues (donc des variables discontinues).   

Nous allons à présent introduire les outils mathématiques nécessaires qui vont nous permettre d'obtenir le système des équations d'Euler en 1D en coordonnées eulériennes et lagrangiennes. En particulier, la formule de Reynolds. Dans toute la suite on travaillera en 1D. 

## Formule de transport de Reynolds

:::{math}
:label: formule de Reynolds
\frac{d}{dt}\int_{\omega (t)} f(x,t)dx = \int_{\omega (t)} \left( \partial_t f(x,t) + \partial_x (f(x,t)\,v(x)) \right)dx.
:::

Tous les points bougent avec la vitesse du fluide, on note $x(X,t)$ la position d'un point du fluide à l'instant t, initialement localisé à X. 

On introduit les *courbes caractéristiques* : 

$$
\left\{
\begin{array}{ll}
\displaystyle \frac{\partial x(X,t)}{\partial t} = u(x(X,t),t) \, , \\[4mm]
x(X,0) = X. \\
\end{array} 
\right. 
$$

On définit le *Jacobien de la transformation* : 
:::{math}
J(x,t) = \frac{\partial x(X,t)}{\partial X}.
:::

$\bullet$ Soit $\varphi : \omega (t) \times \mathbb{R} \longrightarrow \mathbb{R}$ une fonction régulière. On définit la dérivée totale : 
:::{math}
\frac{d \varphi}{dt} = \frac{\partial \varphi}{\partial t} + \frac{\partial x}{\partial t} \  \frac{\partial \varphi}{\partial x}.
:::

Soit $I(t) = [x_1(t) \, , \, x_2(t)]$ un volume de contrôle.

Pour $i=1,2$ : $X_i = x_i(0) = x(X_i,0)$ et $ x_i(t) = x(X_i,t) $

 Dans la suite, nous allons établir nos équations en coordonnées eulériennes $x$ et en coordonnées lagrangiennes $X$ respectivement.

 ## Conservation de la masse

La masse totale contenue dans un volume matérielle $I(t)$ est donnée par : 

$$ m(I(t)) = \int_{I(t)} \rho(x,t)dx. $$

Celle-ci étant constante, on a : 

$$ \frac{dm(I(t))}{dt} = 0 $$ 


C'est-à-dire, par la *formule de Reynolds* : 
:::{math}
\int_{I(t)}\left(\frac{\partial \rho}{\partial t} + \frac{\partial(\rho \, u)}{\partial x}\right)dx = 0 \, , \quad \forall \, I(t) \; \text{volume de contrôle}. 
:::

Ce qui correspond à la version intégrale de la conservation de la masse. 

Autre écriture : 

:::{math}
\int_{I(t)} \frac{\partial \rho}{\partial t}dx + [\rho \, u]_{x_1(t)}^{x_2(t)} = 0 
:::

Donc, comme le volume de contrôle $I(t)$ est arbitraire, il faut que :


 :::{math}
 \boxed{\frac{\partial \rho}{\partial t} + \frac{\partial(\rho \, u)}{\partial x} = 0  \quad \textbf{conservation de la masse (formalisme eulérien)}.}
 :::  

 
 C'est-à-dire la version locale de la conservation de la masse en eulérien.

On exprime maintenant la conservation de la masse en lagrangien. Par un changement de variable, on a : 

:::{math}
\frac{d}{dt} \int_{I(0)} \rho(x(X,t),t) \, J(X,t)dX = 0 
:::

i.e
:::{math}
\int_{I(0)} \frac{d}{dt}\left(\rho(x(X,t),t)\, J(X,t)\right)dX = 0
:::


donc 
:::{math}
\frac{d}{dt}\left(\rho(x(X,t),t)J(X,t)\right)=0
:::

c'est-à-dire : 
:::{math}
\rho(x(X,t),t)J(X,t)= \rho(x(X,0),0)J(X,0)= \rho(X,0).1= \rho_0(X)   
\quad \left(car \ J(X,0)= \frac{\partial x(X,0)}{\partial X}= \frac{\partial X}{\partial X}=1\right) 
:::
où $\rho_0(X) \ $ est densité initiale.

:::{math}
\boxed{\rho(x(X,t),t)J(X,t)= \rho_0(X) \quad \textbf{conservation  de  la  masse  (formalisme lagrangien)}.}
:::  
On vient d'obtenir la version locale de la conservation de la masse en lagrangien.

Avant de continuer sur d'autres lois de conservation, on va établir une formule que l'on utilisera ultérieurement.

Soit $\varphi$ une fonction régulière: 
:::{math}
\begin{align*}
 \frac{d}{dt} \int_{I(t)} \rho\,\varphi\,dx &= \int_{I(0)} \frac{d}{dt}(\rho\, J \, \varphi)dX \\
&= \int_{I(0)} \rho\ J \frac{d\varphi}{dt}dX \\
&= \int_{I(t)} \rho \frac{d\varphi}{dt}dx\\ 
\end{align*}
:::

On obtient : 
:::{math} 
   :label: dérivée particulaire
  \boxed{\frac{d}{dt} \int_{I(t)} \rho\,\varphi\,dx = \int_{I(t)} \rho \frac{d\varphi}{dt}dx} 
:::

## Conservation du moment

La résultante des forces exercées sur notre système est décrite par deux composantes : 

* une pour les forces extérieures, en l'occurrence la force de pesanteur; 
* une pour les forces de contact exercées par le fluide environnant;

La première est nulle par hypothèse. 
La seconde est définie à l'aide d'un tenseur des contraintes $\sigma \,$.

De plus, pour les fluides newtoniens la loi de comportement est : 
:::{math}
\sigma = -p \, \pmb{Id} +  \pmb{\Pi}
:::
où : $p= p(x,t)$ correspond à la pression et $\mu > 0$ à la viscosité dynamique du fluide; $\pmb{\Pi}$ est le tenseur des contraintes visqueuses.  
Dans notre cas, on se restreint aux gaz parfaits : $\pmb{\Pi} = \pmb{0}$. Le tenseur des contraintes est donc : 
:::{math}
\sigma = -p 
:::

Par la **deuxième loi de Newton**,

:::{math}
\begin{align*}
\frac{d}{dt} \int_{x_1(t)}^{x_2(t)} \rho\,u\,dx &= -p(x_2(t),t)+p(x_1(t),t) \\
&= -[p(x,t)]_{x_1(t)}^{x_2(t)} \\
\end{align*}
:::

:::{math}
:label: formulation intégrale conservation du moment
\boxed{\frac{d}{dt} \int_{x_1(t)}^{x_2(t)} \rho\,u\,dx=-\int_{x_1(t)}^{x_2(t)} \frac{\partial p(x,t)}{\partial x} dx} 
:::

Or, par {eq}`dérivée particulaire`, on sait que :
:::{math}
\frac{d}{dt} \int_{x_1(t)}^{x_2(t)} \rho\, u\, dx = \int_{x_1(t)}^{x_2(t)} \rho \frac{du}{dt}dx
:::
Donc, en utilisant aussi \eqref{formulation intégrale conservation du moment}, on obtient la version intégrale de la conservation du moment en lagrangien : 
:::{math}
\int_{x_1(t)}^{x_2(t)}\left(\rho \frac{du}{dt}+\frac{\partial p}{\partial x}\right)dx = 0 \, , \quad \text{pour tout volume de contrôle} \ I(t).
:::
c'est-à-dire : 

:::{math}
\boxed{\rho \frac{du}{dt}+\frac{\partial p}{\partial x} = 0 \quad \textbf{conservation du moment (formalisme lagrangien).}}
:::

Ce qui correspond à la version locale de la conservation du moment en lagrangien.

Pour le formalisme eulérien, on démarre de {eq}`formule de Reynolds` la formule de Reynolds et ensuite on utilise l'équation {eq}`formulation intégrale conservation du moment` :

:::{math}
\frac{d}{dt} \int_{x_1(t)}^{x_2(t)} \rho\, u\, dx = \int_{x_1(t)}^{x_2(t)}\left(\ \frac{\partial (\rho\,u)}{\partial t}+\frac{\partial((\rho\, u)\,u)}{\partial x}\right)dx
:::
D'où avec {eq}`formulation intégrale conservation du moment` : 

:::{math}
\int_{x_1(t)}^{x_2(t)}\left(\frac{\partial (\rho\,u)}{\partial t}+\frac{\partial(\rho\,u^2+\,p)}{\partial x}\right)dx = 0\, , \quad \text{pour tout volume de contrôle} \ I(t).
:::
Ceci est la version intégrale en eulérien.
On déduit la version locale de la conservation du moment en eulérien : 

:::{math}
\boxed{ \frac{\partial (\rho\,u)}{\partial t}+\frac{\partial(\rho\,u^2+\,p)}{\partial x} = 0  \quad \textbf{conservation du moment (formalisme eulérien).} }
:::

## Conservation de l'énergie totale

L'énergie totale est $E$ la somme de l'énergie cinétique et de l'énergie interne : 
:::{math}
E=\rho \epsilon + \frac{1}{2} \rho u^2=\rho e
:::
où $\epsilon$ correspond à l'énergie interne spécifique et $e=\epsilon + \frac{1}{2} u^2$ l'énergie totale spécifique. 

Par le $1^{er}$ *principe de la thermodynamique*, l'énergie totale se conserve : la variation de l'énergie totale $E$ d'un système thermodynamique fermé (aucun échange de matière mais échange d'énergie avec le milieu extérieur) est égale à la quantité d'énergie échangée avec le milieu extérieur, par transfert thermique (chaleur) et transfert mécanique (travail, proportionnel à la force et au déplacement).

Or, ici on néglige les flux de chaleur appliqués. Ainsi, la variation de l'énergie totale est entièrement déterminée par le travail induit par les forces de pression : 

:::{math}
\begin{align*}
\frac{d}{dt} \int_{x_1(t)}^{x_2(t)} \rho\, e\, dx &= -p(x_2(t),t)u(x_2(t),t) + p(x_1(t),t)u(x_1(t),t)  
\end{align*} 
:::

:::{math}
:label: formulation intégrale conservation de l'énergie totale
 \boxed{\frac{d}{dt} \int_{x_1(t)}^{x_2(t)} \rho\, e\, dx = -\int_{x_1(t)}^{x_2(t)} \frac{\partial (p\,u)}{\partial x} dx } 
:::

:::{math}
\Rightarrow  \int_{x_1(t)}^{x_2(t)} \rho\frac{de}{dt} dx + \int_{x_1(t)}^{x_2(t)} \frac{\partial (p\,u)}{\partial x} dx = 0
:::
c'est-à-dire : 

:::{math}
\int_{x_1(t)}^{x_2(t)} \left(\rho \frac{de}{dt} + \frac{\partial (p\,u)}{\partial x} \right) dx = 0 \, , \quad \text{pour tout volume de contrôle} \ I(t).
:::
La version intégrale de la conservation de l'énergie totale en lagrangien.
On a donc la version locale : 


:::{math}
\boxed{\rho \frac{de}{dt} + \frac{\partial (p\,u)}{\partial x} = 0 \quad \textbf{conservation de l'énergie totale (formalisme lagrangien).} }
:::


Puis on déduit le formalisme eulérien en utilisant la formule de Reynolds {eq}`formule de Reynolds` :

:::{math}
\frac{d}{dt} \int_{x_1(t)}^{x_2(t)} \rho\, e\, dx = \int_{x_1(t)}^{x_2(t)}\left(\frac{\partial (\rho\,e)}{\partial t}+\frac{\partial(\rho\,e\,u)}{\partial x}\right)dx
:::
Et par {eq}`formulation intégrale conservation de l'énergie totale` on a : 
:::{math}
\int_{x_1(t)}^{x_2(t)}\left(\frac{\partial (\rho\,e)}{\partial t}+\frac{\partial(\rho\,e\,u)}{\partial x} + \frac{\partial(p\,u)}{\partial x}\right)dx = 0 \, , \quad \text{pour tout volume de contrôle} \ I(t).
:::
La version intégrale de la conservation de l'énergie totale en eulérien.
Finalement, on obtient la version locale :

:::{math}
\boxed{\frac{\partial (\rho\,e)}{\partial t}+\frac{\partial((\rho\,e\,+p)u)}{\partial x} = 0 \quad \textbf{conservation de l'énergie totale (formalisme eulérien).} }
:::


Nous avons obtenu les systèmes d'équations suivants : 

**Équations en coordonnée eulérienne :**

:::{math}
\left\{
\begin{array}{lll}
\displaystyle \frac{\partial \rho}{\partial t} + \frac{\partial (\rho u)}{\partial x} = 0 \, , \\
\displaystyle \frac{\partial (\rho u )}{\partial t} + \frac{\partial (\rho u^2 + p)}{\partial x} = 0 \, , \\ 
\displaystyle \frac{\partial (\rho e )}{\partial t} + \frac{\partial ((\rho e + p)u)}{\partial x} = 0.  
\end{array}
\right.
:::



**Équations en coordonnée lagrangienne :**


:::{math}
\left\{
\begin{array}{lll}
\rho J = \rho_0 \, , \\
\displaystyle \rho \frac{du}{dt} + \frac{\partial p}{\partial x} = 0 \, , \\
\displaystyle \rho \frac{de}{dt} + \frac{\partial(pu)}{\partial x} = 0 \, ,
\end{array}
\right.
::: 


Dans la suite, nous allons voir que les équations d'Euler, en coordonnées eulériennes, ainsi définies admettent des solutions discontinues, telles que des ondes de choc et des discontinuités de contact. En général, la forme différentielle (version locale) des lois de conservation n'est pas valide car repose sur une hypothèse de régularité. Tandis que la version intégrale  l'est toujours. 

Finalement, nous avons établi les équations d'Euler 1D, dépendantes du temps en coordonnées eulériennes et lagrangiennes respectivement. Elles expriment la conservation de la masse, du moment et de l'énergie totale d'un gaz parfait compressible. La prochaine étape repose sur l'étude du problème de Riemann associé au système des équations d'Euler en coordonnées eulérienne. 