
from config.ConnectionBD import connectionBD
from config.ModelsBD import Base
from data.Camiseta import Camiseta
from model.Usuario import Usuario
from controller.UsuarioController import UsuarioController
from controller.CamisetaController import CamisetaController







if __name__=="__main__":
    user1 = Usuario(email="roco@gmail.com",passwd="1234",name="RAMBO")
    shirt1 = Camiseta("X","MORADA")
    camiseta = {
                "talla":"X",
                "color":"RED"
                }
    camiC = CamisetaController().setCamiseta(shirt=camiseta)
    camiC = CamisetaController().setdDat(shirt=camiseta)

    engine = connectionBD()
    Base.metadata.create_all(engine,checkfirst=True)


    userD = {
                "name":"Lorena",
                "email":"Lorena.95@gmail.com",
                "passwd":"lolilove",
                }
    
    print(UsuarioController().__doc__)
    
    
    # CRUD
  
    #create =  UsuarioController().createUsuario(userD)
    read = UsuarioController().readUsuario()
    # update = UsuarioController().updateUsuario(5,userD)
    # delete = UsuarioController().deleteUsuario(2)

    
    
    
