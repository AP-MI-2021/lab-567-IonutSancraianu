import copy

from Domain.read import get_gen, get_titlu, get_pret, get_pret_redus


def pret_minim_pt_fiecare_gen(librarie):
    """
    Functia afiseaza pretul minim pentru fiecare gen diferit din lista
    <librarie>
    :param: o lista de liste
    :return: Returneaza o lista de liste cu perechi de elemente,
     primul element este genul cartii,
    iar urmatorul element este pretul minim
    """
    # daca reducerea a fost aplicata, algoritul va tine cont de pretul redus
    gen_si_minim = []
    for i in librarie:
        poc = True
        for j in gen_si_minim:
            if get_gen(i) == j[0]:
                poc = False
        if poc:
            genu = get_gen(i)
            gen_si_minim.append((genu, minim(librarie, genu)))
    return gen_si_minim


def minim(librarie, key):
    """
    Functia calculeaza pretul minim, din toate vanzarile,
    pentru un anume gen de carte, din parametrul <key>
    :param librarie: o lista de liste
    :param key: sir de caractere
    :return: numar intreg, prin variabila <mini>
    """
    mini = 9999999999
    for i in librarie:
        if get_gen(i) == key:
            if get_pret(i) == get_pret_redus(i):
                if int(get_pret(i)) < mini:
                    mini = int(get_pret(i))
                else:
                    if int(get_pret_redus(i)) < mini:
                        mini = int(get_pret_redus(i))
    return mini


def titluri_distincte(librarie):
    """
    Functia afiseaza, pentru fiecare gen, numarul de titluri distincte
    :param librarie: lista de liste
    :return:
    """
    copy_vanzare = librarie.copy()
    i = 0
    limit = len(copy_vanzare)
    con_ult = 1
    while i < limit - 1:
        con = 1
        j = i + 1
        while j < limit:
            if get_gen(copy_vanzare[i]) == get_gen(copy_vanzare[j]):
                if get_titlu(copy_vanzare[i]) == get_titlu(copy_vanzare[j]):
                    del copy_vanzare[j]
                    limit -= 1
                    j -= 1
                    i -= 1
            j += 1
        x = i + 1
        while x < limit:
            if get_gen(copy_vanzare[i]) == get_gen(copy_vanzare[x]):
                if x == limit - 1:
                    con_ult += 1
                con += 1
                del copy_vanzare[x]
                limit -= 1
                x -= 1
            x += 1
        print("Genul " + get_gen(copy_vanzare[i]) + " contine " +
              str(con) + " titluri distincte" + "\n")
        i += 1
    if con_ult == 1:
        print("Genul " + get_gen(librarie[-1]) + " contine " +
              str(con_ult) + " titluri distincte" + "\n")


def ordonare_dupa_pret(librarie):
    """
    Functia ordoneaza crescator vanzarile in functie de pret.
     Se foloseste metoda paharelor ca modalitate
    :param librarie: O lista de liste

    """
    librarie2 = librarie.copy()
    for i in range(0, len(librarie2) - 1):
        for j in range(i+1, len(librarie2)):
            if int(get_pret(librarie2[i])) > int(get_pret(librarie2[j])):
                pahar = librarie2[i]
                librarie2[i] = librarie2[j]
                librarie2[j] = pahar
    return librarie2


def salvare_versiune_undo(librarie, versiuni_undo):
    """
    Functia salveaza o copie a listei de liste din variabila
     librarie in lista versiuni_undo
    :param librarie: o lista de liste
    :param versiuni_undo: o lista
    """
    if versiuni_undo:
        if librarie != versiuni_undo[len(versiuni_undo) - 1]:
            versiune = copy.deepcopy(librarie)
            versiuni_undo.append(versiune)
    else:
        versiune = copy.deepcopy(librarie)
        versiuni_undo.append(versiune)


def salvare_versiune_redo(librarie, versiuni_redo):
    """
    Funcntia salveaza o copie a listei de liste din variabila
    librariia in lista versiuni_redo
    :param librarie: o lista de lista
    :param versiuni_redo: o lista
    """
    if versiuni_redo:
        if librarie != versiuni_redo[len(versiuni_redo) - 1]:
            versiune = copy.deepcopy(librarie)
            versiuni_redo.append(versiune)
    else:
        versiune = copy.deepcopy(librarie)
        versiuni_redo.append(versiune)


def afisare_vanzari(librarie):
    print()
    for i in librarie:
        print(i)
    print()
