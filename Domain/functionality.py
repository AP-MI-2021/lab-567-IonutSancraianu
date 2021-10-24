from Domain.read import creare_vanzare


def afisare_vanzari(librarie):
    for i in librarie:
        print(i)


def adaugare_vanzare(librarie, id_vanzare):
    """
    Functia adauga o vanzare noua in lista de dictionare 'librarie', avand id-ul vanzarii noi ca si al doilea parametru
    :param librarie: lista de dictionare
    :param id_vanzare: un numar natural
    :return: lista de dictionare modificata
    """
    titlu = input("     -titlul cartii: ")
    gen = input("    -genul cartii: ")
    pret = input("   -pretul cartii: ")
    reducere = input("   -tipul reducerii clientului: ")
    librarie.append({'id_vanzare': id_vanzare, 'titlu': titlu, 'genul': gen, 'pret': pret, 'reducere': reducere})
    return librarie


