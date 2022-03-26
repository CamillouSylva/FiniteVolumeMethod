import numpy as np
from cmath import sqrt as complex_sqrt
import matplotlib.pyplot as plt


class W:
    def __init__(self, r, u, p):
        self._r = r
        self._u = u
        self._p = p

    def __repr__(self):
        return f"[{self.r}, {self.u}, {self.p}]"

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, new_r):
        self._r = new_r

    @property
    def u(self):
        return self._u

    @u.setter
    def u(self, new_u):
        self._u = new_u

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, new_p):
        self._p = new_p


class W_r(W):
    def __init__(self, rr, ur, pr):
        super().__init__(r=rr, u=ur, p=pr)
        self._rr = rr
        #  self.rr = super().r
        self.ur = super().u
        self.pr = super().p

    @property
    def rr(self):
        return self._rr

    @rr.setter
    def rr(self, new_rr):
        self._rr = new_rr

    def __repr__(self):
        return f" W_r = [{self.rr}, {self.ur}, {self.pr}]"


class W_l(W):
    def __init__(self, rl, ul, pl):
        super().__init__(r=rl, u=ul, p=pl)
        self._rl = rl
        #  self.rl = super().r
        self.ul = super().u
        self.pl = super().p

    @property
    def rl(self):
        return self._rl

    @rl.setter
    def rl(self, new_rl):
        self._rl = new_rl

    def __repr__(self):
        return f" W_l = [{self.rl}, {self.ul}, {self.pl}]"


