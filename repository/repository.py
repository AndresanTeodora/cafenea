from domain.cafea import Cafea

class Repository:
    def __init__(self,validator):
        self.__cafele={'1':Cafea(1,'Capuccino','Italia',15),
                       '2':Cafea(2,'Frappe','America',10)}
        self.__validator=validator

    #def save
    def add(self,cafea):
        self.__validator.validate(cafea)
        self.__cafele[cafea.id]=cafea

    def delete(self,id):
        del self.__cafele[id]

