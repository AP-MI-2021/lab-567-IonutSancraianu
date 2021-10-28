from Domain.functionality import pret_minim_pt_fiecare_gen

dic = [{'genul': "rosu", 'pret': 123},
       {'genul': "rosu", 'pret': 43},
       {'genul': "albastru", 'pret': 100},
       {'genul': "albastru", 'pret': 200},
       {'genul': "mov", 'pret': 2},
       {'genul': "mov", 'pret': 1},
       {'genul': "albastru", 'pret': 50}]

print(pret_minim_pt_fiecare_gen(dic))