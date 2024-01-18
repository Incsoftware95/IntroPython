from data.Camiseta import Camiseta


class CamisetaService:


    def createCamiseta(self,data:dict):
        talla , color = data.values()
        neWCamiseta = Camiseta(talla=talla,color=color)
        print(neWCamiseta)
        return True