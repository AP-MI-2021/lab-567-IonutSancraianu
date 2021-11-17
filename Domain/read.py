

from Logic.calcule import remove


def creare_vanzare(librarie):
    """
    Functia creaza si adauga elementele unei vanzari de carte in lista de liste numita 'librarie'
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
        vanzare = [int(id_vanzare),  titlu,  gen, int(pret), reducere, int(pret)]  # [id: 0, titlu: 1, gen: 2, pret: 3,
        # reducere: 4, pret redus: 5]
        # pretul redus are aceeasi valoare ca si pretul intreg pana la apelarea functiei aplicare_reducere
        librarie.append(vanzare)
        return librarie
    except ValueError as ve:
        print(ve)


def get_id(vanzare):
    return vanzare[0]
def set_id(vanzare, modificare):
    vanzare[0] = modificare


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
    vanzare[3] = modificare


def get_reducere(vanzare):
    return vanzare[4]
def set_reducere(vanzare, modificare):
    vanzare[4] = str(modificare)


def get_pret_redus(vanzare):
    return vanzare[5]
def set_pret_redus(vanzare, modificare):
    vanzare[5] = modificare
