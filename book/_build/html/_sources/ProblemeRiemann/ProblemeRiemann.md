# Problème de Riemann associé aux équations d'Euler en 1D

Dans cette section, on présente la méthode de résolution du problème de Riemann pour les équations d'Euler en 1D pour des gaz parfaits.

## Procédure de résolution du problème de Riemann associé au système d'Euler unidimensionnelles dépendantes du temps

On considère le système différentiel non linéaire de lois de conservation suivant :


$$
\left\{
\begin{array}{r c l}
\displaystyle \frac{\partial \rho}{\partial t} + \frac{\partial (\rho u)}{\partial x}  &=& 0 \, , \\[4mm]
\displaystyle \frac{\partial(\rho u)}{\partial t} + \frac{\partial(\rho u^2 + p)}{\partial x} &=& 0 \, , \\[4mm]
\displaystyle \frac{\partial\rho e}{\partial t} + \frac{\partial[(\rho e + p)u]}{\partial x} &=& 0 \, ,
\end{array} 
\right.
$$

qui s'écrit vectoriellement : 

$$
 \boxed{\frac{\partial \pmb{U}}{\partial t} + \frac{\partial \pmb{F(U)}}{\partial x} = \pmb{0}} 
$$

où $\pmb{U}$ est le vecteur des variables conservatives et $\pmb{F(U)}$ le vecteur flux, définis par : 

$$
\pmb{U}=\begin{pmatrix} \rho \\ \rho u \\ \rho e \end{pmatrix} = \begin{pmatrix} \rho \\ m \\ E \end{pmatrix}, \quad \pmb{F(U)}=\begin{pmatrix} \rho u \\ \rho u^2 + p \\ (\rho e + p)u \end{pmatrix} = \begin{pmatrix} m \\ \frac{m^2}{\rho} + p \\ (E + p)\frac{m}{\rho} \end{pmatrix}.
$$

On ajoute la condition initiale à deux états suivante :  

$$
\pmb{U}(x,0) = \pmb{U}^{(0)}(x) =
\left\{
\begin{array}{ll}
 \pmb{U_L} \quad \text{si} \quad x<0 \\
 \pmb{U_R} \quad \text{si} \quad x>0 
\end{array}
\right.
$$



