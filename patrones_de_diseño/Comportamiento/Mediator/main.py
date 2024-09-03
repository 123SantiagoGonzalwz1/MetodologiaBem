from concrete_mediator import ConcreteMediator
from concrete_component import Component1, Component2

def main():
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print('El cliente desencadena la operación A.')
    c1.do_a()

    print('\n', end='')

    print('El cliente desencadena la operación D.')
    c2.do_d()

if __name__ == '__main__':
    main()