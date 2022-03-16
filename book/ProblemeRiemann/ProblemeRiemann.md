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
 \boxed{\frac{\partial \bold{U}}{\partial t} + \frac{\partial \bold{F(U)}}{\partial x} = \bold{0}} 
$$

où $\bold{U}$ est le vecteur des variables conservatives et $\bold{F(U)}$ le vecteur flux, définis par : 

$$
\bold{U}=\begin{pmatrix} \rho \\ \rho u \\ \rho e \end{pmatrix} = \begin{pmatrix} \rho \\ m \\ E \end{pmatrix}, \quad \bold{F(U)}=\begin{pmatrix} \rho u \\ \rho u^2 + p \\ (\rho e + p)u \end{pmatrix} = \begin{pmatrix} m \\ \frac{m^2}{\rho} + p \\ (E + p)\frac{m}{\rho} \end{pmatrix}.
$$

On ajoute la condition initiale à deux états suivante :  

$$
\bold{U}(x,0) = \bold{U}^{(0)}(x) =
\left\{
\begin{array}{ll}
 \bold{U_L} \quad \text{si} \quad x<0 \\
 \bold{U_R} \quad \text{si} \quad x>0 
\end{array}
\right.
$$



