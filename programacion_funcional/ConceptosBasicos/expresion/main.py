resultado = []

for i in valores:
    x = f(g(i))
    resultado.append(x)

# Menos conceptos
resultado = map(comp(f,g), valores)

