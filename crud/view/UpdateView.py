import streamlit as st

# CRUD
from controller.UsuarioController import UsuarioController
def update():
    icon = "☑"
    st.markdown(f"# Update {icon}")
    st.sidebar.markdown(f"# Update {icon}")
    #  Formulario
    with st.form("my_form"):
        st.write("Actulizar registro")
        id = st.text_input('Inserte id')
        name = st.text_input('Nombre')
        email = st.text_input('Email')
        passwd = st.text_input('passwd')
      
        st.form_submit_button('Enviar')

    # Captura de datos
    __userD = {
                "name":name,
                "email":email,
                "passwd":passwd,
                }
    #  Validación simple
    if len(name)>0 and len(email)>0 and len(passwd)>0 and len(id)>0:
        update =  UsuarioController().updateUsuario(user_id=id,user=__userD)
  