# Les solveurs de Riemann approchés Rusanov, HLL et HLLC

On considère le problème avec conditions initiales et conditions aux bords transmissives suivant : 

$$
\left\{ 
\begin{array}{l l l}
\displaystyle \frac{\partial \pmb{U}}{\partial t} + \frac{\partial \pmb{F(U)}}{\partial x} = \pmb{0} \, ,\\[4mm] 
\displaystyle \pmb{U}(x,0) = \pmb{U}^{(0)}(x) \quad \forall \ x \in [x_L;x_R] \, ,\\ 
\end{array} 
\right.
$$

où $\pmb{U}$ le vecteur des variables conservatives et $\pmb{U^{(0)}}$ défini comme dans \eqref{condition_init}.