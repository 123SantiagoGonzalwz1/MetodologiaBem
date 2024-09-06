def reduced(f, array, acc):
    for el in array:
        acc = f(el, acc)
    return acc

def bigger(array):
    return reduced(lambda num, acc: num if num > acc else acc, array, 0)

def count(array):
    return reduced(lambda _, acc: acc + 1, array, 0)

def summation(array):
    return reduced(lambda num, acc: num + acc, array, 0)

def mapping(f, array):
    return reduced(lambda el, acc: acc + [f(el)], array, [])

def increase1(array):
    return mapping(lambda n: n + 1, array)

print('Mayor:', bigger([3,4,2,1,1]))
print('Conteo:', count([3,4,2,1,1]))
print('Sumatoria:', summation([3,4,2,1,1]))
print('Incrementa1:', increase1([3,4,2,1,1]))