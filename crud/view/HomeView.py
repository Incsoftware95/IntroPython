import streamlit as st


def main_page():
    icon = "🎈🏛"
    st.markdown(f"# HOME {icon}")
    st.sidebar.markdown(f"# HOME {icon}")
    st.write("# Bienvenido a nuestro CRUD con python por BOC! 👋")

    st.sidebar.success("Seleccione una pagina.")

    st.markdown(
        """
        ### Introducción a python
        
        Proyecto final desarrollado en el libro introducción a python.

        Esta GUI se desarrollo utilizando el framework streamlit especializado para el despliegue de datos
        en proyectos de machine learning y data science.

        Para nuestro proyecto se realizo un CRUD con python con persistencia de datos con MySql de forma local, el cual provee los datos que se visualizaran con 
        streamlit.
        👈 Seleccione del sidebar 
       
        - Github [streamlit.io](https://streamlit.io)
        - Documentacion Streamlit [documentation](https://docs.streamlit.io)
    """
    )


