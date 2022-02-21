class Persona:
    def __init__(self):
       self.nombre = 'Juan'
       self.apellido = 'Perez'
       self.edad = 28
    
    
persona1  = Persona()   
print(persona1.nombre)    
print(persona1.apellido)
print(persona1.edad)


class Carro:
    def __init__(self):
        self.motor = 2.1
        self.marca = "Mazda"
        self.color = "Negro"
        self.cilindros = 4
        self.carroceria = "Sedan"
        self.año = 2020
        self.gasolina = "Corriente"

Carro1 = Carro()
print(Carro1.motor)
print(Carro1.marca)
print(Carro1.color)
print(Carro1.cilindros)
print(Carro1.carroceria)
print(Carro1.año)
print(Carro1.gasolina)