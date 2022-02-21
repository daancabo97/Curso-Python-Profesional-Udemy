# TUPLA ES DE TIPO INMUTABLE

frutas = ('naranja','papaya','mango')
print(frutas)

#saber el largo
print(len(frutas))

#acceder a un elemento
print(frutas[0])

#acceder de forma inversa en los elemntos
print(frutas[-1])

#acceder a un rango
print(frutas[0:2])


#recorrer elementos de un tupla con for
for fruta in frutas:
     print(fruta, end =' ')

#cambiar valor de tupla


#convertir tupla a una lista y modificar un elemento
frutas_lista = list(frutas)
frutas_lista[0] = 'Pera'
frutas = tuple(frutas_lista)
print('\n',frutas)

#Eliminar la tupla
    # del frutas
    # print(frutas)