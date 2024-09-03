from mediator import Mediator
from concrete_component import Component1, Component2

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str):
        if event == 'A':
            print('El mediador reacciona en A y desencadena las siguientes operaciones:')
            self._component2.do_c()
        elif event == 'D':
            print('El mediador reacciona en D y desencadena las siguientes operaciones:')
            self._component1.do_b()
            self._component2.do_c()