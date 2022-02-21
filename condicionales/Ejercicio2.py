# Calcular estacion del año

mes = str(input(' Proporciona mes del año (Enero - Diciembre): '))
estacion = None
if mes == 'enero' or mes == 'diciembre':
    estacion = 'Invierno'
elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
    estacion = 'Primavera'
elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
    estacion = 'Verano'
elif mes == 'sepiembre' or mes == 'octubre' or mes == 'noviembre':
    estacion ='Otoño'
else:
    estacion = 'mes incorrecto'
print(f'Para el mes de {mes} la estacion es: {estacion}')
