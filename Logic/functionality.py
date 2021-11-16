import copy

from Domain.read import get_gen, get_titlu, get_pret
from Logic.calcule import minim


def pret_minim_pt_fiecare_gen(librarie):
    """
    Functia calculeaza pretul minim pentru fiecare gen diferit din lista <librarie>
    :param: o lista de liste
    :return: Returneaza o lista de liste cu perechi de elemente, primul element este genul,
    iar urmatorul este pretul minim
    """
    gen_si_minim = []
    for i in librarie:
        poc = True
        for j in gen_si_minim:
            if get_gen(i) == j[0]:
                poc = False
        if poc:
            genu = get_gen(i)
            gen_si_minim.append((genu, minim(librarie, genu)))
    print(gen_si_minim)


def titluri_distincte(librarie):
    """
    Functia afiseaza, pentru fiecare gen, numarul de titluri distincte
    :param librarie: lista de liste
    :return:
    """
    copy_vanzare = librarie.copy()
    i = 0
    limit = len(copy_vanzare)
    while i < limit - 1:
        con = 1
        j = i + 1
        while j < len(copy_vanzare):
            if get_gen(copy_vanzare[i]) == get_gen(copy_vanzare[j]):
                if get_titlu(copy_vanzare[i]) == get_titlu(copy_vanzare[j]):
                    del copy_vanzare[j]
                    limit -= 1
                    j -= 1
            j += 1
        x = i + 1
        while x < len(copy_vanzare):
            if get_gen(copy_vanzare[i]) == get_gen(copy_vanzare[x]):
                con += 1
                del copy_vanzare[x]
                limit -= 1
                x -= 1
            x += 1
        print("Genul " + get_gen(copy_vanzare[i]) + " contine " + str(con) + " titluri distincte" + "\n")
        i += 1
    afisare_vanzari(librarie)


def ordonare_dupa_pret(librarie):
    """
    Functia ordoneaza crescator vanzarile in functie de pret. Se foloseste metoda paharelor ca modalitate
    :param librarie: O lista de liste

    """
    librarie2 = librarie.copy()
    for i in range(0, len(librarie2) - 1):
        for j in range(i+1, len(librarie2)):
            if get_pret(librarie2[i]) > get_pret(librarie2[j]):
                pahar = librarie2[i]
                librarie2[i] = librarie2[j]
                librarie2[j] = pahar
    print(librarie2)


def salvare_versiune(librarie, versiuni):
    """
    Functia salveaza o copie a listei de liste din variabila librarie in lista versiuni
    :param librarie: o lista de liste
    :param versiuni: o lista
    """
    versiune = copy.deepcopy(librarie)
    versiuni.append(versiune)


def afisare_vanzari(librarie):
    i = 0
    while i < len(librarie):
        print(librarie[i])
        i += 1
    print("\n")
