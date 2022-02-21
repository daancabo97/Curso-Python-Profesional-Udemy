# Ejercicio tienda de libros

print(""" Proporcione los siguientes datos del libro: """)
nombre = str(input(""" Ingresa el nombre del libro: """))
id = int(input(""" Ingresa el codigo el codigo del libro: """))
precio = float(input(""" Ingresa el precio del libro: """))
envio = (input(""" Indique si el envio es gratis: """))



if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir True o False'

print(f'''
      Nombre:{nombre}
      id:{id}
      precio:{precio}
      envio gratuito?:{envio}
      ''')

print('fin del la informacion')

