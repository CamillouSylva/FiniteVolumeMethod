#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cmath import sqrt as complex_sqrt
from FiniteVolumeMethod.Job.riemann_solver import RiemannSolver


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
    HLLC_S = HLLCSolver(W_L=[1., 0., 1.], W_R=[0.125, 0, 0.1], T=0.2)
    HLLC_S.solve()
    HLLC_S.plot()
