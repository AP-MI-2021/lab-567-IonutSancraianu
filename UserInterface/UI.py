from Domain.functionality import afisare_vanzari, adaugare_vanzare
from Domain.read import creare_vanzare


def main():
    librarie = []
    librarie = creare_vanzare(librarie)
    afisare_vanzari(librarie)
    adaugare_vanzare(librarie, 2341)
    afisare_vanzari(librarie)


if __name__ == '__main__':
    main()