class Persona:
    def __init__(self, nombre , apellido ,  edad ):
       self.nombre = nombre 
       self.apellido = apellido
       self.edad = edad
    
    
persona1  = Persona('Juan','Perez',28)   
print(persona1.nombre)    
print(persona1.apellido)
print(persona1.edad)

class Carro:
    def __init__(self , motor , marca , color , cilindros , carroceria , año , gasolina):
        self.motor = motor
        self.marca = marca
        self.color = color
        self.cilindros = cilindros
        self.carroceria = carroceria
        self.año = año
        self.gasolina = gasolina

Carro1 = Carro(2.1,'Mazda','Negro', 4 ,'Sedan', 2020, 'Corriente')
print(Carro1.motor)
print(Carro1.marca)
print(Carro1.color)
print(Carro1.cilindros)
print(Carro1.carroceria)
print(Carro1.año)
print(Carro1.gasolina)