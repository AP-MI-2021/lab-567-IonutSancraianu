from Domain.functionality import afisare_vanzari, adaugare_vanzare, stergere_vanzare, modificare_vanzare, \
    aplicare_reducere, modificare_gen
from Domain.read import creare_vanzare


def main():
    librarie = []
    while True:
        print("Alegeti optiunea pe care o doriti: ")
        print("1 - Citirea primei vanzari.")
        print("2 - Afisarea tuturor vanzarilor")
        print("3 - Adaugarea unei vanzari noi.")
        print("4 - Stergerea unei vanzari existente.")
        print("5 - Modificarea unei liste deja existente.")
        print("6 - Aplicarea discountului in functie de tipul de reducere si afisarea noului pret "
              "pentru fiecare vanzare")
        print("7 - Modificarea genului cartii pentru un titlu dat")
        print("u - intoarcerea listei de vanzari la versiunea precedenta ultimei modificari")
        print("x - Oprirea programului")
        optiune = str(input("optiune -> "))
        if optiune == "1":
            creare_vanzare(librarie)
        elif optiune == "2":
            afisare_vanzari(librarie)
        elif optiune == "3":
            adaugare_vanzare(librarie)
        elif optiune == "x":
            print("Exiting...")
            break
        elif optiune == "4":
            id_vanzare = input("Id-ul vanzarii care trebuie eliminata -> ")
            stergere_vanzare(librarie, id_vanzare)
        elif optiune == "5":
            id_vanzare = input("Id-ul vanzarii care trebuie modificata -> ")
            key = str(input("elementul vanzarii care trebuie modificata -> "))
            modificare = str(input("modificarea propriu-zisa -> "))
            modificare_vanzare(librarie, id_vanzare, key, modificare)
        elif optiune == "6":
            aplicare_reducere(librarie)
        elif optiune == "7":
            modificare_gen(librarie)
        else:
            print("Optiune incorecta. Va rugam reincercati!")


if __name__ == '__main__':
    main()
