import streamlit as st

# CRUD
from controller.UsuarioController import UsuarioController


def create():

    icon = "&#9999;"
    st.markdown(f"# Create {icon}")
    st.sidebar.markdown(f"# Create {icon}")
    with st.form("my_form"):
        st.write("Crear registro en la Base de datos Mysql")

        name = st.text_input('Nombre')
        email = st.text_input('Email')
        passwd = st.text_input('passwd')
 
        st.form_submit_button('Enviar')


    __userD = {
                "name":name,
                "email":email,
                "passwd":passwd,
                }
    if len(name)>0 and len(email)>0 and len(passwd)>0:
        create =  UsuarioController().createUsuario(__userD)