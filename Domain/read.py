import json


def creare_vanzare(librarie):
    """
    Functia creaza si adauga elementele unei vanzari de carte in lista de dictionare numita 'librarie'
    :param librarie: o lista de dictionare
    :return: aceeasi lista de dictionare modificata
    """
    cufarul_cu_comori = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "w")
    cufarul_cu_comori.close()
    print("Introduceti:")
    id = str(input("    -id-ul vanzarii: "))
    titlu = str(input("    -titlul cartii: "))
    gen = str(input("    -genul cartii: "))
    pret = str(input("    -pretul cartii: "))
    reducere = str(input("    -tipul reducerii clientului: "))
    librarie.append({'id_vanzare': id, 'titlu': titlu, 'genul': gen, 'pret': pret, 'reducere': reducere})
    cufarul_cu_comori = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r+")
    with open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r+") as convert_files:
        convert_files.write(json.dumps(librarie))
    cufarul_cu_comori.close()
    return librarie


def scoatem_din_cufar(librarie):
    with open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori") as cufarul_cu_comori:
        librarie = cufarul_cu_comori.read()
        librarie = json.loads(librarie)
    cufarul_cu_comori.close()


def bagam_in_cufar(librarie):
    cufarul_cu_comori = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r+")
    with open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori",
              "r+") as convert_files:
        convert_files.write(json.dumps(librarie))
    cufarul_cu_comori.close()


def get_id(librarie):
    return creare_vanzare(librarie['id_vanzare'])


def set_idcarte(librarie, modificare):
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