class RiemannSolver:
    def __init__(self,
                 W_L: list,  # W_l,  # np.ndarray = None,
                 W_R: list,  #: W_r,  # np.ndarray = None
                 nx: int = 100,  # nb de mailles
                 x_0: float = 0.3,  # pt de discontinuite
                 #  t0: float = 0.,
                 T: float = 0.2,  # tps final
                 L: float = 1.,  # longueur du domaine
                 cfl: float = 0.9,  # coeff nb de Courant,
                 gamma: float = 1.4,
                 ):
        self.W_L = W_l(*W_L)
        self.W_R = W_r(*W_R)

        self.gamma = gamma
        self.T = T
        self.x_0 = x_0
        self.L = L
        self.Nx = nx
        self.cfl = cfl
        self.dx = self.L / self.Nx  # pas d'espace
        self.initialization()
        self.initial_states()
        self.initial_conditions()

    @property
    def rl(self):
        return self.W_L.rl

    @rl.setter
    def rl(self, new_rl):
        self.W_L.rl = new_rl

    @property
    def ul(self):
        return self.W_L.ul

    @ul.setter
    def ul(self, new_ul):
        self.W_L.ul = new_ul

    @property
    def pl(self):
        return self.W_L.pl

    @pl.setter
    def pl(self, new_pl):
        self.W_L.pl = new_pl

    ######

    @property
    def rr(self):
        # print(self.W_R.rr)
        return self.W_R.rr

    @rr.setter
    def rr(self, new_rr):
        self.W_R.rr = new_rr

    @property
    def ur(self):
        return self.W_R.ur

    @ur.setter
    def ur(self, new_ur):
        self.W_R.ur = new_ur

    @property
    def pr(self):
        return self.W_R.pr

    @pr.setter
    def pr(self, new_pr):
        self.W_R.pr = new_pr

    @property
    def U(self):
        return self._U
        # return np.array([self.r,self.m, self.E]).reshape(3, self.Nx)

    @property
    def F(self):
        return self._F

    # @property
    # def Fr(self):
    #     return self.fr
    #
    # @Fr.setter
    # def Fr(self, fr):
    #     self.fr = fr

    # @U.setter
    # def U(self, new_u):
    #     self._U = new_u

    def initialization(self):
        """
        :return: initialisation
        """
        self.x = np.zeros((1, self.Nx + 1)).reshape(self.Nx + 1, 1)  # noeuds
        # print(self.x)
        self.xm = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # points milieu
        self._U = np.zeros((3, self.Nx)).reshape(3, self.Nx)
        # r, m et E définis comme ci-dessous permet de mettre à jour le vecteur U lorsque les
        # valeurs r, m et E changent.
        self.r = self.U[0]
        self.m = self.U[1]
        self.E = self.U[2]
        # self.r = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # densite
        #  self.m = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # moment
        #  self.E = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # energie totale

        #   print("U = ", self.U[0] + np.ones(self.Nx))
        self.u = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # vitesse
        self.p = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # pression
        self.e = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # energie interne
        self.a = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # vecteur avec toutes les vitesses du son

        self._F = np.zeros((3, self.Nx + 1)).reshape(3, self.Nx + 1)
        self.fr = self._F[0]
        self.fm = self._F[1]
        self.fE = self._F[2]

    def initial_states(self):
        """
            Etats initiaux a gauche(l) et  a droite(r)
            r = densite, u = vitesse, e = energie interne
        :return: define the initial states
        """
        self.ml = self.rl * self.ul  # moment a gauche
        self.El = self.pl / (self.gamma - 1.) + 0.5 * self.rl * (self.ul ** 2)
        self.el = self.pl / (self.rl * (self.gamma - 1.))

        self.mr = self.rr * self.ur  # moment a droite
        self.Er = self.pr / (self.gamma - 1.) + 0.5 * self.rr * (self.ur ** 2)
        self.er = self.pr / (self.rr * (self.gamma - 1.))
        print(f"rl, ul, ml = {self.rl}, {self.ul}, {self.ml}\nrr, ur, mr = {self.rr}, {self.ur}, {self.mr} \n")

    def initial_conditions(self):
        """
        :return: define initial conditions
        """

        self.x[0] = 0
        for i in range(0, self.Nx):
            self.x[i + 1] = (i + 1) * self.dx
            self.xm[i] = (self.x[i] + self.x[i + 1]) / 2
            if self.xm[i] < self.x_0:  # % L / 2 = x_0
                self.r[i] = self.rl
                self.m[i] = self.ml
                self.u[i] = self.ul
                self.E[i] = self.El
                self.p[i] = self.pl
                self.e[i] = self.el
            else:
                self.r[i] = self.rr
                self.m[i] = self.mr
                self.u[i] = self.ur
                self.E[i] = self.Er
                self.p[i] = self.pr
                self.e[i] = self.er
            self.a[i] = np.sqrt(self.gamma * self.p[i] / self.r[i])

    def compute_Fi(self, i, rl, ml, El, rr, mr, Er):
        print("Méthode à implémenter pour les sous classes")

    def compute_Ui(self, j, dt):
        for i in range(3):
            # self.U[i][j] = self.U[i][j] - (dt / self.dx) * (self.F[i][j + 1] - self.F[i][j])
            self.U[i][j] = self.U[i][j] + (dt / self.dx) * (self.F[i][j] - self.F[i][j + 1])

    def solve(self):
        t = 0
        while t < self.T:
            Smax = 0
            for i in range(0, self.Nx):
                Smax = max(Smax, abs(self.u[i]) + self.a[i])
            dt = min(self.T - t, self.cfl * (self.dx / Smax))
            for i in range(0, self.Nx + 1):
                if i == 0:
                    rl = self.r[i]
                    ml = self.m[i]
                    El = self.E[i]
                else:
                    rl = self.r[i - 1]
                    ml = self.m[i - 1]
                    El = self.E[i - 1]
                if i == self.Nx:
                    rr = self.r[i - 1]
                    mr = self.m[i - 1]
                    Er = self.E[i - 1]
                else:
                    rr = self.r[i]
                    mr = self.m[i]
                    Er = self.E[i]
                # print("rl=", rl)
                self.compute_Fi(i, rl, ml, El, rr, mr, Er)

            for i in range(0, self.Nx):
                self.compute_Ui(i, dt)

                # self.r[i] = self.r[i] - (dt / self.dx) * (Fr[i + 1] - Fr[i])  # densite
                # self.m[i] = self.m[i] - (dt / self.dx) * (Fm[i + 1] - Fm[i])  # moment
                # self.E[i] = self.E[i] - (dt / self.dx) * (FE[i + 1] - FE[i])
                self.u[i] = self.m[i] / self.r[i]
                self.p[i] = (self.gamma - 1.) * (self.E[i] - 0.5 * (self.m[i] ** 2) / self.r[i])  # pression
                #  On suppose que que le gaz obeit a la loi d'etat des gaz parfaits ==> p =(gamma -1)*rho*e
                self.e[i] = self.p[i] / (self.r[i] * (self.gamma - 1.))  # energie interne
                self.a[i] = np.sqrt(abs(self.gamma * self.p[i]) / self.r[i])
            t += dt

        # print("Res = ", self.r)  # self.r, self.m, self.E, self.u, self.p, self.e, self.a)
        # print("xm = ", self.xm)
        # print("p = ", self.p)
        # print("len(xm) = ", len(self.xm), "\nlen(p)", len(self.p))
        # #  self.U = np.array([self.r, self.m, self.E]).reshape(3, self.Nx)
        # print(self.U)
        # print(self.U[0])
        return self.r, self.m, self.E, self.u, self.p, self.e, self.a

    def plot(self):
        """
        :param solver_type: type de solveur (Rusanov, HLL, HLLC)
        :param test: numero de test (1, 2, 3, 4)
        :return: 

        """""
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


