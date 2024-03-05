
from config.ConnectionBD import connectionBD
from config.ModelsBD import Base
from data.Camiseta import Camiseta
from model.Usuario import Usuario
from controller.UsuarioController import UsuarioController
from controller.CamisetaController import CamisetaController


import streamlit as st
from view.HomeView import main_page
from view.CreateView import create
from view.UpdateView import update
from view.ReadView import read
from view.DeleteView import delete
import sys

def main():
    #  COnexion a la base de datos
    # engine = connectionBD()
    # Crea los modelos si no existen
    # Base.metadata.create_all(engine,checkfirst=True)

    # page_names_to_funcs = {
    #     "Home Page": main_page,
    #     "Create": create,
    #     "Read": read,
    #     "Update": update,
    #     "Delete": delete,
    # }
    v = sys.version.split(" ")
    st.sidebar.header(f"🐍 {v[0]}")
    # selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
    # page_names_to_funcs[selected_page]()


if __name__=="__main__":

    engine = connectionBD()
    Base.metadata.create_all(engine,checkfirst=True)
    
   
    # user1 = Usuario(email="roco@gmail.com",passwd="1234",name="RAMBO")
    # shirt1 = Camiseta("X","MORADA")
    # camiseta = {
    #             "talla":"X",
    #             "color":"RED"
    #             }
    # camiC = CamisetaController().setCamiseta(shirt=camiseta)
    # camiC = CamisetaController().setdDat(shirt=camiseta)

    # userD = {
    #             "name":"Lorena",
    #             "email":"Lorena.95@gmail.com",
    #             "passwd":"lolilove",
    #             }
    
    # print(UsuarioController().__doc__)
    
    
    # # CRUD
  
    # #create =  UsuarioController().createUsuario(userD)
    # read = UsuarioController().readUsuario()
    # print(read)
    # update = UsuarioController().updateUsuario(5,userD)
    # delete = UsuarioController().deleteUsuario(2)
