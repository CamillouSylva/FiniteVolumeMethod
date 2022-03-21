import numpy as np
import fluxnum
import matplotlib.pyplot as plt
from numerical_fluxes import numerical_flux


class RiemannSolver:

    # _prim_var = ["r", "u", "p"] #variables primitives

    # variables conservatives: r: rho, m=rho*u, E=rho*e
    # variables primitives: r: densite, u: vitesse,, p: pression

    def __init__(self, gamma: float = 1.4,
                 t0: float = 0.,
                 T: float = 0.2,  # tps final
                 x_0: float = 0.3,  # pt de discontinuite
                 L: float = 1.,  # longueur du domaine
                 Nx: int = 100,  # nb de mailles
                 CFL: float = 0.9,  # coeff nb de Courant,
                 W_L: np.ndarray = None,
                 W_R: np.ndarray = None):
        """

        :param gamma: Indice (ou coefficient) adiabatique
        :param t0: Temps initial
        :param T: Temps final
        :param x_0: Point de discontinuité
        :param L: Longueur du domaine
        :param Nx: Nombre de mailles
        :param CFL: Coefficient nombre de Courant
        :param W_L: Vecteur contenant les variables primitives (r_l, u_l, p_l) de
        l'état initial constant à gauche
        :param W_R: Vecteur contenant les variables primitives (r_r, u_r, p_r) de
        l'état initial constant à droite
        """
        self.gamma = gamma
        self.t0 = t0
        self.T = T
        self.x_0 = x_0
        self.Nx = Nx
        self.CFL = CFL
        if W_L is None:
            W_L = np.zeros(3)
        if W_R is None:
            W_R = np.zeros(3)
        self.W_L = W_L
        self.W_R = W_R
        self.dx = L / Nx
        # self.reset()
        self.initialization()
        self.initial_states()
        self.initial_conditions()

    # def __getattr__(self, attr):
    #     sv = self._prim_var
    #     try:
    #         return self.W[:, sv.index(attr)]
    #     except:
    #         raise AttributeError(attr) 

    def initialization(self):
        """
        :return: initialisation
        """
        self.x = np.zeros((1, self.Nx + 1)).reshape(self.Nx + 1, 1)  # noeuds
        self.xm = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # points milieu
        self.r = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # densite
        self.m = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # moment
        self.E = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # energie totale
        self.u = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # vitesse
        self.p = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # pression
        self.e = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # energie interne
        self.a = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # vecteur avec toutes les vitesses du son

    def moment(self, W):
        # return W[0] * W[1]

        return W[0] * W[1]

    def total_energy(self, W):
        # return W[0] * (W[2] / (self.gamma - 1) / W[0] + 0.5 * W[1] ** 2)

        return W[0] * (W[2] / (self.gamma - 1) / W[0] + 0.5 * W[1] ** 2)

    # return W[2] / (self.gamma - 1) + 0.5 * W[0] * W[1] ** 2

    def intern_energy(self, W):
        # return W[2] / (W[0] * (self.gamma - 1.))

        return W[2] / (W[0] * (self.gamma - 1.))

    def initial_states(self):
        """
            Etats initiaux a gauche(l) et  a droite(r)
            r = densite, u = vitesse, e = energie interne
        :return: define the initial states
        """
        # self.ml = self.rl * self.ul  # moment a gauche
        # self.El = self.pl / (self.gamma - 1.) + 0.5 * self.rl * (self.ul ** 2)
        self.e_L = self.intern_energy(self.W_L)
        # self.mr = self.rr * self.ur  # moment a droite
        # self.Er = self.pr / (self.gamma - 1.) + 0.5 * self.rr * (self.ur ** 2)
        self.e_R = self.intern_energy(self.W_R)
        self.E_L = self.total_energy(self.W_L)
        self.E_R = self.total_energy(self.W_R)
        self.m_L = self.moment(self.W_L)
        self.m_R = self.moment(self.W_R)

    def initial_conditions(self):
        """
        :return: define initial conditions
        """
        self.x[0] = 0
        for i in range(self.Nx):
            self.x[i + 1] = (i + 1) * self.dx
            self.xm[i] = (self.x[i] + self.x[i + 1]) / 2
            if self.xm[i] < self.x_0:  # % L / 2 = x_0
                self.r[i] = self.W_L[0]
                self.m[i] = self.m_L
                self.u[i] = self.W_L[1]
                self.E[i] = self.E_L
                self.p[i] = self.W_L[2]
                self.e[i] = self.e_L
            else:
                self.r[i] = self.W_R[0]
                self.m[i] = self.m_R
                self.u[i] = self.W_R[1]
                self.E[i] = self.E_R
                self.p[i] = self.W_R[2]
                self.e[i] = self.e_R
            self.a[i] = np.sqrt(self.gamma * self.p[i] / self.r[i])
            # print("r ==", self.r)

    # def reset(self):
    #     self.W = np.array([self.W_L])
    #     self.t = np.array([self.t0])
    #     self.U_L = np.array([self.W_L[0],
    #                          self.m_L,
    #                          self.E_L])
    #     self.U_R = np.array([self.W_L[0],
    #                          self.m_R,
    #                          self.E_R])        
    #     self.F_L = np.array([self.m_L,
    #                          self.m_L**2/self.W_L[0]+ self.W_L[2],
    #                          (self.E_L+self.W_L[2])*self.m_L/self.W_L[0]])
    #     self.F_R = np.array([self.m_R,
    #                          self.m_R**2/self.W_R[0]+ self.W_R[2],
    #                          (self.E_R+self.W_R[2])*self.m_R/self.W_R[0]])

    def solve(self, solver_type: str = "Rusanov"):
        """_summary_

        Args:
            solver_type (str, optional): _description_. Defaults to "Rusanov".
        """

        F = np.zeros((3, self.Nx + 1))
        data = {}
        Fi = np.zeros((3, self.Nx + 1))
        # Fr = np.zeros((1, self.Nx+1))
        # Fm = np.zeros((1, self.Nx+1))
        # FE = np.zeros((1, self.Nx+1))
        Fr = np.zeros(self.Nx + 1)
        Fm = np.zeros(self.Nx + 1)
        FE = np.zeros(self.Nx + 1)
        t = 0.
        while t < self.T:
            Smax = 0.
            for i in range(self.Nx):
                Smax = max(Smax, abs(self.u[i]) + self.a[i])
            dt = min(self.T - t, self.CFL * (self.dx / Smax))  # pour ne pas depasser T

            for i in range(self.Nx + 1):
                if i == 0:
                    self.W_L[0] = self.r[i]
                    self.m_L = self.m[i]
                    self.E_L = self.E[i]
                else:
                    self.W_L[0] = self.r[i - 1]
                    self.m_L = self.m[i - 1]
                    self.E_L = self.E[i - 1]
                if i == self.Nx:
                    self.W_R[0] = self.r[i - 1]
                    self.m_R = self.m[i - 1]
                    self.E_R = self.E[i - 1]
                else:
                    self.W_R[0] = self.r[i]
                    self.m_R = self.m[i]
                    self.E_R = self.E[i]
                print("self.WL=", self.W_L[0])
                F[0, i] = numerical_flux(solver_type, self.W_L[0], self.m_L, self.E_L, self.W_R[0], self.m_R,
                                         self.E_R)[0]
                F[1, i] = numerical_flux(solver_type, self.W_L[0], self.m_L, self.E_L, self.W_R[0], self.m_R,
                                         self.E_R)[1]
                F[2, i] = numerical_flux(solver_type, self.W_L[0], self.m_L, self.E_L, self.W_R[0], self.m_R,
                                         self.E_R)[2]
                # data = fluxnum.fluxnum(solver_type, self.W_L[0], self.m_L, self.E_L, self.W_R[0], self.m_R,
                #                        self.E_R)
                # F[0, i] = \
                #     fluxnum.fluxnum(solver_type, self.W_L[0], self.m_L, self.E_L, self.W_R[0], self.m_R,
                #                                     self.E_R)["Fr"][0]

                # F[1, i] = \
                #     fluxnum.fluxnum(solver_type, self.W_L[0], self.m_L, self.E_L, self.W_R[0], self.m_R,
                #                                     self.E_R)["Fi"]

                # F[2, i] = \
                #     fluxnum.fluxnum(solver_type, self.W_L[0], self.m_L, self.E_L, self.W_R[0], self.m_R,
                #                                     self.E_R)[
                # 2]
                # Fr[i] = F[0, i]
                # Fm[i] = Fi[1, i]
                # FE[i] = Fi[2, i]
                # Fi[0,i] = F[0, i]
                # Fi[2,i] = F[1, i]
                # Fi[2,i] = F[2, i]
                # Fi[0, i] = data["Fi"][0]
                # Fi[1, i] = data["Fi"][1]
                # Fi[2, i] = data["Fi"][2]
                Fr[i] = F[0, i]
                Fm[i] = F[1, i]
                FE[i] = F[2, i]
            #    print("Fi[2, i] = ", data["Fi"][2])
            #  print(Fi)
            for i in range(self.Nx):
                self.r[i] = self.r[i] - (dt / self.dx) * (Fr[i + 1] - Fr[i])  # densite
                self.m[i] = self.m[i] - (dt / self.dx) * (Fm[i + 1] - Fm[i])  # moment
                self.E[i] = self.E[i] - (dt / self.dx) * (FE[i + 1] - FE[i])

                # self.r[i] = self.r[i] - (dt / self.dx) * (Fi[0, i + 1] - Fi[0, i])
                # self.m[i] = self.m[i] - (dt / self.dx) * (Fi[1, i + 1] - Fi[1, i])  # moment
                # self.E[i] = self.E[i] - (dt / self.dx) * (Fi[2, i + 1] - Fi[2, i])
                self.u[i] = self.m[i] / self.r[i]
                self.p[i] = (self.gamma - 1.) * (self.E[i] - 0.5 * (self.m[i] ** 2) / self.r[i])  # pression
                #  On suppose que que le gaz obeit a la loi d'etat des gaz parfaits ==> p =(gamma -1)*rho*e
                self.e[i] = self.p[i] / (self.r[i] * (self.gamma - 1.))  # energie interne
                self.a[i] = np.sqrt(abs(self.gamma * self.p[i]) / self.r[i])
            t += dt

        print("Res = ", self.r)  # print("Résultats = ", self.r, self.m, self.E, self.u, self.p, self.e, self.a)
        print("xm = ", self.xm)
        print("p = ", self.p)
        print("len(xm) = ", len(self.xm), "\nlen(p)", len(self.p))
        print(self.W_L[0], self.W_L[1], self.W_L[2])
        print(self.W_R[0], self.W_R[1], self.W_R[2])

        return self.r, self.m, self.E, self.u, self.p, self.e, self.a

    def plot(self, ):
        self.solve()

        plt.plot(self.xm, self.p, color="black", linestyle="--")
        plt.xlabel("position xm")
        plt.ylabel("pression p")
        plt.show()

        plt.plot(self.xm, self.u, color="black", linestyle="--")
        plt.xlabel("position xm")
        plt.ylabel("vitesse u")
        plt.show()

        plt.plot(self.xm, self.r, color="black", linestyle="--")
        plt.xlabel("position xm")
        plt.ylabel("densité r")
        plt.show()

        plt.plot(self.xm, self.e, color="black", linestyle="--")
        plt.xlabel("position xm")
        plt.ylabel("énergie interne e")
        plt.show()


class SolverRusanov(RiemannSolver):
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def solve(self):
        return super().solve(solver_type="Rusanov")

    # @property    #getter
    # def S_L(self):
    #     return self._S_L

    # @S_L.setter
    # def S_L(self, new_S_L):
    #     self._S_L = new_S_L

    # def S_R(self):
    #     self.S_R = np.abs(self.W_R.r)

    # def Sp(self):
    #     self.Sp = np.max(self.S_L, self.S_R)

    # def RusaF(self):       
    #     return 0.5*(self.F_L+self.F_R) - 0.5*self.Sp*(self.U_R-self.U_L)


class SolverHLL(RiemannSolver):
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def solve(self):
        return super().solve(solver_type="HLL")


class SolverHLLC(RiemannSolver):
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def solve(self):
        return super().solve(solver_type="HLLC")


if __name__ == '__main__':
    # o = SolverRusanov(T=0.2, x_0=0.3, Nx=100, W_L=np.array([[1.0], [0.], [1.0]]), W_R=np.array([[0.125], [0.], [0.1]]))
    o = SolverRusanov(T=0.2, x_0=0.3, Nx=100, W_L=np.array([1.0, 0., 1.0]), W_R=np.array([0.125, 0., 0.1]))

    o.solve()
    o.plot()
