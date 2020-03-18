class Fonte3f:
    def __init__(self, Efn: tuple, IL: tuple):
        Eff = fasor(Efn)
        self.efn = Efn
        self.eff = (Efn[0]-Efn[1],Efn[1]-Efn[2],Efn[2]-Efn[0])
