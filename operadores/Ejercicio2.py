# Ejercicio determina si es mayor de edad

edad_adulto = 18
edad_persona = int(input("Ingresa tu edad: "))

if edad_persona >= edad_adulto:
    print(f'La persona con edad de {edad_persona} es adulto')
else:
    print(f'La persona con edad de {edad_persona} es menor')