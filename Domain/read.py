import json
import os


def creare_vanzare(librarie):
    """
    Functia creaza si adauga elementele unei vanzari de carte in lista de dictionare numita 'librarie'
    :param librarie: o lista de dictionare
    :return: aceeasi lista de dictionare modificata
    """
    print("Introduceti:")
    id = str(input("    -id-ul vanzarii: "))
    titlu = str(input("    -titlul cartii: "))
    gen = str(input("    -genul cartii: "))
    pret = str(input("    -pretul cartii: "))
    reducere = str(input("    -tipul reducerii clientului: "))
    vanzare = {'id_vanzare': id, 'titlu': titlu, 'genul': gen, 'pret': pret, 'reducere': reducere}
    librarie.append(vanzare)
    # cufarul_cu_comori = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r+")
    # cufarul_cu_comori.write(json.dumps(librarie))


def scoatem_din_cufar(librarie):
    """
    Functia citeste o lista de dictionare din fisierul "cufarul cu comori"
    :param librarie: lista de dictionare care primeste valorile din fisier
    """
    with open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r") \
            as cufarul_cu_comori:
        librarie = json.loads(cufarul_cu_comori)
    cufarul_cu_comori.close()


def bagam_in_cufar(librarie):
    """
    Functia scrie in fisierul "cufarul cu comori" datele din lista de dictionare librarie
    :param librarie: o lista de dictionare
    :return:
    """
    cufarul_cu_comori = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "w")
    cufarul_cu_comori.write(json.dumps(str(librarie)))
    cufarul_cu_comori.close()


def deschide_cufar():
    cufarul_cu_comori = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r+")


def inchide_cufar():
    cufarul_cu_comori = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r+")
    cufarul_cu_comori.close()


def get_id(librarie):
    return creare_vanzare(librarie['id_vanzare'])
def set_id(librarie, modificare):
    librarie['id'] = modificare


def get_titlu(librarie):
    return creare_vanzare(librarie['titlu'])
def set_titlu(librarie, modificare):
    librarie['titlu'] = modificare


def get_gen(librarie):
    return creare_vanzare(librarie['genul'])
def set_gen(librarie, modificare):
    librarie['genul'] = modificare


def get_pret(librarie):
    return creare_vanzare(librarie['pret'])
def set_pret(librarie, modificare):
    librarie['pret'] = modificare


def get_reducere(librarie):
    return creare_vanzare(librarie['reducere'])
def set_reducere(librarie, modificare):
    librarie['reducere'] = modificare
