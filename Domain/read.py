import ast
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
    vanzare = {'id_vanzare': id, 'titlu': titlu, 'genul': gen, 'pret': pret, 'reducere': reducere, 'pret redus': pret}
    librarie.append(vanzare)


def get_id(librarie):
    return librarie['id_vanzare']
def set_id(librarie, modificare):
    librarie['id'] = modificare


def get_titlu(librarie):
    return librarie['titlu']
def set_titlu(librarie, modificare):
    librarie['titlu'] = modificare


def get_gen(librarie):
    return librarie['genul']
def set_gen(librarie, modificare):
    librarie['genul'] = modificare


def get_pret(librarie):
    return librarie['pret']
def set_pret(librarie, modificare):
    librarie['pret'] = modificare


def get_reducere(librarie):
    return librarie['reducere']
def set_reducere(librarie, modificare):
    librarie['reducere'] = modificare

def get_pret_redus(librarie):
    return librarie['pret redus']
def set_pret_redus(librarie, modificare):
    librarie['pret redus'] = modificare
