
dia = """                                   
            Bienvenido elige como estuvo tu dia de 1 a 5

            1
            2
            3
            4
            5

            """  


opcion = int(input(dia))
print('Mi dia estuvo de:', opcion)
if opcion == 1:
    print('pesimo')
elif opcion == 2:
    print('Regular')
elif opcion == 3:
    print('Bueno')
elif opcion == 4:
    print('Genial')
elif opcion == 5:
    print('Excelente')
else:
    print('Elige una opcion valida')

