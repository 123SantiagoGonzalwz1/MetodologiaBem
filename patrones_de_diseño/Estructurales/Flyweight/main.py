from factory import ChessPieceFactory

def main():
    piece1 = ChessPieceFactory.get_flyweight('Peón', 'Blanco')
    piece2 = ChessPieceFactory.get_flyweight('Peón', 'Blanco')

    print(piece1 is piece2)

    piece1.display('A4')
    piece2.display('H2')

if __name__ == "__main__":
    main()