class RusanovSolver(RiemannSolver):
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def compute_Fi(self, i, rl, ml, El, rr, mr, Er):
        ul = ml / rl
        pl = (self.gamma - 1) * (El - 0.5 * (ml ** 2) / rl)
        al = complex_sqrt((self.gamma * pl / rl))

        pr = (self.gamma - 1) * (Er - 0.5 * (mr ** 2) / rr)
        ur = mr / rr
        ar = complex_sqrt(self.gamma * pr / rr)

        Fi = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
        Fl = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
        Fl[0] = ml
        Fl[1] = (ml ** 2) / rl + pl
        Fl[2] = (El + pl) * (ml / rl)

        Fr = np.zeros((3, 1))  # .reshape(3, 1)

        Fr[0] = mr
        Fr[1] = (mr ** 2) / rr + pr
        Fr[2] = (Er + pr) * (mr / rr)
        # if solver_type == "Rusanov":  # flux numerique Rusanov ; Sl et Sr sont des vitesses d’onde
        Sl = (abs(ul) + al).real  # % vitesse minimale

        Sr = (abs(ur) + ar).real  # vitesse maximale
        #   print(Sr, Sl)

        Sp = max(Sl, Sr)

        Fi[0] = 0.5 * (Fl[0] + Fr[0] - Sp * (rr - rl))
        Fi[1] = 0.5 * (Fl[1] + Fr[1] - Sp * (mr - ml))
        Fi[2] = 0.5 * (Fl[2] + Fr[2] - Sp * (Er - El))

        # self.fr[i] = Fi[0]
        # self.fm[i] = Fi[1]
        # self.fE[i] = Fi[2]

        self.F[0, i] = Fi[0]
        # self.fr[i] =  Fi[0]
        self.F[1, i] = Fi[1]
        self.F[2, i] = Fi[2]


class HLLSolver(RiemannSolver):
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def compute_Fi(self, i, rl, ml, El, rr, mr, Er):
        Ur = np.array([rr, mr, Er]).reshape(3, 1)
        Ul = np.array([rl, ml, El]).reshape(3, 1)

        ul = ml / rl
        pl = (self.gamma - 1) * (El - 0.5 * (ml ** 2) / rl)
        al = complex_sqrt((self.gamma * pl / rl))

        pr = (self.gamma - 1) * (Er - 0.5 * (mr ** 2) / rr)
        ur = mr / rr
        ar = complex_sqrt(self.gamma * pr / rr)

        Fi = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
        Fl = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
        Fl[0] = ml
        Fl[1] = (ml ** 2) / rl + pl
        Fl[2] = (El + pl) * (ml / rl)

        Fr = np.zeros((3, 1))  # .reshape(3, 1)

        Fr[0] = mr
        Fr[1] = (mr ** 2) / rr + pr
        Fr[2] = (Er + pr) * (mr / rr)

        Sl = (ul - al).real  # vitesse minimale

        Sr = (ur + ar).real  # vitesse maximale
        #  print(Sl, Sr)
        if Sl >= 0:
            Fi[0] = Fl[0]
            Fi[1] = Fl[1]
            Fi[2] = Fl[2]

        elif Sl < 0 < Sr:  # Sl < 0 and 0 < Sr:
            Fi[0] = (Sr * Fl[0] - Sl * Fr[0] + Sl * Sr * (Ur[0] - Ul[0])) / (Sr - Sl)
            Fi[1] = (Sr * Fl[1] - Sl * Fr[1] + Sl * Sr * (Ur[1] - Ul[1])) / (Sr - Sl)
            Fi[2] = (Sr * Fl[2] - Sl * Fr[2] + Sl * Sr * (Ur[2] - Ul[2])) / (Sr - Sl)

        else:  # % (0 >= Sr)
            Fi[0] = Fr[0]
            Fi[1] = Fr[1]
            Fi[2] = Fr[2]
        self.F[0, i] = Fi[0]
        # self.fr[i] =  Fi[0]
        self.F[1, i] = Fi[1]
        self.F[2, i] = Fi[2]


