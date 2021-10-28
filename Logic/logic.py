import sys

from Domain.read import get_gen, get_pret


def fifteen_percent(x):
    x = int(x)
    x = x - x * (15 / 100)
    return x


def ten_percent(x):
    x = int(x)
    x = x - x * (1 / 10)
    return x


def minim(librarie, key):
    """
    Functia calculeaza valoarea minima dintr-un set de date dintr-un sir de dictionare, in functie de cheia din
    parametrul <key>
    :param librarie: o lista de dictionare
    :param key: cheia din setul de date date pentru care se calculeaza minimul
    :return: numar intreg, prin variabila <min>
    """
    mini = 1000000000
    for i in librarie:
        if get_gen(i) == key:
            if int(get_pret(i)) < mini:
                mini = int(get_pret(i))
    return mini


