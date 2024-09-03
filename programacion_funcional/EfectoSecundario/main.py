# Función pura
def adiciona1(lista, elemento):
    return lista + [elemento]

# Función con evento secundario
def adiciona2(lista, elemento):
    lista.append(elemento)
    return lista

if __name__ == "__main__":
    lista = [1]
    r = adiciona1(lista, 2)
    print('Resultado', r)
    print('Lista no ha cambiado', lista)

    lista = [1]
    r = adiciona2(lista, 2)
    print('Resultado', r)
    print('Lista ha cambiado', lista)
