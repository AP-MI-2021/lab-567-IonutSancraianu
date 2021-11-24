# Acest modul il folosesc pentru testarea diferitelor functii sau a altor lucruri,
# A nu se lua in considerare ce e scris aici
from Logic.functionality import titluri_distincte

lst = [
        ["3465", "ion", "actiune", "9", "gold", "9"],
        ["35677", "wasd", "romantic", "67", "gold", "67"],
        ["2345", "idiotul", "actiune", "15", "gold", "15"],
        ["235", "qwe", "romantic", "38", "gold", "38"],
        ["123", "rambo", "actiune", "40", "gold", "40"],
        ["124", "qwerty", "dezvoltare", "9", "gold", "9"]
    ]

titluri_distincte(lst)
