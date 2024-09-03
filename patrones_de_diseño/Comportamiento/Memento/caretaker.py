from originator import Originator

class Caretaker:
    def __init__(self, originator: Originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print('\nCuidador: Salvando el estado del originador...')
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f'Cuidador: Restaurando el estado a: {memento.get_name()}')

        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print('Cuidador: Aquí está la lista de recuerdos:')
        for memento in self._mementos:
            print(memento.get_name())