class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.raza = raza
    
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def __init__(self, nombre, especie, color):
        super().__init__(nombre, especie)
        self.color = color
    
    def sonido(self):
        return "Miau!"

# Creamos una instancia de la clase Perro y una instancia de la clase Gato
perro1 = Perro("Firulais", "Canino", "Labrador")
gato1 = Gato("Garfield", "Felino", "Naranja")

# Accedemos a los atributos y métodos de las instancias
print(perro1.nombre)  # Imprime "Firulais"
print(perro1.raza)  # Imprime "Labrador"
print(perro1.sonido())  # Imprime "Guau!"
print(gato1.nombre)  # Imprime "Garfield"
print(gato1.color)  # Imprime "Naranja"
print(gato1.sonido())  # Imprime "Miau!"
