def update(array, value):
    new = array[:]
    new[-1] = value
    return new

my_array = [1,2,3]
nl = update(my_array, 5)
print(nl)
print(my_array)