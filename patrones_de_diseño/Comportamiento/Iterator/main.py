from iterator import WordsCollection

def main():
    collection = WordsCollection()
    collection.add_item('Primero')
    collection.add_item('Segundo')
    collection.add_item('Tercero')

    print('Transversal Recta:')
    print('\n'.join(collection))
    
    print('\nTransversal Reversa:')
    print('\n'.join(collection.get_reverse_iterator()), end='')

if __name__ == "__main__":
    main()