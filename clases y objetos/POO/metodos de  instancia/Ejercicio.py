# Ejercicio aritmetica:

class Aritmetica:

    """
    Clase aritmetica para realizar las operaciones de sumar , restar . etc
    """

    def __init__(self , operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoB - self.operandoA

    def multiplicar(self):
        return self.operandoB * self.operandoA

    def dividir(self):
        return self.operandoB / self.operandoA

aritmetica1 = Aritmetica(5 , 7)
print(f' sumar : {aritmetica1.sumar()}' )
print(f' restar : {aritmetica1.restar()}' )
print(f' multiplicar : {aritmetica1.multiplicar()}' )
print(f' dividir : {aritmetica1.dividir()}' )



