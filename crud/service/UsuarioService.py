# Models

from model.Usuario import Usuario

# SqlAlchemy
from config.ModelsBD import Address, User
from config.ConnectionBD import connectionBD
from sqlalchemy.orm import Session
from sqlalchemy import select
#  Pandas
import pandas as pd

class UsuarioService:
    """
    CRUD usuario

    create: recibe data y guarda en la base de datos
    read: retorna el contenido de la base de datos
    update: actualiza por id en la base de datos
    delete: elimina por id en la base de datos
    
    """


    def createUsuario(self,data:dict):
        name, email , passwd = data.values()
        neWUser = Usuario(email= email,passwd=passwd,name=name)
        neWUser.encrypt()
        engine =  connectionBD()
        with Session(engine) as session:
            newU = User(
                name=name,
                passwd=neWUser.get_passwd(),
                addresses=[Address(email_address=email)],
            )
            session.add_all([newU])
            session.commit()
        return True    
    def readUsuario(self):
        engine =  connectionBD()
        with Session(engine) as session:
            stmt = select(User).join(Address.user).where(User.id==Address.user_id)

            #  Captura de datos para presentar con streamlit
            df = pd.read_sql(stmt,session.bind)
            # print(df)
            dat =[]
            for user in session.scalars(stmt):
                # print(user)
                dat.append(user)
        return df
    def updateUsuario(self,user_id,data:dict):
        name, email , passwd = data.values()
        neWUser = Usuario(email= email,passwd=passwd,name=name)
        neWUser.encrypt()
        engine =  connectionBD()
        with Session(engine) as session:
            userUpd =session.get(User,user_id)
            userUpd.name = name
            userUpd.addresses = [Address(email_address=email)]
            userUpd.passwd = neWUser.get_passwd()
            session.commit()
        return userUpd    
    
    
    def deleteUsuario(self,user_id):
        engine =  connectionBD()
        with Session(engine) as session:
            userDelete =session.get(User,user_id)
            session.delete(userDelete)
            session.commit()
        return userDelete

