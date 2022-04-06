#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from W import Wr, Wl


class RiemannSolver:
    def __init__(self,
                 W_L: list,
                 W_R: list,
                 nx: int = 100,
                 x_0: float = 0.3,
                 T: float = 0.2,
                 L: float = 1.,
                 cfl: float = 0.9,
                 gamma: float = 1.4,
                 ):
        """
        :param W_L: Liste des variables primitives (r_l, u_l, p_l) de l'état initial à gauche
        :param W_R: Liste des variables primitives (r_r, u_r, p_r) de l'état initial à droite
        :param nx: Nombre de mailles
        :param x_0: Point de discontinuité
        :param T: Temps final
        :param L: Longueur du domaine
        :param cfl: Nombre de Courant (condition de Courant–Friedrichs–Lewy).
                    C'est une condition nécessaire pour qu'un schéma numérique produise
                    une solution cohérente lors de la résolution.
        :param gamma: Indice (ou coefficient) adiabatique
        """
        self._W_L = Wl(*W_L)
        self._W_R = Wr(*W_R)

        self.T = T
        self.x_0 = x_0
        self.L = L
        self.Nx = nx
        self.cfl = cfl
        self._dx = self.L / self.Nx  # pas d'espace
        self._gamma = gamma
        self.initialization()
        self.initial_states()
        self.initial_conditions()

    @property
    def dx(self):
        """
        return: Pas d'espace
        """
        return self._dx

    @dx.setter
    def dx(self, new_dx: float):
        self._dx = float(new_dx)

    @property
    def gamma(self):
        """
        return: Indice (ou coefficient) adiabatique
        """
        return self._gamma

    @gamma.setter
    def gamma(self, new_gamma: float):
        self._gamma = float(new_gamma)

    @property
    def W_L(self) -> Wl:
        """
        return: Vecteur des variables primitives (r=rho, u, p) de l'état initial à gauche
        """
        return self._W_L

    @W_L.setter
    def W_L(self, wl: list):
        """
        :param wl: liste [u=rho, r, p] des variables primitives à gauche
        :return: Mettre à jour le vecteur des variables primitives à gauche
        """
        if len(wl) == 3:
            self._W_L = Wl(*wl)

    @property
    def W_R(self) -> Wr:
        """
        return: Vecteur des variables primitives (r=rho, u, p) de l'état initial à droite
        """
        return self._W_R

    @W_R.setter
    def W_R(self, wr: list):
        """
        :param wr: liste [u=rho, r, p] des variables primitives à droite
        :return: Mettre à jour le vecteur des variables primitives à droite
        """
        if len(wr) == 3:
            self._W_R = Wr(*wr)

    @property
    def xm(self) -> np.ndarray:
        """
        return: Vecteur des points milieux
        """
        return self._xm

    @property
    def U(self):
        """
        return: Vecteur des variables conservatives
        """
        return self._U

    @property
    def F(self) -> np.ndarray:
        """
        return: Vecteur flux F(U) contenant le vecteur des variables conservatives U
        """
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
    @property
    def r(self) -> np.ndarray:
        """
        return: Vecteur contenant la variable conservative rho
                représentant la densité sur chaque maille (en espace).
        """
        return self._r

    @property
    def m(self) -> np.ndarray:
        """
        return: Vecteur contenant la variable conservative m
                représentant le moment sur chaque maille (en espace).
        """
        return self._m

    @property
    def E(self) -> np.ndarray:
        """
        return: Vecteur contenant la variable conservative E
                représentant l'énergie totale sur chaque maille (en espace).
        """
        return self._E

    def initialization(self):
        """
        :return: initialisation
        """
        self.x = np.zeros((1, self.Nx + 1)).reshape(self.Nx + 1, 1)  # noeuds
        # print(self.x)
        self._xm = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # points milieu
        self._U = np.zeros((3, self.Nx)).reshape(3, self.Nx)
        # r, m et E définis comme ci-dessous permet de mettre à jour le vecteur U lorsque les
        # valeurs r, m et E changent.
        self._r = self.U[0]  # r=rho ->
        self._m = self.U[1]  # m variable conservative représentant le moment
        self._E = self.U[2]  # E variable conservative représentant la densité
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
        :return: Définition des états à gauche et à droite
        """
        # self.ml = self.rl * self.ul  # moment a gauche
        self.ml = self.W_L.r * self.W_L.u  # moment a gauche

        # self.El = self.pl / (self.gamma - 1.) + 0.5 * self.rl * (self.ul ** 2)
        self.El = self.W_L.p / (self.gamma - 1.) + 0.5 * self.W_L.r * (self.W_L.u ** 2)

        # self.el = self.pl / (self.rl * (self.gamma - 1.))
        self.el = self.W_L.p / (self.W_L.r * (self.gamma - 1.))

        # self.mr = self.rr * self.ur  # moment a droite
        self.mr = self.W_R.r * self.W_R.u  # moment a droite

        # self.Er = self.pr / (self.gamma - 1.) + 0.5 * self.rr * (self.ur ** 2)
        self.Er = self.W_R.p / (self.gamma - 1.) + 0.5 * self.W_R.r * (self.W_R.r ** 2)

        # self.er = self.pr / (self.rr * (self.gamma - 1.))
        self.er = self.W_R.p / (self.W_R.r * (self.gamma - 1.))

        #        print(f"rl, ul, ml = {self.rl}, {self.ul}, {self.ml}\nrr, ur, mr = {self.rr}, {self.ur}, {self.mr} \n")
        print(
            f"rl, ul, pl = {self.W_L.r}, {self.W_L.u}, {self.W_L.p}\nrr, ur, mr = {self.W_R.r}, {self.W_R.u}, {self.mr} \n")

    def initial_conditions(self):
        """
        :return: define initial conditions
        """

        self.x[0] = 0
        for i in range(0, self.Nx):
            self.x[i + 1] = (i + 1) * self.dx
            self.xm[i] = (self.x[i] + self.x[i + 1]) / 2
            if self.xm[i] < self.x_0:  # % L / 2 = x_0
                self.r[i] = self.W_L.r  # self.rl
                # self.u[i] = self.ul
                self.u[i] = self.W_L.u
                # self.p[i] = self.pl
                self.p[i] = self.W_L.p

                self.m[i] = self.ml
                self.E[i] = self.El
                self.e[i] = self.el
            else:
                # self.r[i] = self.rr
                self.r[i] = self.W_R.r
                # self.u[i] = self.ur
                self.u[i] = self.W_R.u
                # self.p[i] = self.pr
                self.p[i] = self.W_R.p

                self.m[i] = self.mr
                self.E[i] = self.Er
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
                fr, fm, fE = self.compute_Fi(i, rl, ml, El, rr, mr, Er)
                self.F[0, i] = fr
                self.F[1, i] = fm
                self.F[2, i] = fE
            print(f"fr = {fr}")
                

            for i in range(0, self.Nx):
                # self.compute_Ui(i, dt)
                self.r[i] = self.r[i] - (dt / self.dx) * (self.F[0, i + 1] - self.F[0, i])  # densite
                self.m[i] = self.m[i] - (dt / self.dx) * (self.F[1, i + 1] - self.F[1, i])  # moment
                self.E[i] = self.E[i] - (dt / self.dx) * (self.F[2, i + 1] - self.F[2, i])
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


if __name__ == "__main__":
    RS = RiemannSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2)
    RS.ur = 99
    print(RS.ur)

    RS.solve()
    print(RS.ur)
    RS.plot()
