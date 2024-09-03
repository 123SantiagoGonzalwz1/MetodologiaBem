from abstract_class import AbstractClass
from concrete_class import ConcreteClass1, ConcreteClass2

def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()

if __name__ == "__main__":
    print('El mismo código de cliente puede funcionar con diferentes subclases:')
    client_code(ConcreteClass1())
    print('')

    print('El mismo código de cliente puede funcionar con diferentes subclases:')
    client_code(ConcreteClass2())