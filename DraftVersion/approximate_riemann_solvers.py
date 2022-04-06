import numpy as np
from matplotlib import pyplot as plt
import numerical_fluxes


class Euler1D:
    def __init__(self, Nx: int):
        """
        :param Nx: nombre de mailles
        """
        self.Nx = Nx
        self.list_type_solver = ["Rusanov", "HLL", "HLLC"]
        self.list_test = ["1", "2", "3", "4"]
        self.type_solver = None
        self.test = None
        self.gamma = 1.4

        # self.Nx = None  # Nx

        # self.rl = 1.0  # densite
        # self.ul = -2.0
        # self.pl = 0.4
        #
        # self.rr = 1.0
        # self.ur = 2.0  # vitesse
        # self.pr = 0.4  # pression

        self.T = 0.2  # 0.15  # temps final(pour Sod modifié)
        # self.x_0 = 0.5  # point de discontinuité

        self.L = 1.  # longueur du domaine
        self.dx = self.L / self.Nx  # pas d'espace
        self.gamma = 1.4
        # limitation du pas de temps par la condition CFL
        self.cfl = 0.9

    def choose_test(self, test_num: int):
        """
        :param test_num: numero de test
        :return:
        """
        if test_num == 1:  # cas test 1
            self.rl = 1.0  # densite
            self.ul = 0.0  # vitesse
            self.pl = 1.0  # pression

            self.rr = 0.125
            self.ur = 0.0
            self.pr = 0.1

            self.T = 0.2  # temps final(pour Sod modifié)
            self.x_0 = 0.3  # point de discontinuité

        if test_num == 2:  # cas test 2
            self.rl = 1.0
            self.ul = -2.0
            self.pl = 0.4

            self.rr = 1.0
            self.ur = 2.0
            self.pr = 0.4

            self.T = 0.15
            self.x_0 = 0.5
            # cas test 3:
        if test_num == 3:
            self.rl = 1.0
            self.ul = 0.0
            self.pl = 1000

            self.rr = 1.0
            self.ur = 0.0
            self.pr = 0.01

            self.T = 0.012
            self.x_0 = 0.5

        if test_num == 4:  # cas test 4
            self.rl = 5.99924
            self.ul = 19.5975
            self.pl = 460.894

            self.rr = 5.99242
            self.ur = -6.19633
            self.pr = 46.0950

            self.T = 0.035
            self.x_0 = 0.4

        if test_num == 5:
            self.rl = 1.0
            self.ul = -19.59745
            self.pl = 1000

            self.rr = 1.0
            self.ur = -19.59745
            self.pr = 0.01

            self.T = 0.012
            self.x_0 = 0.8

    def initialization(self):
        """
        :return: initialisation
        """
        self.x = np.zeros((1, self.Nx + 1)).reshape(self.Nx + 1, 1)  # noeuds
        # print(self.x)
        self.xm = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # points milieu
        self.r = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # densite
        self.m = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # moment
        self.E = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # energie totale
        self.u = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # vitesse
        self.p = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # pression
        self.e = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # energie interne
        self.a = np.zeros((1, self.Nx)).reshape(self.Nx, 1)  # vecteur avec toutes les vitesses du son

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
        # print("xm avant = ", self.xm)

    def solve(self):
        F = np.zeros((3, self.Nx + 1))
        Fr = np.zeros(self.Nx + 1)
        Fm = np.zeros(self.Nx + 1)
        FE = np.zeros(self.Nx + 1)
        t = 0
        while t < self.T:
            Smax = 0
            for i in range(0, self.Nx):
                Smax = max(Smax, abs(self.u[i]) + self.a[i])
            dt = min(self.T - t, self.cfl * (self.dx / Smax))
            for i in range(0, self.Nx + 1):
                if i == 0:
                    self.rl = self.r[i]
                    self.ml = self.m[i]
                    self.El = self.E[i]
                else:
                    self.rl = self.r[i - 1]
                    self.ml = self.m[i - 1]
                    self.El = self.E[i - 1]
                if i == self.Nx:
                    self.rr = self.r[i - 1]
                    self.mr = self.m[i - 1]
                    self.Er = self.E[i - 1]
                else:
                    self.rr = self.r[i]
                    self.mr = self.m[i]
                    self.Er = self.E[i]
                print("rl=", self.rl)
                F[0, i] = \
                    numerical_fluxes.numerical_flux(self.type_solver, self.rl, self.ml, self.El, self.rr, self.mr,
                                                    self.Er)[
                        0]
                F[1, i] = \
                    numerical_fluxes.numerical_flux(self.type_solver, self.rl, self.ml, self.El, self.rr, self.mr,
                                                    self.Er)[
                        1]
                F[2, i] = \
                    numerical_fluxes.numerical_flux(self.type_solver, self.rl, self.ml, self.El, self.rr, self.mr,
                                                    self.Er)[
                        2]
                Fr[i] = F[0, i]
                Fm[i] = F[1, i]
                FE[i] = F[2, i]
                print("FE[i] = ", FE[i])
            for i in range(0, self.Nx):
                self.r[i] = self.r[i] - (dt / self.dx) * (Fr[i + 1] - Fr[i])  # densite
                self.m[i] = self.m[i] - (dt / self.dx) * (Fm[i + 1] - Fm[i])  # moment
                self.E[i] = self.E[i] - (dt / self.dx) * (FE[i + 1] - FE[i])
                self.u[i] = self.m[i] / self.r[i]
                self.p[i] = (self.gamma - 1.) * (self.E[i] - 0.5 * (self.m[i] ** 2) / self.r[i])  # pression
                #  On suppose que que le gaz obeit a la loi d'etat des gaz parfaits ==> p =(gamma -1)*rho*e
                self.e[i] = self.p[i] / (self.r[i] * (self.gamma - 1.))  # energie interne
                self.a[i] = np.sqrt(abs(self.gamma * self.p[i]) / self.r[i])
            t += dt
        # plt.plot(self.xm, self.p, color="black", linestyle="--")
        # plt.show()
        # plt.plot(self.xm, self.u, color="black", linestyle="--")
        #
        # plt.show()
        #   print("xm après = ", self.xm)
        print("Res = ", self.r)  # self.r, self.m, self.E, self.u, self.p, self.e, self.a)
        print("xm = ", self.xm)
        print("p = ", self.p)
        print("len(xm) = ", len(self.xm), "\nlen(p)", len(self.p))
        print(self.ul, self.rl, self.pl, "\n", self.ur, self.rr, self.pr)
        return self.r, self.m, self.E, self.u, self.p, self.e, self.a

    def euler_bis(self, solver_type, rl, ul, pl, rr, ur, pr, T, x_0):
        self.type_solver = solver_type
        self.rl = rl
        self.ul = ul
        self.pl = pl
        self.rr = rr
        self.ur = ur
        self.pr = pr
        self.T = T
        self.x_0 = x_0
        self.initialization()
        self.initial_states()
        self.initial_conditions()

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

    def euler(self, solver_type, test: int):
        """
        :param solver_type: type de solveur (Rusanov, HLL, HLLC)
        :param test: numero de test (1, 2, 3, 4)
        :return: 

        """""
        self.type_solver = solver_type
        self.test = self.choose_test(test)
        self.initialization()
        self.initial_states()
        self.initial_conditions()
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


if __name__ == "__main__":
    E = Euler1D(Nx=100)
    E.euler(solver_type="Rusanov", test=1)
# E.euler_bis("Rusanov", 1., 0., 1., 0.125, 0.0, 0.1, 0.2, 0.3)