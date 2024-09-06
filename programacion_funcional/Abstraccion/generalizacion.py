def fn(name, f, x):
    print(name, '\nEl valor inicial es: ', x)
    r = f(x)
    print('El valor final es', r, '\n------')
    return r

def f1(x):
    return fn('Función 1: ', lambda x: f2(x) + f3(x), x)

def f2(x):
    return fn('Función 2: ', lambda x: x * 2, x)

def f3(x):
    return fn('Función 3:', lambda x: x - 5, x)

f1(10)