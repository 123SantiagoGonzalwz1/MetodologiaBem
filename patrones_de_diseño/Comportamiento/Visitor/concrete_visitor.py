from visitor import Visitor

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element):
        print(f'{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1')

    def visit_concrete_component_b(self, element):
        print(f'{element.exclusive_method_of_concrete_component_b()} + ConcreteVisitor1')

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element):
        print(f'{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2')

    def visit_concrete_component_b(self, element):
        print(f'{element.exclusive_method_of_concrete_component_b()} + ConcreteVisitor2')