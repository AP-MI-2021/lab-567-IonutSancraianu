from Domain.read import get_reducere, get_pret, set_pret_redus, get_pret_redus, get_id, get_titlu, set_titlu, \
    get_gen
from Logic.logic import fifteen_percent, ten_percent, minim


def adaugare_vanzare(librarie):
    """
    Functia adauga o vanzare noua in lista de dictionare 'librarie'
    :param librarie: lista de dictionare
    :return: lista de dictionare modificata
    """
    id_vanzare = str(input("    -id-ul vanzarii: "))
    titlu = str(input("    -titlul cartii: "))
    gen = str(input("    -genul cartii: "))
    pret = str(input("    -pretul cartii: "))
    reducere = str(input("    -tipul reducerii clientului: "))
    vanzare = {'id_vanzare': id_vanzare, 'titlu': titlu, 'genul': gen, 'pret': pret,
               'reducere': reducere, 'pret redus': pret}
    librarie.append(vanzare)


def modificare_vanzare(librarie, id_vanzare, key, modificare):
    """
    Functia modifica un element al vanzarii alese prin parametrul id_vanzare, in functie de cheia din parametrul key,
    iar modificarea va fi stocata in parametrul modificare
    :param modificare: numar intreg sau sir de caractere
    :param librarie: lista de dictionare
    :param id_vanzare: numar intreg
    :param key: numar intreg sau sir de caractere
    """
    for i in librarie:
        if get_id(i) == id_vanzare:
            i[key] = str(modificare)
        break


def stergere_vanzare(librarie, id_vanzare):
    """
    Funtia sterge vanzarea cu id-ul specificat in al doilea parametru
    :param librarie: o lista de dictionare
    :param id_vanzare: un numar integ
    """
    i = 0
    while i < len(librarie):
        if get_id(librarie[i]) == id_vanzare:
            del librarie[i]
            i = i - 1
            break
        i += 1


def aplicare_reducere(librarie):
    """
    Functia aplica reducerea corespondeta tipului de reducere cuvenit, dictionarul contine si pretul initial al cartii,
    dar si pretul redus
    :param librarie: o lista de dictionare
    """
    for i in librarie:
        if get_pret(i) == get_pret_redus(i):
            if get_reducere(i) == "gold":
                set_pret_redus(i, fifteen_percent(get_pret(i)))
            elif get_reducere(i) == "silver":
                set_pret_redus(i, ten_percent(get_pret(i)))
        else:
            print("Pentru vanzarea " + str(get_id(i) + ", a fost aplicata o reducere."))


def modificare_gen(librarie):
    """
    Functia modifica genul cartii cu titul ales in variabila <titlu>, iar modificarea propriu-zisa este stocata
    in variabila <modificare>
    :param librarie:
    :return:
    """
    titlu = str(input("Titlul cartii al carei gen trebuie modificat: "))
    modificare = input("Introduceti modificarea propriu-zisa: ")
    for i in librarie:
        if get_titlu(i) == titlu:
            set_titlu(i, modificare)


def pret_minim_pt_fiecare_gen(librarie):
    """
    Functia calculeaza pretul minim pentru fiecare gen diferit din lista <librarie>
    :param: o lista de dictionare
    :return: Returneaza un tuple cu perechi de elemente, primul element este genul, iar urmatorul este pretul minim
    """
    gen_si_minim = []
    for i in librarie:
        poc = True
        for j in gen_si_minim:
            if get_gen(i) == j[0]:
                poc = False
        if poc:
            gen_si_minim.append((get_gen(i), minim(librarie, get_gen(i))))
    return gen_si_minim


def ordonare_dupa_pret(librarie):
    """
    Functia ordoneaza crescator vanzarile in functie de pret. Se foloseste metoda paharelor ca modalitate
    :param librarie: O lista de dictionare
    """
    for i in range(0, len(librarie) - 1):
        for j in range(i+1, len(librarie)):
            if librarie[i]['pret'] > librarie[j]['pret']:
                pahar = librarie[i]
                librarie[i] = librarie[j]
                librarie[j] = pahar


def titluri_distincte(librarie):
    """
    Functia afiseaza, pentru fiecare gen, numarul de titluri distincte
    :param librarie:
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


def afisare_vanzari(librarie):
    i = 0
    while i < len(librarie):
        print(librarie[i])
        i += 1
