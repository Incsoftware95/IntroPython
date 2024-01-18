# from data.Camiseta import Camiseta
from model.Auth import Auth

class Usuario(Auth):
    
    def __init__(self, email: str, passwd: str,name:str) -> None:
        super().__init__(email, passwd)
        self.name = name

    def get_name(self):
        return self.name
    

    def __str__(self) -> str:
        return f"Name: {self.name},  "+super().__str__()
if __name__ == "__main__":
    
    hu = Usuario(name="Einstein",passwd="Emc2",email="einstein1925@gmail.com")

