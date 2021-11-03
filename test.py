
# Acest modul nu reprezinta o parte oficiala din proiect, aici testez diferite functii sau altele

import re

from Domain.read import get_gen

dic = [{'genul': "rosu", 'titlu': "ion"},
       {'genul': "rosu", 'titlu': "idiotul"},
       {'genul': "albastru", 'titlu': "actiune"},
       {'genul': "albastru", 'titlu': "romantic"},
       {'genul': "mov", 'titlu': "ion"},
       {'genul': "mov", 'titlu': "wasd"},
       {'genul': "albastru", 'titlu': "actiune"},
       {'genul': "rosu", 'titlu': "ion"}]

lst = [0, 1, 2, 3, 4, 5]

print(get_gen(lst))
