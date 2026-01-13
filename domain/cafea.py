class Cafea
    def __init__(self,nume,tara_origine,pret):
        self.__nume=nume
        self.__tara_origine=tara_origine
        self.__pret=pret

    @property
    def nume(self):
        return self.__nume

    @property
    def tara_origine(self):
        return self.__tara_origine

    @property
    def pret(self):
        return self.__pret

    @nume.setter
    def set_nume(self,nume):
        self.__nume=nume

    @tara_origine.setter
    def set_tara_origine(self,tara_origine):
        self.__tara_origine=tara_origine

    @pret.setter
    def set_pret(self,pret):
        self.__pret=pret

    def __str__(self):
        return f"Nume: {self.__nume} este scumpa: {self.__pret} si este din {self.__tara_origine}"