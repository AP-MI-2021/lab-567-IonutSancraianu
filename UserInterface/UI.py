import re
from Logic.CRUD import redo, adaugare_vanzare, modificare_vanzare, aplicare_reducere, undo, modificare_gen, \
    stergere_vanzare
from Logic.functionality import titluri_distincte, salvare_versiune_redo, salvare_versiune_undo, afisare_vanzari, \
    pret_minim_pt_fiecare_gen, ordonare_dupa_pret
from Tests.tests import all_tests


def main():
    versiuni_undo = []
    librarie = []
    versiuni_redo = []
    start = False
    all_tests()
    print()
    while True:
        print("Alegeti optiunea pe care o doriti: ")
        print("1 - Citirea primei vanzari. ")
        print("a - Afisarea tuturor vanzarilor. ")
        print("2 - Adaugarea unei vanzari noi.")
        print("3 - Stergerea unei vanzari existente.")
        print("4 - Modificarea unei liste deja existente.")
        print("5 - Aplicarea discountului in functie de tipul de reducere si afisarea noului pret "
              "pentru fiecare vanzare. ")
        print("6 - Modificarea genului cartii pentru un titlu dat. ")
        print("7 - Determinarea pretului minim pentru fiecare gen. ")
        print("8 - Ordonarea crescator dupa pret. ")
        print("9 - Afișarea numărului de titluri distincte pentru fiecare gen. ")
        print("u - Undo. ")
        print("r - Redo")
        print("x - Oprirea programului. ")
        optiune = str(input("optiune -> "))
        if optiune == "1":
            librarie = adaugare_vanzare(librarie)
            salvare_versiune_undo(librarie, versiuni_undo)
            start = False
        elif optiune == "a":
            afisare_vanzari(librarie)
        elif optiune == "2":
            librarie = adaugare_vanzare(librarie)
            afisare_vanzari(librarie)
            salvare_versiune_undo(librarie, versiuni_undo)
            start = False
        elif optiune == "x":
            print("Exiting...")
            break
        elif optiune == "3":
            librarie = stergere_vanzare(librarie, id_vanzare=input("Id-ul vanzarii care trebuie eliminata -> "))
            afisare_vanzari(librarie)
            salvare_versiune_undo(librarie, versiuni_undo)
            start = False
        elif optiune == "4":
            id_vanzare = input("Id-ul vanzarii care trebuie modificata -> ")
            key = input("Elementul vanzarii care trebuie modificata "
                        "([id_vanzare: 0, titlu: 1, gen: 2, pret: 3,reducere: 4]) -> ")
            modificare = input("modificarea propriu-zisa -> ")
            librarie = modificare_vanzare(librarie, id_vanzare, key, modificare)
            afisare_vanzari(librarie)
            salvare_versiune_undo(librarie, versiuni_undo)
            start = False
        elif optiune == "5":
            librarie = aplicare_reducere(librarie)
            afisare_vanzari(librarie)
            salvare_versiune_undo(librarie, versiuni_undo)
            start = False
        elif optiune == "6":
            titlu = str(input("Introduceti titlul cartii al carei gen trebuie modificat -> "))
            modificare = str(input("Introduceti modificarea -> "))
            librarie = modificare_gen(librarie, titlu, modificare)
            afisare_vanzari(librarie)
            salvare_versiune_undo(librarie, versiuni_undo)
            start = False
        elif optiune == "7":
            print(pret_minim_pt_fiecare_gen(librarie))
        elif optiune == "8":
            print(ordonare_dupa_pret(librarie))
        elif optiune == "9":
            titluri_distincte(librarie)
        elif optiune == "u":
            if len(versiuni_undo) != 0:
                salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
            librarie = undo(librarie, versiuni_undo)
            afisare_vanzari(librarie)
            start = True
        elif optiune == "r":
            librarie = redo(librarie, versiuni_redo, start)
            salvare_versiune_undo(librarie, versiuni_undo)
            afisare_vanzari(librarie)
        else:
            print("Optiune incorecta. Va rugam reincercati!")


def command_console():
    print("Lista comenzilor:")
    print("    - read -> citirea primei vanzari;")
    print("    - showall -> afisarea tuturor vanzarilor;")
    print("    - delete -> stergerea unei anume vanzari;")
    print("    - add -> adaugarea unei vanzari;")
    print("    - sale -> Aplicarea discountului in functie de tipul de reducere;")
    print("Separatori luati in considerare: , . ;")
    print("OBS: Orice alta comanda decat cele descrise mai sus rezulta in oprirea programului.")
    str_comenzi = str(input("introduceti sirul de comenzi: "))
    lista_comenzi = re.split(', |. |; | ', str_comenzi)
    librarie2 = []
    for i in lista_comenzi:
        if i == "read":
            librarie2 = adaugare_vanzare(librarie2)
        elif i == "showall":
            afisare_vanzari(librarie2)
        elif i == "delete":
            librarie2 = stergere_vanzare(librarie2,
                                         id_vanzare=(input("introduceti id-ul vanzarii care trebuie stearsa: ")))
        elif i == "add":
            librarie2 = adaugare_vanzare(librarie2)
        elif i == "sale":
            librarie2 = aplicare_reducere(librarie2)
        else:
            print("Comanda introdusa este incorecta." + "\n" + "Exiting...")
            break


if __name__ == '__main__':
    while True:
        terminal = str(input("Introduceti 1 daca doriti sa folositi prima interfata (main) " + "\n" +
                             ",2 daca doriti sa folositi interfata 2 (command terminal) " + "\n" +
                             "sau x daca doriti sa opriti programul -> "))
        if terminal == "1":
            main()
            break
        elif terminal == "2":
            command_console()
            break
        elif terminal == "x":
            print("Exiting...")
            break
        else:
            print("Terminal gresit, Reintroduceti!")
