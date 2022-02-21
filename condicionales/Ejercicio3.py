# Desarrollar etapas de vida segun edad
edad = int(input(' Proporciona tu edad: '))
etapa = None
if  0 <= edad <= 10:
    etapa = 'La infancia es increible...'
elif 10 <= edad <= 20:
    etapa = 'Muchos cambios y mucho estudio...'
elif 20 <= edad <= 30:
    etapa = 'Amor y comienza el trabajo...'
else:
    etapa = 'Etapa de vida no reconocida'
print(f'Para la edad de {edad} la etapa es: {etapa}')
