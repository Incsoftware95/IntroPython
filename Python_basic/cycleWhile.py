# Developer: Breyner Ocampo C.
# Date: 13-04-2023
# script: While

# Definición de variables
# Ejemplo de un menú
j = 1
orden = ""
perro = 5
hamburguesa = 10
total = 0
while (j != 0):
  print(f"1- Hamburguesa ->{hamburguesa} usd\n2- Perro caliente ->{perro} usd \n0- Salir")
  try:
    j = int(input("Ingrese opcion: "))
    if j == 1:
      orden += "1- Hamburguesa\n"
      total += hamburguesa
    elif j == 2:
      orden += "1- Perro Caliente\n"
      total += perro
    elif j == 0:
      print("Gracias por visitarnos")
    else:
      print("No es una opcion")
  except ValueError as e:
    print("Error " + str(e)) 
else:
  print("Su orden es:\n")
  print(orden)
  print("Total: "+str(total))
