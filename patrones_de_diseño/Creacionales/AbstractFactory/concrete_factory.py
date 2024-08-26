from abstract_factory import UIAbstractFactory, Button, TextBox

# Implementaciones concretas de las clases abstractas
class DarkButton(Button):
    def paint(self):
        print("Botón Oscuro")

class DarkTextBox(TextBox):
    def paint(self):
        print("Caja de texto oscura")

class LightButton(Button):
    def paint(self):
        print("Botón Claro")

class LightTextBox(TextBox):
    def paint(self):
        print("Caja de texto clara")


# Devulven instancias de las clases anteriores
class DarkUIFactory(UIAbstractFactory):
    def create_button(self):
        return DarkButton()

    def create_textbox(self):
        return DarkTextBox()

class LightUIFactory(UIAbstractFactory):
    def create_button(self):
        return LightButton()

    def create_textbox(self):
        return LightTextBox()