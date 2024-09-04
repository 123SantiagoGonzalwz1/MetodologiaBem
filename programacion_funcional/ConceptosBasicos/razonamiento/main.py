def f1(lista):
    return [x * 2 for x in lista]

def f2(palabra):
    return [palabra]

def mi_funcion(x,y):
    return f1(x) + f2(y)

print(f1([1,2]))
print(f2('Hola'))

print(mi_funcion([3,4], 'Saludos'))

assert mi_funcion([3,4], 'Saludos') == [6,8, 'Saludos']
print('Funciono!')