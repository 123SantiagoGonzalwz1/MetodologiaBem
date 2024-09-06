from pyrsistent import pmap, m

d1 = pmap({ 'Hola' : 'a todos', 'Santiago' : 'González' })
print(d1)

d2 = m(a = 1, b = 5)
print(d2)

print('------------')

print(d1['Hola'])
print(d2['b'])

print('-----------')

r = d1.set('Santiago', 'aprende')
print(r)
print(d1)