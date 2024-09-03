from random import sample
from string import ascii_letters
from memento import Memento
from concrete_memento import ConcreteMemento

class Originator:
    _state = None

    def __init__(self, state: str):
        self._state = state
        print(f'Originador: Mi estado inicial es: {self._state}')

    def do_something(self):
        print('Originador: Estoy haciendo algo importante.')
        self._state = self._generate_random_string(30)
        print(f'Originador: Y mi estado ha cambiado a: {self._state}')

    @staticmethod
    def _generate_random_string(length: int = 10):
        return ''.join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)
    
    def restore(self, memento: Memento):
        self._state = memento.get_state()
        print(f'Originador: Mi estado ha cambiado a: {self._state}')