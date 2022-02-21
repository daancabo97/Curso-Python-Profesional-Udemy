# LISTA ES DE TIPO MUTABLE


# Definir una variable de tipok str
nombres = ['Juan','Karla','Maria',0, True , 5.1]

# Imprimir la lista de nombres
# print(nombres)

# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])

# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])

# imprimir un rango de valores
print(nombres[0:2])

# ir al inicio de la lista al indice
print(nombres[:3])

# ir desde el indice indicado hasta el final
print(nombres[1:])

# cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
 

# iterar un valor
for nombre in nombres:
   print(nombre)
else:
    print('no existen mas nombres en la lista')


# preguntar el largo de una lista
print(len(nombres))

# agregar un elemento
nombres.append('Daniel')
print(nombres)

# insertar un elemento en un indice especifico
nombres.insert(2,'Claudia')
print(nombres)

# remover un elemento
nombres.remove('Juan')
print(nombres)

#remover el ultimo valor agregado
nombres.pop()
print(nombres)

# Eliminar un elemento en un indice indicado
del nombres[5]
print(nombres)

# Limpiar la lista
    # nombres.clear()
    # print(nombres)

# Borrar la lista por completo
    # del nombres
    # print(nombres)




