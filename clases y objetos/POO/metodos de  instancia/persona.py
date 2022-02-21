class Persona:
    def __init__(self, nombre , apellido ,  edad ):
       self.nombre = nombre 
       self.apellido = apellido
       self.edad = edad
    
    def mostrar_detalle(self):
        print(f'persona: {self.nombre}, {self.apellido}, {self.edad}')


persona1 = Persona('Juan','Perez',28) 
persona1.mostrar_detalle()
#persona1.mostrar_detalle(persona1)

persona2 = Persona('Claudia','Escobar',27) 
persona2.mostrar_detalle()


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

    def mostrar_carro(self):
        print(f'carro: {self.motor}, {self.marca}, {self.color}, {self.cilindros}, {self.carroceria}, {self.año}, {self.gasolina}')


Carro1 = Carro(2.1,'Mazda','Negro', 4 ,'Sedan', 2020, 'Corriente')
Carro1.mostrar_carro()

Carro2 = Carro(2.1,'Renault','blanco', 6 ,'Camioneta', 2022, 'Gasolina')
Carro2.mostrar_carro()
