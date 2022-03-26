#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cmath import sqrt as complex_sqrt
from FiniteVolumeMethod.Job.riemann_solver import RiemannSolver


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


if __name__ == "__main__":
    RS = RusanovSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2)
    RS.W_L.u = 99
    print(RS.W_L.u)

    RS.solve()
    print(RS.W_L.u)
    RS.plot()
