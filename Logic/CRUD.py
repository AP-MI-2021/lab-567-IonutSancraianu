import copy

from pandas.core.computation.ops import isnumeric

from Domain.read import get_id, set_pret_redus, get_pret, get_reducere, get_pret_redus, get_titlu, set_gen, set_id, \
    creare_vanzare
from Logic.calcule import ten_percent, fifteen_percent, remove


def adaugare_vanzare(librarie):
    """
    Functia creaza elementele unei vanzari de carte
    :param librarie: o lista de dictionare
    :return: aceeasi lista de dictionare modificata
    """
    try:
        print("Introduceti:")
        id_vanzare = input("    -id-ul vanzarii: ")
        if not id_vanzare.isnumeric():
            raise ValueError("Id-ul vanzarii trebuie sa fie un numar intreg.")
        if librarie is not None:
            for i in librarie:
                if id_vanzare == get_id(i):
                    raise ValueError("Acest id exista deja, va rugam introduceti un id valid. ")
        titlu = str(input("    -titlul cartii: "))
        if not remove(titlu, " ").isalnum():
            raise ValueError("Titlul trebuie sa fie un cuvant (sau mai multe).")
        gen = str(input("    -genul cartii: "))
        if not remove(gen, " ").isalnum():
            raise ValueError("Genul cartii trebuie sa fie un cuvant (sau mai multe).")
        pret = str(input("    -pretul cartii: "))
        if not remove(pret, ".").isnumeric():
            raise ValueError("Pretul vanzarii trebuie sa fie un numar.")
        reducere = str(input("    -tipul reducerii clientului: "))
        if not (reducere in ["gold", "silver", "none"]):
            raise ValueError("Tipul reducerii trebuie sa fie gold, silver sau none")
        vanzare = creare_vanzare(int(id_vanzare), titlu, gen, float(pret), reducere)
        # [id: 0, titlu: 1, gen: 2, pret: 3, reducere: 4, pret redus: 5]
        # pretul redus are aceeasi valoare ca si pretul intreg pana la apelarea functiei aplicare_reducere
        librarie.append(vanzare)
        return librarie
    except ValueError as ve:
        print(ve)


def modificare_vanzare(librarie, id_vanzare, key, modificare):
    """
    Functia modifica un element al vanzarii alese prin parametrul id_vanzare, in functie de cheia din parametrul key,
    iar modificarea va fi stocata in parametrul modificare
    :param modificare: numar intreg sau sir de caractere
    :param librarie: lista de liste
    :param id_vanzare: numar intreg
    :param key: numar intreg
    """
    try:
        if not id_vanzare.isnumeric():
            raise ValueError("Id-ul vanzarii trebuie sa fie un numar intreg.")
        if not key.isnumeric():
            raise ValueError("Key reprezinta indexul modificarii si trebuie sa fie un numar natural, de la 0 la 4.")
        elif int(key) < 0 or int(key) > 4:
            raise ValueError("Elementul vanzarii reprezinta indexul modificarii in lista"
                             " si trebuie sa fie un numar natural, de la 0 la 4.")
        elif int(key) == 3:
            if not isnumeric(remove(modificare, ".")):
                raise ValueError("Modificarea pentru pretul vanzarii trebuie sa fie un numar natural.")
        elif int(key) != 3 and int(key) != 0:
            if not remove(modificare, " ").isalnum():
                raise ValueError("Modificarea elementulul selectat al vanzarii trebuie sa fie un cuvant "
                                 "(sau mai multe)")
        for i in librarie:
            if id_vanzare == get_id(i):
                if int(key) == 0:
                    if not modificare.isnumeric():
                        raise ValueError("Modificarea pentru id-ul vanzarii trebuie sa fie un numar natural.")
                    for j in librarie:
                        if modificare == get_id(j):
                            raise ValueError("Acest id exista deja, "
                                             "va rugam introduceti o modificare valida pentru id-ul vanzarii. ")
                    set_id(i, modificare)
                else:
                    i[int(key)] = modificare
                    break
        return librarie
    except ValueError as ve:
        print(ve)

def stergere_vanzare(librarie, id_vanzare):
    """
    Funtia sterge vanzarea cu id-ul specificat in al doilea parametru
    :param librarie: o lista de liste
    :param id_vanzare: un numar intreg
    """
    try:
        if not id_vanzare.isnumeric():
            raise ValueError("Id-ul vanzarii trebuie sa fie un numar.")
        i = 0
        while i < len(librarie):
            if get_id(librarie[i]) == id_vanzare:
                del librarie[i]
                i = i - 1
                break
            i += 1
        return librarie
    except ValueError as ve:
        print(ve)


def aplicare_reducere(librarie):
    """
    Functia aplica reducerea corespondeta tipului de reducere cuvenit, dictionarul contine si pretul initial al cartii,
    dar si pretul redus
    :param librarie: o lista de liste

    """
    for i in librarie:
        if get_pret(i) == get_pret_redus(i):
            if get_reducere(i) == "gold":
                set_pret_redus(i, fifteen_percent(get_pret(i)))
            elif get_reducere(i) == "silver":
                set_pret_redus(i, ten_percent(get_pret(i)))
            elif get_reducere(i) == "none":
                set_pret_redus(i, int(get_pret(i)))
        else:
            print("Pentru vanzarea " + get_id(i) + ", a fost deja aplicata o reducere.")
    return librarie


def modificare_gen(librarie, titlu, modificare):
    """
    Functia modifica genul cartii cu titul ales in variabila <titlu>, iar modificarea propriu-zisa este stocata
    in variabila <modificare>
    :param modificare: un sir de caractere
    :param titlu: un sir de caractere
    :param librarie: lista de liste
    :return: lista de liste modificata
    """
    try:
        if not remove(titlu, " ").isalnum():
            raise ValueError("Titlul trebuie sa fie un cuvant.")

        for i in librarie:
            if get_titlu(i) == titlu:
                set_gen(i, modificare)
        return librarie
    except ValueError as ve:
        print(ve)


def undo(librarie, versiuni_undo):
    """
    Functia restaureaza lista de liste librarie la versiunea precedenta ulimei
    :param librarie: o lista de liste
    :param versiuni_undo: o lista de liste
    :return: o liste de liste
    """
    if len(versiuni_undo) < 1:
        print("Nu se mai poate face undo.")
    elif len(versiuni_undo) == 1:
        del versiuni_undo[0]
        del librarie[0]
    else:
        del versiuni_undo[len(versiuni_undo) - 1]
        librarie = copy.deepcopy(versiuni_undo[len(versiuni_undo) - 1])
    return librarie


def redo(librarie, versiuni_redo):
    """
    Functia restaureaza lista de liste librarie la versoinea precedenta ultimului undo
    :param librarie:
    :param versiuni_redo:
    :return:
    """
    del versiuni_redo[len(versiuni_redo) - 1]
    librarie = copy.deepcopy(versiuni_redo[len(versiuni_redo) - 1])
    return librarie
