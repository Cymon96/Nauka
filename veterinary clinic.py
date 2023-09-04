# Program do dodawania oraz usuwania pacjnetów i ich danych w placówce weterynaryjnej

import time
from enum import IntEnum

Menu = IntEnum("Menu", "Register Unregister Show Search")
Pets = {}

while True:
    print("\n")
    print("Menu weterynarii 'Pod martwym kotkiem'")
    print("1 - Zarejestruj pacjenta\n2 - Wyrejestruj pacjenta\n3 - "
          "Wyświetl wszystkich zarejestrowanych pacjentów\n4 - Znajdź w bazie pacjenta")

    choice = int(input("Wybierz działanie: "))
    Choice = Menu(choice)

    match Choice:
        case Menu.Register:
            print("\n")
            Name = input("Podaj imie zwierzecia: ").capitalize()
            Species = input("Podaj gatunek zwierzęcia: ").capitalize()
            Age = input("Podaj wiek zwierzęcia: ") + " Lat"
            Weight = input("Podaj wagę zwierzęcia: ") + "Kg"
            OwnersName = input("Podaj imie właściciela: ").capitalize()
            OwnersSurname = input("Podaj nazwisko właściciela: ").capitalize()

            Pets[Name] = {
                "Imie": Name,
                "Gatunek": Species,
                "Wiek": Age,
                "Waga": Weight,
                "Imie opiekuna": OwnersName,
                "Nazwisko opiekuna": OwnersSurname
            }
            print("\n")
            print(f"Zarejestrowano zwierzę o imieniu: {Name}")
            for key, value in Pets[Name].items():
                    print(f"{key}: {value}")
        case Menu.Unregister:
            unregister = input("Podaj imie zwierzecia które chcesz wyrejestrować: ").capitalize()
            if unregister in Pets:
                del Pets[unregister]
                print("Wyrejestrowano zwierze o imieniu: ", unregister)
        case Menu.Show:
            for patient in Pets:
                print("\n")
                for data in Pets[patient]:
                    print(data, Pets[patient][data])
        case Menu.Search:
            search = input("Podaj imie zwierzęcia: ").capitalize()
            if search in Pets:
                print("\n")
                for key, value in Pets[search].items():
                        print(f"{key}: {value}")
        case _:
            print("Wybrałeś błędną pozycję. Spróbuj ponownie za 5 sekund")
            time.sleep(5)
