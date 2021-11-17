# ACest modul il folosesc pentru testarea diferitelor functii sau a altor lucruri,
# A nu se lua in considerare ce e scris aici
from numpy.core.defchararray import isnumeric, isalnum, isalpha

from Logic.CRUD import aplicare_reducere
from Logic.functionality import afisare_vanzari

lst = [
        ["123", "ion", "actiune", "90", "gold", "90"],
        ["234", "idiotul", "deeper one", "123", "silver", "123"],
        ["345", "alchimistul", "psihologic", "78", "none", "78"],
        ["456", "minunea", "sad", "100", "silver", "100"]
    ]

afisare_vanzari(aplicare_reducere(lst))
