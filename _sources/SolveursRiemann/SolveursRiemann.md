# Les solveurs de Riemann approchés Rusanov, HLL et HLLC

On considère le problème avec conditions initiales et conditions aux bords transmissives suivant : 

$$
\left\{ 
\begin{array}{l l l}
\displaystyle \frac{\partial \bold{U}}{\partial t} + \frac{\partial \bold{F(U)}}{\partial x} = \bold{0} \, ,\\[4mm] 
\displaystyle \bold{U}(x,0) = \bold{U}^{(0)}(x) \quad \forall \ x \in [x_L;x_R] \, ,\\ 
\end{array} 
\right.
$$

où $\bold{U}$ le vecteur des variables conservatives et $\bold{U^{(0)}}$ défini comme dans \eqref{condition_init}.