# 'Pizza' Representa el producto final
class Pizza:
    # Inicialización de los atributos como 'None'
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    # Devulve los valores de la pizza en una cadena de texto
    def __str__(self):
        return f'Masa: {self.dough} | Salsa: {self.sauce} | Cubierta: {self.topping}'