class HLLCSolver(RiemannSolver):
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def compute_Fi(self, i, rl, ml, El, rr, mr, Er):
        Ur = np.array([rr, mr, Er]).reshape(3, 1)
        Ul = np.array([rl, ml, El]).reshape(3, 1)

        ul = ml / rl
        pl = (self.gamma - 1) * (El - 0.5 * (ml ** 2) / rl)
        al = complex_sqrt((self.gamma * pl / rl))

        pr = (self.gamma - 1) * (Er - 0.5 * (mr ** 2) / rr)
        ur = mr / rr
        ar = complex_sqrt(self.gamma * pr / rr)

        Fi = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
        Fl = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
        Fl[0] = ml
        Fl[1] = (ml ** 2) / rl + pl
        Fl[2] = (El + pl) * (ml / rl)

        Fr = np.zeros((3, 1))  # .reshape(3, 1)

        Fr[0] = mr
        Fr[1] = (mr ** 2) / rr + pr
        Fr[2] = (Er + pr) * (mr / rr)

        # Sl = (ul - al).real  # vitesse minimale

        # Sr = (ur + ar).real  # vitesse maximale

        Sl = min((ul - al).real, (ur - ar).real)
        Sr = max((ul + al).real, (ur + ar).real)
        #  print("pr",rl * (Sl - ul))
        Se = (pr - pl + rl * ul * (Sl - ul) - rr * ur * (Sr - ur)) / (rl * (Sl - ul) - rr * (Sr - ur))

        # print((Sl - Se))
        Uel = (rl * ((Sl - ul) / (Sl - Se)) * np.array([1., Se, El / rl + (Se - ul) * (Se + pl / (rl * (Sl - ul)))],
                                                       dtype=float))
        # print("Uel", Uel)
        Uer = rr * ((Sr - ur) / (Sr - Se)) * np.array([1., Se, Er / rr + (Se - ur) * (Se + pr / (rr * (Sr - ur)))],
                                                      dtype=float)

        if Sl >= 0:
            Fi[0] = Fl[0]
            Fi[1] = Fl[1]
            Fi[2] = Fl[2]

        elif Sl <= 0 <= Se:  # Se -> S*
            Fi[0] = Fl[0] + Sl * (Uel[0] - Ul[0])
            Fi[1] = Fl[1] + Sl * (Uel[1] - Ul[1])
            Fi[2] = Fl[2] + Sl * (Uel[2] - Ul[2])

        elif Se <= 0 <= Sr:
            Fi[0] = Fr[0] + Sr * (Uer[0] - Ur[0])
            Fi[1] = Fr[1] + Sr * (Uer[1] - Ur[1])
            Fi[2] = Fr[2] + Sr * (Uer[2] - Ur[2])

        else:  # (Sr <= 0)
            Fi[0] = Fr[0]
            Fi[1] = Fr[1]
            Fi[2] = Fr[2]

        self.F[0, i] = Fi[0]
        self.F[1, i] = Fi[1]
        self.F[2, i] = Fi[2]


if __name__ == "__main__":
    # RS = RiemannSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2)
    #
    # RS.solve()
    # RS.plot()
    RuS = RusanovSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2, L=1)
    RuS.solve()
    RuS.plot()

    # hll = HLLSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2)
    # hll.solve()
    # hll.plot()
    # hllc = HLLCSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2, L=1)
    # hllc.solve()
    # hllc.plot()
