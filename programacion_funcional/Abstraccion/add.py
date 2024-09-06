# Mutando la lista
def add(array):
    array.append('Manzana')
    return array

my_array = ['Pera', 'Banano']
print(add(my_array))
print(my_array)

# Lista no mutada
def add2(array):
    return array + ['Manzana']

my_array = ['Pera', 'Banano']
print(add2(my_array))
print(my_array)