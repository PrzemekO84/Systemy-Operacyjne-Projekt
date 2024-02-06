import os

def wyswietl_foldery(sciezka):
    # Wyświetlenie informacji o bieżącym katalogu
    print("Aktualny katalog:", sciezka)
    
    # Wyświetlenie listy folderów w podanej ścieżce
    print("\nFoldery w bieżącym katalogu:")
    for folder in os.listdir(sciezka):
        if os.path.isdir(os.path.join(sciezka, folder)):
            print(folder)

def nawiguj_po_folderach():
    sciezka_katalogu_domowego = os.path.expanduser('~')
    
    while True:
        wyswietl_foldery(sciezka_katalogu_domowego)
        wybor = input("\nWpisz nazwę folderu, aby przejść do niego (lub 'q' aby wyjść): ")
        
        if wybor.lower() == 'q':
            break
        
        nowa_sciezka = os.path.join(sciezka_katalogu_domowego, wybor)
        
        if os.path.isdir(nowa_sciezka):
            sciezka_katalogu_domowego = nowa_sciezka
        else:
            print("Podany folder nie istnieje. Spróbuj ponownie.")

if __name__ == "__main__":
    nawiguj_po_folderach()
