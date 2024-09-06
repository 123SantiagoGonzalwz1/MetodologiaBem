def count(array):
    if array == []:
        return 0
    else:
        return 1 + count(array[1:])

def summation(array):
    if array == []:
        return 0
    else:
        return array[0] + summation(array[1:])

print(count([1,2,3,4]))
print(summation([1,2,3,4]))


def counting_and_summation(f, array):
    if array == []:
        return 0
    else:
        return f(array[0]) + counting_and_summation(f, array[1:])

print('Conteo: ', counting_and_summation(lambda n: 1, [1,2,3,4]))
print('Sumatoria: ', counting_and_summation(lambda n: n, [1,2,3,4]))