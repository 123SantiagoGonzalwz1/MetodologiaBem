from leaf import File
from composite import Directory

def main():
    file1 = File('Archivo1.txt')
    file2 = File('Archivo2.csv')
    directory1 = Directory('Directorio1')

    directory1.add(file1)
    directory1.add(file2)

    directory1.show_details()

if __name__ == "__main__":
    main()