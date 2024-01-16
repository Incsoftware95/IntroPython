
class Coche:
    # constructor
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.encendido = False

    # métodos
    def encender(self):
        self.encendido = True
        print("El coche está encendido")

    def apagar(self):
        self.encendido = False
        print("El coche está apagado")

    def info_coche(self):
        print(
            f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Color: {self.color}, Encendido: {self.encendido}")

if __name__ == "__main__":
    # instancia de la clase
    mi_coche = Coche("Toyota", "Corolla", 2020, "Negro")

    # acceder a los atributos de la instancia
    print(mi_coche.marca)
    print(mi_coche.modelo)
    print(mi_coche.anio)
    print(mi_coche.color)

    # llamar a los métodos de la instancia
    mi_coche.encender()
    mi_coche.info_coche()
    mi_coche.apagar()
    mi_coche.info_coche()
