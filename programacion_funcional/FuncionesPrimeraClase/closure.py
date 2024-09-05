def funcion():
    x = 1
    def interna():
        return x
    return interna

f2 = funcion()
assert f2() == 1
print('OK')

print(f2)

print(f2())