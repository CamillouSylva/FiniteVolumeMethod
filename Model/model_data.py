# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtSignal

from FiniteVolumeMethod.Job import rusanov_solver, hll_solver, hllc_solver


class Model(QObject):
    # Faire hériter la classe Model() de QObject est nécessaire pour pouvoir utiliser les pyqtSignal()
    float_value_changed = pyqtSignal(float)
    int_value_changed = pyqtSignal(int)
    str_value_changed = pyqtSignal(str)
    L_value_changed = pyqtSignal()
    L_changed = pyqtSignal(float)
    type_solver_changed = pyqtSignal(str)
    problem_changed = pyqtSignal(str)

    def __init__(self,
                 r_l: float = 1.,
                 u_l: float = 0.,
                 p_l: float = 1.,
                 r_r: float = 0.125,
                 u_r: float = 0.,
                 p_r: float = 0.1,
                 x_0: float = 0.3,
                 nx: int = 100,
                 L: float = 1.,
                 T: float = 0.2,
                 cfl: float = 0.9,
                 gamma: float = 1.4,
                 ):
        super(Model, self).__init__()
        self._r_l = r_l
        self._u_l = u_l
        self._p_l = p_l
        self._r_r = r_r
        self._u_r = u_r
        self._p_r = p_r
        self._x_0 = x_0
        self._nx = nx
        self._L = L
        self._T = T
        self._cfl = cfl
        self._gamma = gamma
        self._type_solver = None
        self._problem = None

    def __repr__(self):
        return f" rl = {self.rl}, ul = {self.ul}, pl = {self.pl}\n" \
               f" rr = {self.rr}, ur = {self.ur}, pr = {self.pr}\n" \
               f" x_0 = {self.x_0}, Nx = {self.Nx}, T = {self.T}\n" \
               f" cfl = {self.cfl}, gamma = {self.gamma}, L = {self.L}\n" \
               f" Type de solveur : {self.type_solver}"

    @property
    def rl(self):
        return self._r_l

    @rl.setter
    def rl(self, value: float):
        self._r_l = value
        print(value)
        self.float_value_changed[float].emit(value)

    @property
    def ul(self):
        return self._u_l

    @ul.setter
    def ul(self, value: float):
        self._u_l = value
        self.float_value_changed[float].emit(value)

    @property
    def pl(self):
        return self._p_l

    @pl.setter
    def pl(self, value: float):
        self._p_l = value
        self.float_value_changed[float].emit(value)

    @property
    def rr(self):
        return self._r_r

    @rr.setter
    def rr(self, value: float):
        self._r_r = value
        self.float_value_changed[float].emit(value)

    @property
    def ur(self):
        return self._u_r

    @ur.setter
    def ur(self, value: float):
        self._u_r = value
        self.float_value_changed[float].emit(value)

    @property
    def pr(self):
        return self._p_r

    @pr.setter
    def pr(self, value: float):
        self._p_r = value
        self.float_value_changed[float].emit(value)

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, value: float):
        self._T = value
        self.float_value_changed[float].emit(value)

    @property
    def x_0(self):
        return self._x_0

    @x_0.setter
    def x_0(self, value: float):
        self._x_0 = value
        self.float_value_changed[float].emit(value)

    #  self.L_changed[float].emit(value)

    @property
    def Nx(self):
        return self._nx

    @Nx.setter
    def Nx(self, value: int):
        self._nx = value

    @property
    def cfl(self):
        return self._cfl

    @cfl.setter
    def cfl(self, value: float):
        self._cfl = value
        self.float_value_changed[float].emit(value)

    @property
    def gamma(self):
        return self._gamma

    @gamma.setter
    def gamma(self, value: float):
        self._gamma = value
        self.float_value_changed[float].emit(value)

    @property
    def L(self):
        print(self._L)
        return self._L

    @L.setter
    def L(self, value):
        self._L = value
        self.L_changed[float].emit(value)

        # self.str_value_changed[str].emit("L")
        # self.problem_changed[str].emit(self.type_solver)

    @property
    def type_solver(self):
        return self._type_solver

    @type_solver.setter
    def type_solver(self, _type_solver):
        self._type_solver = _type_solver
        self.type_solver_changed[str].emit(_type_solver)
        print("type de solveur modifié")

    def problem_to_solve(self):
        rl = self.rl
        ul = self.ul
        pl = self.pl

        rr = self.rr
        ur = self.ur
        pr = self.pr
        Nx = self.Nx
        x_0 = self.x_0
        T = self.T
        cfl = self.cfl
        L = self.L
        if self.type_solver == "Rusanov":

            self._problem = rusanov_solver.RusanovSolver([rl, ul, pl],
                                                         [rr, ur, pr],
                                                         nx=Nx, x_0=x_0, T=T,
                                                         L=L, cfl=cfl)
        elif self.type_solver == "HLL":
            self._problem = hll_solver.HLLSolver([rl, ul, pl],
                                                 [rr, ur, pr],
                                                 nx=Nx, x_0=x_0, T=T,
                                                 L=L, cfl=cfl)
        elif self.type_solver == "HLLC":
            self._problem = hllc_solver.HLLCSolver([rl, ul, pl],
                                                   [rr, ur, pr],
                                                   nx=Nx, x_0=x_0, T=T,
                                                   L=L, cfl=cfl)
        return self._problem

    @property
    def problem(self):
        return self._problem
        # return self.problem_to_solve()

    @problem.setter
    def problem(self, type_solver):
        self._problem = self.problem_to_solve()
        self.problem_changed[str].emit(type_solver)

    def solve_problem(self):
        if self._problem:
            self.problem.solve()

    @property
    def r(self):
        if self.problem:
            return self.problem.r

    @property
    def xm(self):
        if self.problem:
            return self.problem.xm

    @property
    def u(self):
        if self.problem:
            return self.problem.u

    @property
    def p(self):
        if self.problem:
            return self.problem.p

    @property
    def e(self):
        if self.problem:
            return self.problem.e

    # def set_problem(self):
    #     self._problem = self.problem_to_solve()


if __name__ == "__main__":
    d = Model()
    # d.x_0 = 0.999
    # print(d)
    # from FiniteVolumeMethod.Job.W import Wr, Wl
    #
    # w = Wr(d.rr, d.ur, d.pr)
    # print(w)
    # w.r = 99
    # print(w)
    # print(d)
    print(d.r)
    d.type_solver = "Rusanov"
    d.problem_to_solve()
    print("\nr = ", d.r)
    d.solve_problem()
    print("\nr = ", d.r)
    import matplotlib.pyplot as plt

    plt.plot(d.problem.xm, d.r)
    plt.show()
