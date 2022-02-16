from Logic.calcule import remove


def creare_vanzare(id_vanzare, titlu, gen, pret, tipul_reducerii):
    """
    Functia genereaza o lista cu detaliile unei vanzari de carte,
     din cadrul unei librarii
    :param id_vanzare: un numar natural
    :param titlu: un sir de caractere
    :param gen: un sir de caractere
    :param pret: un numar intreg sau rational
    :param tipul_reducerii: <gold>, <silver> sau <none>
    :return: o lista ce contine elementele de mai sus
    """

    if not id_vanzare.isnumeric():
        raise ValueError("Id-ul vanzarii trebuie sa fie un numar intreg.")
    if not remove(titlu, " ").isalnum():
        raise ValueError("Titlul trebuie sa fie un cuvant (sau mai multe).")
    if not remove(gen, " ").isalnum():
        raise ValueError("Genul cartii trebuie sa fie un cuvant "
                         "(sau mai multe).")
    if not remove(pret, ".").isnumeric():
        raise ValueError("Pretul vanzarii trebuie sa fie un numar.")
    if not (tipul_reducerii in ["gold", "silver", "none"]):
        raise ValueError("Tipul reducerii trebuie sa fie gold, silver sau none")
    # [id: 0, titlu: 1, gen: 2, pret: 3, reducere: 4, pret redus: 5]
    # pretul redus are aceeasi valoare ca si pretul intreg pana la apelarea
    # functiei aplicare_reducere
    return [int(id_vanzare), titlu, gen, float(pret), tipul_reducerii,
            int(pret)]


def get_id(vanzare):
    return vanzare[0]


def set_id(vanzare, modificare):
    vanzare[0] = int(modificare)


def get_titlu(vanzare):
    return vanzare[1]


def set_titlu(vanzare, modificare):
    vanzare[1] = str(modificare)


def get_gen(vanzare):
    return vanzare[2]


def set_gen(vanzare, modificare):
    vanzare[2] = str(modificare)


def get_pret(vanzare):
    return vanzare[3]


def set_pret(vanzare, modificare):
    vanzare[3] = int(modificare)


def get_reducere(vanzare):
    return vanzare[4]


def set_reducere(vanzare, modificare):
    vanzare[4] = str(modificare)


def get_pret_redus(vanzare):
    return vanzare[5]


def set_pret_redus(vanzare, modificare):
    vanzare[5] = modificare
