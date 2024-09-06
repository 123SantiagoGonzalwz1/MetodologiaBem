from pyrsistent import pvector, v
from IPython.display import display

vec = pvector([1,2,3])
vec2 = v(1,2,3)

print(vec[2])
print(vec2[0])

display(vec.append(4))
print(vec)

r = vec2.append(5)
print(r)
print(vec2)
print('----------------')

display(vec.set(0,11))
print(vec)

r = vec2.set(0,22)
print(r)
print(vec2)