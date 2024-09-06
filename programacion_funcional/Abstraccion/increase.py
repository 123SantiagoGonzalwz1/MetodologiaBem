def increases1(numbers):
    if numbers == []:
        return []
    else:
        return [numbers[0] + 1] + increases1(numbers[1:])

print(increases1([1,2,3]))

def increases2(numbers):
    if numbers == []:
        return []
    else:
        return [numbers[0] + 2] + increases2(numbers[1:])

print(increases2([1,2,3]))

def increases(f, numbers):
    if numbers == []:
        return []
    else:
        return [f(numbers[0])] + increases(f, numbers[1:])

print(increases(lambda n: n + 4, [1,2,3]))