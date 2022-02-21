class Persona:
    def __init__(self, nombre , apellido ,  edad ):
       self.nombre = nombre 
       self.apellido = apellido
       self.edad = edad
    


persona1 = Persona('Juan','Perez',28) 
print(f'Objeto persona 1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}')

persona2 = Persona('Claudia','Escobar',27) 
print(f'Objeto persona 2: {persona2.nombre}, {persona2.apellido}, {persona2.edad}')


################################################################################################################################################

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
print(f'objeto carro 1 : {Carro1.motor}, {Carro1.marca}, {Carro1.color}, {Carro1.cilindros}, {Carro1.carroceria}, {Carro1.año}, {Carro1.gasolina}')

Carro2 = Carro(2.1,'Renault','blanco', 6 ,'Camioneta', 2022, 'Gasolina')
print(f'objeto carro 2 : {Carro2.motor}, {Carro2.marca}, {Carro2.color}, {Carro2.cilindros}, {Carro2.carroceria}, {Carro2.año}, {Carro2.gasolina}')