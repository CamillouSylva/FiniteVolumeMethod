#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Module contenant les classes qui permettent de creer les vecteurs des variables primitives
    W_L = (r_l, u_l, p_l) et W_R = (r_r, u_r, p_r) des états initiaux à gauche et à droite
"""


class W:
    def __init__(self, r: float, u: float, p: float):
        self._r = r
        self._u = u
        self._p = p

    def __repr__(self):
        return f" W = ({self.r}, {self.u}, {self.p})"

    @property
    def r(self):
        """
        return: densité rho
        """
        return self._r

    @r.setter
    def r(self, new_r: float):
        """
        :param new_r: Nouvelle valeur de la densité rho
        :return: Modifier la valeur de la densité rho
        """
        self._r = new_r

    @property
    def u(self):
        return self._u

    @u.setter
    def u(self, new_u: float):
        self._u = new_u

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, new_p: float):
        self._p = new_p


class Wl(W):
    """
        Vecteur des variables primitives (r=rho, u, p) de l'état initial à gauche
    """
    def __init__(self, rl: float, ul: float, pl: float):
        """
        :param rl: densité initiale (rho) à gauche
        :param ul: vitesse initiale (u) à gauche
        :param pl: pression initiale (p) à gauche
        """
        super().__init__(r=rl, u=ul, p=pl)

    def __repr__(self):
        return f"W_L = ({self.r}, {self.u}, {self.p})"


class Wr(W):
    """
    Vecteur des variables primitives (r=rho, u, p) de l'état initial à droite
    """
    def __init__(self, rr: float, ur: float, pr: float):
        """
        :param rr: densité initiale (rho) à droite
        :param ur: vitesse initiale (u) à droite
        :param pr: pression initiale (p) à droite
        """
        super().__init__(r=rr, u=ur, p=pr)

    def __repr__(self):
        return f"W_R = ({self.r}, {self.u}, {self.p})"


if __name__ == "__main__":
    # wl = W_l(1, 2, 3)
    # print(wl)
    # wl.rl = 12.
    # print(wl)

    wr = Wr(0, 1, 2)
    print(wr)


    def w(u, v, p):
        w = Wr(u, v, p)
        return w


    w1 = w(1, 2, 33)
    print(w1)
    w1.r = 77
    print("w1", w1)
    w1.u = 55
    print(w1)
    print(w1.u)

    v = Wl(10, 20, 30)
    print(v)
    v.u = 22
    print(v)
