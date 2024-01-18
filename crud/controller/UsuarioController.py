
from service.UsuarioService import UsuarioService



class UsuarioController:
    """
    CRUD
    controller
    llama los servicios
    """

    def createUsuario(self,user:dict):
        UsuarioService().createUsuario(data=user)
        return  "View"
    def readUsuario(self):
        users = UsuarioService().readUsuario()
        return users
    def updateUsuario(self,user_id,user:dict):
        user = UsuarioService().updateUsuario(user_id=user_id,data=user)
        return user
    def deleteUsuario(self,user_id):
        user = UsuarioService().deleteUsuario(user_id=user_id)
        return user
        