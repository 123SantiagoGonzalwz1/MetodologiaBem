from pyrsistent import PClass, field

class Spot(PClass):
    x = field()
    y = field()

    def traslation(self, dx, dy):
        return self.set(x = self.x + dx, y = self.y + dy)

spot1 = Spot(x = 1, y = 2)
spot2 = spot1.traslation(5,5)

print(spot1)
print(spot2)