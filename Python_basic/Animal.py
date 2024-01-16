from abc import ABC, abstractmethod

# La clase animal hereda de ABC


class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        return "Guau guau"


class Gato(Animal):
    def sonido(self):
        return "Miau miau"


if __name__ == "__main__":
    # instancia de la clase
    mi_perro = Perro()
    mi_gato = Gato()


    # llamar a los métodos de la instancia
    print(mi_perro.sonido())
    print(mi_gato.sonido())

