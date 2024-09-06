def fn(name, f, x):
    print(name, '\nEl valor inicial es: ', x)
    r = f(x)
    print('El valor final es', r, '\n------')
    return r

def fn_decorator(f):
    return lambda x: fn(f.__name__, f, x)

@fn_decorator
def f1(x):
    return f2(x) + f3(x)

@fn_decorator
def f2(x):
    return x * 2

@fn_decorator
def f3(x):
    return x - 5

f1(10)