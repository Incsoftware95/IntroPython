# ¿Como crear una carpeta y un archivo de texto en python?

# importamos la librería os
import os

# Definimos el nombre de la carpeta y el archivo
folder_name = "mi_carpeta"
file_name = "mi_archivo.txt"

# Creamos la carpeta si no existe
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Creamos el archivo dentro de la carpeta
file_path = os.path.join(folder_name, file_name)
with open(file_path, 'w') as f:
    f.write("Este es mi archivo de texto creado con Python!")
