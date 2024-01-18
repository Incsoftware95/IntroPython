from service.CamisetaService import CamisetaService
from data.Camiseta import Camiseta


class CamisetaController:

    def __init__(self) -> None:
        pass


    def setCamiseta(self,shirt:dict):
        talla , color = shirt.values()
        neWCamiseta = Camiseta(talla=talla,color=color)
        print(neWCamiseta)
        return "OK"
    def setdDat(self,shirt:dict):
        return CamisetaService().createCamiseta(data=shirt)
        