class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


if __name__ == "__main__":

    # Crear objeto de la clase Persona
    p = Persona("Breyner", 25)

    # Obtener el nombre y la edad
    nombre = p.get_nombre()
    edad = p.get_edad()
    print(nombre, edad)  # Salida: Breyner 25

    # Modificar el nombre y la edad
    p.set_nombre("Pedro")
    p.set_edad(30)

    # Obtener el nombre y la edad actualizados
    nombre = p.get_nombre()
    edad = p.get_edad()
    print(nombre, edad)  # Salida: Pedro 30

    # Intentar acceder directamente a los atributos privados genera un error
    print(p.__nombre)  # Genera un error


