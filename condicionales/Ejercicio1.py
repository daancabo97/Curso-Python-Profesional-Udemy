# Ejercicio conversion de Numero a texto

numero = int(input('Proporciona un valor entre 1 y 3: '))
numero_texto = ''
if numero == 1:
    numero_texto = 'numero uno'
elif numero == 2:
    numero_texto = 'numero dos'
elif numero == 3:
    numero_texto = 'numero tres'
else:
    numero_texto = 'Valor fuera de rango'
print(f'Numero proporcionado : {numero: } -> {numero_texto}')
