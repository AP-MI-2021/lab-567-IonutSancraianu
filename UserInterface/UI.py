from Domain.functionality import afisare_vanzari, adaugare_vanzare, stergere_vanzare, modificare_vanzare
from Domain.read import creare_vanzare, bagam_in_cufar, inchide_cufar, deschide_cufar


def main():
    deschide_cufar()
    while True:
        print("Alegeti optiunea pe care o doriti: ")
        print("1 - Citirea primei vanzari.")
        print("2 - Afisarea tuturor vanzarilor")
        print("3 - Adaugarea unei vanzari noi.")
        print("4 - Stergerea unei vanzari existente.")
        print("5 - Modificarea unei liste deja existente.")
        print("6 - Aplicarea discountului in functie de tipul de reducere si afisarea noului pret "
              "pentru fiecare vanzare")
        print("u - intoarcerea listei de vanzari la versiunea precedenta ultimei modificari")
        print("x - Oprirea programului")
        optiune = str(input("optiune -> "))
        librarie = []
        if optiune == "1":
            creare_vanzare(librarie)
        elif optiune == "2":
            afisare_vanzari(librarie)
        elif optiune == "3":
            adaugare_vanzare(librarie)
        elif optiune == "x":
            bagam_in_cufar(librarie)
            inchide_cufar()
            break
        elif optiune == "4":
            id_vanzare = input("Id-ul vanzarii care trebuie eliminata -> ")
            stergere_vanzare(librarie, id_vanzare)
        elif optiune == "5":
            id_vanzare = input("Id-ul vanzarii care trebuie modificata -> ")
            key = str(input("elementul vanzarii care trebuie modificata -> "))
            modificare = str(input("modificarea propriu-zisa -> "))
            modificare_vanzare(librarie, id_vanzare, key, modificare)
        else:
            print("Optiune incorecta. Va rugam reincercati!")


if __name__ == '__main__':
    main()
