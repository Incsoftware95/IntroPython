# Developer: Breyner Ocampo C.
# Date: 13-04-2023
# script: condicionales

# Definición de variables

edad_1 = 10
edad = 12
# Condicionales 
# Comparar edades
if edad_1 > edad:
  print(f"{edad_1} es mayor a {edad}")
  edad_1 = 10
elif edad_1 < edad and edad_1 >=1:
  print(f"{edad_1} es menor a {edad}")
else:
  print(f"{edad_1} no es una edad")

#  Condicional ternario
votar = "Mayor de edad puede votar" if edad >= 18 else "Menor de edad no puede votar"
print(votar)

