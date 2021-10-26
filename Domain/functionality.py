from Domain.read import bagam_in_cufar


def afisare_vanzari(librarie):
    for i in librarie:
        print(i)


def adaugare_vanzare(librarie):
    """
    Functia adauga o vanzare noua in lista de dictionare 'librarie'
    :param librarie: lista de dictionare
    :return: lista de dictionare modificata
    """
    id_vanzare = str(input("    -id-ul vanzarii"))
    titlu = str(input("    -titlul cartii: "))
    gen = str(input("    -genul cartii: "))
    pret = str(input("    -pretul cartii: "))
    reducere = str(input("    -tipul reducerii clientului: "))
    librarie.append({'id_vanzare': id_vanzare, 'titlu': titlu, 'genul': gen, 'pret': pret, 'reducere': reducere})


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
        if i['id_vanzare'] == id_vanzare:
            i[key] = str(modificare)
        break
    bagam_in_cufar(librarie)


def stergere_vanzare(librarie, id_vanzare):
    """
    Funtia sterge vanzarea cu id-ul specificat in al doilea parametru
    :param librarie: o lista de dictionare
    :param id_vanzare: un numar integ
    """
    for i in librarie:
        if i['id_vanzare'] == id_vanzare:
            del i
        break
