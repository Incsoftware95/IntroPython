import streamlit as st

# CRUD
from controller.UsuarioController import UsuarioController
def read():
    icon = "🕮"
    st.markdown(f"# Read {icon}")
    st.sidebar.markdown(f"# Read {icon}")
    st.write("Lista de Registro de Usuario")
    #  Consulta en la base de datos
    read = UsuarioController().readUsuario()
    st.table(read)


