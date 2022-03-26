#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cmath import sqrt as complex_sqrt
from FiniteVolumeMethod.Job.riemann_solver import RiemannSolver


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


if __name__ == "__main__":
    HLLS = HLLSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2)
    HLLS.solve()
    HLLS.plot()
