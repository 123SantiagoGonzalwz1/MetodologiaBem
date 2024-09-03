from component import Component
from visitor import Visitor
from concrete_component import ConcreteComponentA, ConcreteComponentB
from concrete_visitor import ConcreteVisitor1, ConcreteVisitor2
from typing import List

def client_code(components: List[Component], visitor: Visitor):
    for component in components:
        component.accept(visitor)

if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print('El código cliente funciona con todos los visitantes a través de la interfaz de visitante base:')
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print('Permite que el mismo código de cliente funcione con diferentes tipos de visitantes:')
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)