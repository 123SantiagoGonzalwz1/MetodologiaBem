def reduced(f, array, acc):
    if array == []:
        return acc
    else:
        acc_n = f(array[0], acc)
        return reduced(f, array[1:], acc_n)

def bigger(array):
    return reduced(lambda num, acc: num if num > acc else acc, array, 0)

def count(array):
    return reduced(lambda _, acc: acc + 1, array, 0)

def summation(array):
    return reduced(lambda num, acc: num + acc, array, 0)

print('Mayor: ', bigger([3,4,2,1,1]))
print('Conteo: ', count([3,4,2,1,1]))
print('Sumatoria: ', summation([3,4,2,1,1]))


def mapping(f, array):
    return reduced(lambda el, acc: acc + [f(el)], array, [])

def increase1(array):
    return mapping(lambda n: n + 1, array)

print(increase1([3,4,2,1,1]))