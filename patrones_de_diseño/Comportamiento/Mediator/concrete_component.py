from base_component import BaseComponent

class Component1(BaseComponent):
    def do_a(self):
        print('El componente 1 hace A.')
        self.mediator.notify(self, 'A')

    def do_b(self):
        print('El componente 1 hace B')
        self.mediator.notify(self, 'B')

class Component2(BaseComponent):
    def do_c(self):
        print('El componente 2 hace C.')
        self.mediator.notify(self, 'C')

    def do_d(self):
        print('El componente 2 hace D')
        self.mediator.notify(self, 'D')

