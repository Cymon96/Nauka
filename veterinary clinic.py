# Program do dodawania oraz usuwania pacjnetów i ich danych w placówce weterynaryjnej

import time

Pets = {}

while True:
    print("\n")
    print("Menu weterynarii 'Pod martwym kotkiem'")
    print("1 - Zarejestruj pacjenta\n2 - Wyrejestruj pacjenta\n3 - "
          "Wyświetl wszystkich zarejestrowanych pacjentów\n4 - Znajdź w bazie pacjenta")

    Menu = input("Wybierz działanie: ")

    if Menu == "1":
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
            if key != "Imię":
                print(f"{key}: {value}")
    elif Menu == "2":
        unregister = input("Podaj imie zwierzecia które chcesz wyrejestrować: ").capitalize()
        if unregister in Pets:
            del Pets[unregister]
            print("Wyrejestrowano zwierze o imieniu: ", unregister)
    elif Menu == "3":
        for patient in Pets:
            print("\n")
            for data in Pets[patient]:
                print(data, Pets[patient][data])
    elif Menu == "4":
        search = input("Podaj imie zwierzęcia: ").capitalize()
        if search in Pets:
            print("\n")
            for key, value in Pets[search].items():
                if key != search:
                    print(f"{key}: {value}")
    else:
        print("Wybrałeś błędną pozycje. Spróbuj ponownie za 5 sekund")
        time.sleep(5)
