import copy

from Domain.read import get_id, set_pret_redus, get_pret, get_reducere, get_pret_redus, get_titlu, set_gen
from Logic.calcule import ten_percent, fifteen_percent


def modificare_vanzare(librarie, id_vanzare, key, modificare):
    """
    Functia modifica un element al vanzarii alese prin parametrul id_vanzare, in functie de cheia din parametrul key,
    iar modificarea va fi stocata in parametrul modificare
    :param modificare: numar intreg sau sir de caractere
    :param librarie: lista de liste
    :param id_vanzare: numar intreg
    :param key: numar intreg
    """
    for i in librarie:
        if id_vanzare in i:
            i[key] = modificare
            break
    return librarie


def stergere_vanzare(librarie, id_vanzare):
    """
    Funtia sterge vanzarea cu id-ul specificat in al doilea parametru
    :param librarie: o lista de liste
    :param id_vanzare: un numar intreg
    """
    i = 0
    while i < len(librarie):
        if get_id(librarie[i]) == id_vanzare:
            del librarie[i]
            i = i - 1
            break
        i += 1
    return librarie


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
    :return:
    """
    for i in librarie:
        if get_titlu(i) == titlu:
            set_gen(i, modificare)
    return librarie


def undo(librarie, versiuni):
    """
    Functia restaureaza lista de liste librarie la versiunea precedenta ulimei
    :param librarie: o lista de liste
    :param versiuni: o lista de liste
    :return: o liste de liste
    """
    if len(versiuni) < 1:
        print("Nu se mai poate face undo.")
    elif len(versiuni) == 1:
        del versiuni[0]
    else:
        del versiuni[len(versiuni) - 1]
        librarie = copy.deepcopy(versiuni[len(versiuni) - 1])
    return librarie
