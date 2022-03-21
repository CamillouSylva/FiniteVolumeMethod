# %%
import numpy as np
import cmath


def fluxnum(type, rl, ml, El, rr, mr, Er):
    Ur = np.array([[rr], [mr], [Er]])
    Ul = np.array([[rl], [ml], [El]])

    gamma = 1.4
    ul = ml / rl
    pl = (gamma - 1) * (El - 0.5 * (ml ** 2) / rl)
    al = cmath.sqrt(gamma * pl / rl)
    ur = mr / rr
    pr = (gamma - 1) * (Er - 0.5 * (mr ** 2) / rr)
    ar = cmath.sqrt(gamma * pr / rr)

    Fi, Fl = np.zeros((3, 1)), np.zeros((3, 1))

    Fl[0] = ml
    Fl[1] = (ml ** 2) / rl + pl
    Fl[2] = (El + pl) * (ml / rl)

    Fr = np.zeros((3, 1))

    Fr[0] = mr
    Fr[1] = (mr ** 2) / rr + pr
    Fr[2] = (Er + pr) * (mr / rr)

    if type == 1:  # flux numerique Rusanov
        Sl = (np.abs(ul) + al).real
        Sr = (np.abs(ur) + ar).real
        Sp = max(Sl, Sr)
        Fi[0] = 0.5 * (Fl[0] + Fr[0] - Sp * (rr - rl))
        Fi[1] = 0.5 * (Fl[1] + Fr[1] - Sp * (mr - ml))
        Fi[2] = 0.5 * (Fl[2] + Fr[2] - Sp * (Er - El))

    elif type == 2:  # flux numerique HLL
        Sl = (ul - al).real  # vitesse minimale
        Sr = (ur + ar).real  # vitesse maximale

        if Sl >= 0:
            Fi = Fl
        elif Sl < 0 & 0 < Sr:
            Fi = (Sr * Fl - Sl * Fr + Sl * Sr * (Ur - Ul)) / (Sr - Sl)
        else:  # 0>=Sr
            Fi = Fr

    elif type == 3:  # flux numerique HLLC
        # Sl=(ul-al).real #vitesse minimale
        # Sr=(ur+ar).real #vitesse maximale
        Sl = min((ul - al).real, (ur - ar).real)
        Sr = max((ul + al).real, (ur + ar).real)
        Se = (pr - pl + rl * ul * (Sl - ul) - rr * ur * (Sr - ur)) / (rr * (Sl - ul) - rr * (Sr - ur))

        Uel = rl * ((Sl - ul) / (Sl - Se)) * np.array([[1.], [Se], [El / rl + (Se - ul) * (Se + pl / (rl * (Sl - ul)))]])
        Uer = rr * ((Sr - ur) / (Sr - Se)) * np.array([[1.], [Se], [Er / rr + (Se - ur) * (Se + pr / (rr * (Sr - ur)))]])
        if Sl >= 0:
            Fi = Fl
        elif (Sl <= 0) & (0 <= Se):
            Fi = Fl + Sl * (Uel - Ul)
        elif (Se <= 0) & (0 <= Sr):
            Fi = Fr + Sr * (Uer - Ur)
        else:  # Sr<=0
            Fi = Fr
    return {"type": type, "pl": pl, "al": al, "Fr": Fr, "Fl": Fl, "Fi": Fi}


if __name__ == "__main__":
    f = fluxnum(type=3, rl=1.0, ml=1., El=0.1, rr=1., mr=0.5, Er=1.)
    # fluxnum(type=3, rl=1.0, ml=1., El=0.1, rr=1., mr=0.5, Er=1.)
    # fluxnum(type=3, rl=1.0, ml=1., El=0.1, rr=1., mr=0.5, Er=1.)
    print(f)
    # %%
