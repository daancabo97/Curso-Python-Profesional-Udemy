def ListarTerminos(**Terminos):
    for llave, valor in Terminos.items():
        print(f'{llave}: {valor}')


if __name__ == '__main__':
    ListarTerminos(IDE = 'Integrated Development Environment', PK="Primary Key")
    ListarTerminos(DBMS = 'Database Managent System')   
