from concrete_factory import DarkUIFactory, LightUIFactory

# Código del cliente que utiliza
# una fábrica para crear productos
def client_code(factory):
    button = factory.create_button()
    textbox = factory.create_textbox()

    button.paint()
    textbox.paint()

# Eejecución y creación del botón
# y caja de texto con sus respectivos
# temas
if __name__ == "__main__":
    client_code(DarkUIFactory())
    print()
    client_code(LightUIFactory())