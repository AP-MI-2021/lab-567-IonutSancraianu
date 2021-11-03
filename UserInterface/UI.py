import re
from Domain.functionality import *
from Domain.read import creare_vanzare


def main():
    librarie = []
    while True:
        print("Alegeti optiunea pe care o doriti: ")
        print("1 - Citirea primei vanzari. ")
        print("2 - Afisarea tuturor vanzarilor. ")
        print("3 - Adaugarea unei vanzari noi.")
        print("4 - Stergerea unei vanzari existente.")
        print("5 - Modificarea unei liste deja existente.")
        print("6 - Aplicarea discountului in functie de tipul de reducere si afisarea noului pret "
              "pentru fiecare vanzare. ")
        print("7 - Modificarea genului cartii pentru un titlu dat. ")
        print("8 - Determinarea pretului minim pentru fiecare gen. ")
        print("9 - Ordonarea crescator dupa pret. ")
        print("10 - Afișarea numărului de titluri distincte pentru fiecare gen. ")
        print("u - intoarcerea listei de vanzari la versiunea precedenta ultimei modificari. (nu e disponibil inca) ")
        print("x - Oprirea programului. ")
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
            stergere_vanzare(librarie, id_vanzare=input("Id-ul vanzarii care trebuie eliminata -> "))
        elif optiune == "5":
            id_vanzare = input("Id-ul vanzarii care trebuie modificata -> ")
            key = str(input("elementul vanzarii care trebuie modificata "
                            "([id_vanzare: 0, titlu: 1, gen: 2, pret: 3,reducere: 4]) -> "))
            modificare = str(input("modificarea propriu-zisa -> "))
            modificare_vanzare(librarie, id_vanzare, key, modificare)
        elif optiune == "6":
            aplicare_reducere(librarie)
        elif optiune == "7":
            modificare_gen(librarie)
        elif optiune == "8":
            pret_minim_pt_fiecare_gen(librarie)
        elif optiune == "9":
            ordonare_dupa_pret(librarie)
        elif optiune == "10":
            titluri_distincte(librarie)
        else:
            print("Optiune incorecta. Va rugam reincercati!")


def command_console():
    # Separatori luati in considerare: , . ;
    print("Lista comenzilor:")
    print("    - read -> citirea primei vanzari;")
    print("    - showall -> afisarea tuturor vanzarilor;")
    print("    - delete -> stergerea unei anume vanzari;")
    print("    - add -> adaugarea unei vanzari;")
    print("    - sale -> Aplicarea discountului in functie de tipul de reducere;")
    print("OBS: Orice alta comanda decat cele descrise mai sus rezulta in oprirea programului.")
    str_comenzi = str(input("introduceti sirul de comenzi: "))
    lista_comenzi = re.split(', |. |;', str_comenzi)
    librarie2 = []
    for i in lista_comenzi:
        if i == "read":
            creare_vanzare(librarie2)
        elif i == "showall":
            afisare_vanzari(librarie2)
        elif i == "delete":
            stergere_vanzare(librarie2, id_vanzare=(input("introduceti id-ul vanzarii care trebuie stearsa: ")))
        elif i == "add":
            adaugare_vanzare(librarie2)
        elif i == "sale":
            aplicare_reducere(librarie2)
        else:
            print("Comanda introdusa este incorecta." + "\n" + "Exiting...")
            break


if __name__ == '__main__':
    while True:
        terminal = str(input("Introduceti 1 daca doriti sa folositi prima interfata (main) "
                             "sau 2 daca doriti sa folositi interfata 2 (command terminal) -> "))
        if terminal == "1":
            main()
            break
        elif terminal == "2":
            command_console()
            break
        else:
            print("Terminal gresit, Reintroduceti!")
