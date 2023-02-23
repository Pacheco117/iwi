class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es " + self.nombre + " y tengo " + str(self.edad) + " años.")

person = Persona("Sergio", 22)
person.saludar()