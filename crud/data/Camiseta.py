class Camiseta:

    def __init__(self,talla,color) -> None:
        self.talla = talla
        self.color = color
    @property
    def gettalla(self):
        return self.talla
    def __str__(self) -> str:
        return f"talla: {self.talla}, color: {self.color}"
    
if __name__ == "__main__":

    ca =Camiseta("L","RED")
    print(ca)