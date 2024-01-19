import streamlit as st

# CRUD
from controller.UsuarioController import UsuarioController


def delete():
    icon = "🗑"
    st.markdown(f"# Delete {icon}")
    st.sidebar.markdown(f"# Delete {icon}")
   
    with st.form("my_form"):
        st.write("Insere id para eliminar registro")

        id = st.text_input('Inserte id')
        st.form_submit_button('Enviar')

    
    if len(id)>0:
        delete =  UsuarioController().deleteUsuario(id)
        