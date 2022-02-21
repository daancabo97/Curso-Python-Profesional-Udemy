def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['juan','maria','daniela']

if __name__ == '__main__':
    desplegarNombres(nombres)  # Tupla
    desplegarNombres('carlos') # Tupla 
    desplegarNombres((10, 11)) # Tupla
    desplegarNombres([10 , 11]) # Lista