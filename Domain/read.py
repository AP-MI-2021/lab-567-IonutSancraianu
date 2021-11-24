

def creare_vanzare(id_vanzare, titlu, gen, pret, tipul_reducerii):
    """
    Functia genereaza o lista cu detaliile unei vanzari de carte, din cadrul unei librarii
    :param id_vanzare: un numar natural
    :param titlu: un sir de caractere
    :param gen: un sir de caractere
    :param pret: un numar intreg sau rational
    :param tipul_reducerii: <gold>, <silver> sau <none>
    :return: o lista ce contine elementele de mai sus
    """
    return [id_vanzare, titlu, gen, pret, tipul_reducerii, int(pret)]


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
