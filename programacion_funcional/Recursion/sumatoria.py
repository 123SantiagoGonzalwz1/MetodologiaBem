def sumatoria(lista):
    # Caso Base
    if lista == []:
        return 0
    else:
        # Recursión
        return lista[0] + sumatoria(lista[1:])

print(sumatoria([1,2,3,4,5]))