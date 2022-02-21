# Ejercicio and 

valor = int(input(' Escribe un valor: '))
valor_minimo = 0
valor_maximo = 5

# dentro_de_rango = (valor >= valor_minimo) and (valor <= valor_maximo)
dentro_de_rango = valor >= valor_minimo and valor <= valor_maximo

if dentro_de_rango:
    print(f'El valor {valor} esta dentro de rango' )
else:
    print(f'El valor {valor} esta fuera de rango' )
         