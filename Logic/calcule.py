

def fifteen_percent(x):
    x = int(x)
    x = x - x * (15 / 100)
    return x


def ten_percent(x):
    x = int(x)
    x = x - x * (1 / 10)
    return x


def remove(txt, x):
    """
    Functia elimina caracterul sau caractere din parametrul x dintr-un string
    :param x: un sir de caractere
    :param txt:
    :return: sirul de caractere txt fara toate caractere din sirul x
    """
    return txt.replace(x, "")




