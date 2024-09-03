from originator import Originator
from caretaker import Caretaker

def main():
    originator = Originator('Super-duper-super-puper-super.')
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print('\nCliente: Ahora retrocedamos!\n')
    caretaker.undo()

    print('\nCliente: Una vez más!\n')
    caretaker.undo()

if __name__ == "__main__":
    main()