from pyrsistent import pset, s

s1 = pset(['Manzana', 'Pera'])
print(s1)

s2 = s('Banano', 'Ciruela')
print(s2)

print('----------------')

# Unión
fruit = s1 | s2
print(fruit)

# Adición
ns = s1.add('Durazno')
print(ns)
print(s1)

# Eliminar
rs = ns.remove('Manzana')
print(rs)
print(ns)