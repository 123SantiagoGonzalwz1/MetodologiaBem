from pyrsistent import freeze, thaw

data = [[1,2,3,4], [3,4,5], {'a':10, 'b':20}]
print(data)

di = freeze(data)
print(di)

r = thaw(di)
print(r)