# Proyecto CRUD

Proyecto CRUD con persistencia de datos con el motor Mysql, utilizando python aplicando los conocimiento aprendidos en el libro Introducción a python.

## Configuracion

Creación de entorno virtual, debe tener instalado virtualenv pip install virtualenv

`
vitualenv env
`

### Activación de entorno virtual

`
source env/Scripts/activate
`

Si todo esta correcto probar en la terminal pip freeze y no debe tener ninguna libreria instalada.

Si no le reconoce las librerias debe seleccionar le interprete del entorno virtual.

VSC seleccionar interprete del etorno virual

`
/env/scripts/python.exe
`

## View

La visualización del crud se utilizo uno de los mejores frameworks para despliegue de datos en proyecto de machine learning o data science, sacando provecho al poder de manejo de datos de python.

Para desplegar el proyecto se debe utilizar el siguiente comando:

`
python -m streamlit run app.py
`

### Iconos

Pagina de iconos para mejorar la parte visual

[symbl](https://symbl.cc/es/)

### Requerimientos

Para generar los requerimientos se debe utilizar el siguiente comando:

`pip freeze > requirements.txt`

Si desea compilar el proyecto, luego de la activación del entorno virtual debe instalar los requerimientos del proyecto con el siguiente comando.

`pip install requirements.txt`
