from Logic.logic import *


def creare_vanzare(librarie):
    """
    Functia creaza si adauga elementele unei vanzari de carte in lista de dictionare numita 'librarie'
    :param librarie: o lista de dictionare
    :return: aceeasi lista de dictionare modificata
    """
    print("Introduceti:")
    while True:
        id_vanzare = str(input("    -id-ul vanzarii: "))
        if not verificare_apartenenta(librarie, id_vanzare):
            break
        else:
            print("Acest id exista deja, va rugam introduceti un id valid. ")
    titlu = str(input("    -titlul cartii: "))
    gen = str(input("    -genul cartii: "))
    pret = str(input("    -pretul cartii: "))
    reducere = str(input("    -tipul reducerii clientului: "))
    vanzare = [id_vanzare,  titlu,  gen, pret, reducere, pret]  # [id: 0, titlu: 1, gen: 2, pret: 3,
    # reducere: 4, pret redus: 5]
    librarie.append(vanzare)


def get_id(vanzare):
    return vanzare[0]
def set_id(vanzare, modificare):
    vanzare[0] = modificare


def get_titlu(vanzare):
    return vanzare[1]
def set_titlu(vanzare, modificare):
    vanzare[1] = modificare


def get_gen(vanzare):
    return vanzare[2]
def set_gen(vanzare, modificare):
    vanzare[2] = modificare


def get_pret(vanzare):
    return vanzare[3]
def set_pret(vanzare, modificare):
    vanzare[3] = modificare


def get_reducere(vanzare):
    return vanzare[4]
def set_reducere(vanzare, modificare):
    vanzare[4] = modificare


def get_pret_redus(vanzare):
    return vanzare[5]
def set_pret_redus(vanzare, modificare):
    vanzare[5] = modificare
