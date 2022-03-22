from cmath import sqrt as complex_sqrt
import numpy as np


def numerical_flux(solver_type: str, rl: float, ml: float, El: float, rr: float, mr: float, Er: float,
                   gamma: float = 1.4) -> np.ndarray:
    """
    :param solver_type: Solver type (Rusanov, HLL or HLLC)
    :param rl:
    :param ml:
    :param El:
    :param rr:
    :param mr:
    :param Er:
    :param gamma:
    :return:
    """
    Ur = np.array([rr, mr, Er]).reshape(3, 1)
    Ul = np.array([rl, ml, El]).reshape(3, 1)

    ul = ml / rl
    pl = (gamma - 1) * (El - 0.5 * (ml ** 2) / rl)
    al = complex_sqrt((gamma * pl / rl))

    pr = (gamma - 1) * (Er - 0.5 * (mr ** 2) / rr)
    ur = mr / rr
    ar = complex_sqrt(gamma * pr / rr)

    Fi = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
    Fl = np.zeros((3, 1))  # .reshape(3, 1)  # np.zeros(3)
    Fl[0] = ml
    Fl[1] = (ml ** 2) / rl + pl
    Fl[2] = (El + pl) * (ml / rl)

    Fr = np.zeros((3, 1))  # .reshape(3, 1)

    Fr[0] = mr
    Fr[1] = (mr ** 2) / rr + pr
    Fr[2] = (Er + pr) * (mr / rr)
    if solver_type == "Rusanov":  # flux numerique Rusanov ; Sl et Sr sont des vitesses d’onde
        Sl = (abs(ul) + al).real  # % vitesse minimale

        Sr = (abs(ur) + ar).real  # vitesse maximale
        #   print(Sr, Sl)

        Sp = max(Sl, Sr)

        Fi[0] = 0.5 * (Fl[0] + Fr[0] - Sp * (rr - rl))
        Fi[1] = 0.5 * (Fl[1] + Fr[1] - Sp * (mr - ml))
        Fi[2] = 0.5 * (Fl[2] + Fr[2] - Sp * (Er - El))

    if solver_type == "HLL":  # flux numerique HLL (Harten-Lax-Van Leer)

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

    if solver_type == "HLLC":  # flux numerique HLLC

        # Sl = (ul - al).real  # vitesse minimale

        # Sr = (ur + ar).real  # vitesse maximale

        Sl = min((ul - al).real, (ur - ar).real)
        Sr = max((ul + al).real, (ur + ar).real)
        #  print("pr",rl * (Sl - ul))
        Se = (pr - pl + rl * ul * (Sl - ul) - rr * ur * (Sr - ur)) / (rl * (Sl - ul) - rr * (Sr - ur))
        print((Sl - Se))
        Uel = (rl * ((Sl - ul) / (Sl - Se)) * np.array([1, Se, El / rl + (Se - ul) * (Se + pl / (rl * (Sl - ul)))],
                                                       dtype=float))
        # print("Uel", Uel)
        Uer = rr * ((Sr - ur) / (Sr - Se)) * np.array([1, Se, Er / rr + (Se - ur) * (Se + pr / (rr * (Sr - ur)))],
                                                      dtype=float)

        if Sl >= 0:
            Fi[0] = Fl[0]
            Fi[1] = Fl[1]
            Fi[2] = Fl[2]

        elif Sl <= 0 and 0 <= Se:
            Fi[0] = Fl[0] + Sl * (Uel[0] - Ul[0])
            Fi[1] = Fl[1] + Sl * (Uel[1] - Ul[1])
            Fi[2] = Fl[2] + Sl * (Uel[2] - Ul[2])

        elif Se <= 0 and 0 <= Sr:
            Fi[0] = Fr[0] + Sr * (Uer[0] - Ur[0])
            Fi[1] = Fr[1] + Sr * (Uer[1] - Ur[1])
            Fi[2] = Fr[2] + Sr * (Uer[2] - Ur[2])

        else:  # (Sr <= 0)
            Fi[0] = Fr[0]
            Fi[1] = Fr[1]
            Fi[2] = Fr[2]
    # print("Fi", Fi)
    return Fi.reshape(3, 1)


if __name__ == "__main__":
    print("fluxnum()", numerical_flux(solver_type="HLLC", rl=1., ml=1., El=0.1, rr=1., mr=0.5, Er=1.))

    flux = numerical_flux(solver_type="Rusanov", rl=1., ml=1., El=0.1, rr=1., mr=0.5, Er=1.)
    print("flux", flux)
