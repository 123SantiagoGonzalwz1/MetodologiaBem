from component import Component
from visitor import Visitor

class ConcreteComponentA(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self):
        return 'A'

class ConcreteComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def exclusive_method_of_concrete_component_b(self):
        return 'B'