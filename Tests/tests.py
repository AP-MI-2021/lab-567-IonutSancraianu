from Logic.CRUD import modificare_vanzare, stergere_vanzare, aplicare_reducere, modificare_gen, undo, redo
from Logic.functionality import salvare_versiune_undo, pret_minim_pt_fiecare_gen, ordonare_dupa_pret, minim, \
    salvare_versiune_redo


# [id: 0, titlu: 1, gen: 2, pret: 3, reducere: 4, pret redus: 5] -> legenda cu indexarea elementelor
def test_modificare_vanzare():
    lst = [
        [123, "ion", "actiune", "90", "gold", "90"],
        [234, "idiotul", "deeper one", "123", "silver", "123"],
        [345, "alchimistul", "psihologic", "78", "none", "78"]
    ]
    assert(modificare_vanzare(lst, "123", "1", "ghita")) == [
        [123, "ghita", "actiune", "90", "gold", "90"],
        [234, "idiotul", "deeper one", "123", "silver", "123"],
        [345, "alchimistul", "psihologic", "78", "none", "78"]
    ]
    assert(modificare_vanzare(lst, "234", "2", "romantic")) == [
        [123, "ghita", "actiune", "90", "gold", "90"],
        [234, "idiotul", "romantic", "123", "silver", "123"],
        [345, "alchimistul", "psihologic", "78", "none", "78"]
    ]
    assert(modificare_vanzare(lst, "345", "4", "silver")) == [
        [123, "ghita", "actiune", "90", "gold", "90"],
        [234, "idiotul", "romantic", "123", "silver", "123"],
        [345, "alchimistul", "psihologic", "78", "silver", "78"]
    ]


def test_stergere_vanzare():
    lst = [
        [123, "ion", "actiune", "90", "gold", "90"],
        [234, "idiotul", "deeper one", "123", "silver", "123"],
        [345, "alchimistul", "psihologic", "78", "none", "78"]
    ]
    assert(stergere_vanzare(lst, "123")) == [
        [234, "idiotul", "deeper one", "123", "silver", "123"],
        [345, "alchimistul", "psihologic", "78", "none", "78"]
    ]
    assert(stergere_vanzare(lst, "345")) == [[234, "idiotul", "deeper one", "123", "silver", "123"]]
    assert(stergere_vanzare(lst, "234")) == []


def test_aplicare_reducere():
    lst = [
        ["123", "ion", "actiune", "90", "gold", "90"],
        ["234", "idiotul", "deeper one", "123", "silver", "123"],
        ["345", "alchimistul", "psihologic", "78", "none", "78"],
        ["456", "minunea", "sad", "100", "silver", "100"]
    ]
    assert(aplicare_reducere(lst)) == [
        ["123", "ion", "actiune", "90", "gold", 76.5],
        ["234", "idiotul", "deeper one", "123", "silver", 110.7],
        ["345", "alchimistul", "psihologic", "78", "none", 78],
        ["456", "minunea", "sad", "100", "silver", 90]
    ]
    assert(aplicare_reducere(lst)) == [
        ["123", "ion", "actiune", "90", "gold", 76.5],
        ["234", "idiotul", "deeper one", "123", "silver", 110.7],
        ["345", "alchimistul", "psihologic", "78", "none", 78],
        ["456", "minunea", "sad", "100", "silver", 90]
    ]  # dar se va afisa, pentru fiecare vanzare,
    # "reducerea a fost aplicata"


def test_modificare_gen():
    lst = [
        ["123", "ion", "actiune", "90", "gold", "90"],
        ["234", "idiotul", "deeper one", "123", "silver", "123"],
        ["345", "alchimistul", "psihologic", "78", "none", "78"],
        ["456", "minunea", "sad", "100", "silver", "90"]
    ]
    assert(modificare_gen(lst, "ion", "romantic")) == [
        ["123", "ion", "romantic", "90", "gold", "90"],
        ["234", "idiotul", "deeper one", "123", "silver", "123"],
        ["345", "alchimistul", "psihologic", "78", "none", "78"],
        ["456", "minunea", "sad", "100", "silver", "90"]
    ]
    assert(modificare_gen(lst, "idiotul", "psihologic")) == [
        ["123", "ion", "romantic", "90", "gold", "90"],
        ["234", "idiotul", "psihologic", "123", "silver", "123"],
        ["345", "alchimistul", "psihologic", "78", "none", "78"],
        ["456", "minunea", "sad", "100", "silver", "90"]
    ]
    assert(modificare_gen(lst, "alchimistul", "educativ")) == [
        ["123", "ion", "romantic", "90", "gold", "90"],
        ["234", "idiotul", "psihologic", "123", "silver", "123"],
        ["345", "alchimistul", "educativ", "78", "none", "78"],
        ["456", "minunea", "sad", "100", "silver", "90"]
    ]


def test_undo():
    versiuni_undo = []
    lst = [[123, "ion", "actiune", "90", "gold", "90"]]
    salvare_versiune_undo(lst, versiuni_undo)
    lst.append([234, "idiotul", "deeper one", "123", "silver", "123"])
    salvare_versiune_undo(lst, versiuni_undo)
    lst.append([345, "alchimistul", "psihologic", "78", "none", "78"])
    salvare_versiune_undo(lst, versiuni_undo)
    lst.append([456, "minunea", "sad", "100", "silver", "90"])
    salvare_versiune_undo(lst, versiuni_undo)
    stergere_vanzare(lst, "345")
    salvare_versiune_undo(lst, versiuni_undo)
    modificare_gen(lst, "idiotul", "self improvement")
    salvare_versiune_undo(lst, versiuni_undo)
    lst.append([567, "cei trei muschetari", "echipa", "148", "silver", "148"])
    salvare_versiune_undo(lst, versiuni_undo)
    assert(undo(lst, versiuni_undo)) == [
        [123, "ion", "actiune", "90", "gold", "90"],
        [234, "idiotul", "self improvement", "123", "silver", "123"],
        [456, "minunea", "sad", "100", "silver", "90"]
    ]
    assert(undo(lst, versiuni_undo)) == [
        [123, "ion", "actiune", "90", "gold", "90"],
        [234, "idiotul", "deeper one", "123", "silver", "123"],
        [456, "minunea", "sad", "100", "silver", "90"]
    ]
    undo(lst, versiuni_undo)
    assert(undo(lst, versiuni_undo)) == [
        [123, "ion", "actiune", "90", "gold", "90"],
        [234, "idiotul", "deeper one", "123", "silver", "123"],
        [345, "alchimistul", "psihologic", "78", "none", "78"]
    ]


def test_pret_minim_pt_fiecare_gen():
    # [id: 0, titlu: 1, gen: 2, pret: 3, reducere: 4, pret redus: 5] -> legenda cu indexarea elementelor
    # dat fiind ca algoritmul foloseste doar elementele gen ( 2 ) si pret ( 3 ), doar acestea vor fi prezente in sir
    lst = [
        ["123", "wasd", "actiune", "100", "gold", "100"],
        ["124", "wasd", "romantic", "67", "gold", "67"],
        ["12", "wasd", "actiune", "15", "gold", "15"],
        ["125", "asd", "romantic", "68", "gold", "68"],
        ["1244", "wasd", "dezvoltare", "100", "gold", "100"],
        ["2354", "wasd", "actiune", "30", "gold", "30"]
    ]
    assert(pret_minim_pt_fiecare_gen(lst)) == [("actiune", 15), ("romantic", 67), ("dezvoltare", 100)]
    lst = [
        [" ", " ", "actiune", "9", "gold", "9"],
        [" ", " ", "romantic", "67", "gold", "67"],
        [" ", " ", "actiune", "15", "gold", "15"],
        [" ", " ", "romantic", "38", "gold", "38"],
        [" ", " ", "dezvoltare", "40", "gold", "40"],
        [" ", " ", "actiune", "9", "gold", "9"]
    ]
    assert (pret_minim_pt_fiecare_gen(lst)) == [("actiune", 9), ("romantic", 38), ("dezvoltare", 40)]


def test_ordonare_dupa_pret():
    lst = [
        ["123", "ion", "romantic", "90", "gold", "90"],
        ["234", "idiotul", "psihologic", "123", "silver", "123"],
        ["345", "alchimistul", "educativ", "78", "none", "78"],
        ["456", "minunea", "sad", "100", "silver", "100"]
    ]
    assert(ordonare_dupa_pret(lst)) == [
        ["345", "alchimistul", "educativ", "78", "none", "78"],
        ["123", "ion", "romantic", "90", "gold", "90"],
        ["456", "minunea", "sad", "100", "silver", "100"],
        ["234", "idiotul", "psihologic", "123", "silver", "123"]
    ]


def test_minim():
    lst = [
        ["3465", " ", "actiune", "9", "gold", "9"],
        ["35677", " ", "romantic", "67", "gold", "67"],
        ["2345", " ", "actiune", "15", "gold", "15"],
        ["235", " ", "romantic", "38", "gold", "38"],
        ["123", " ", "dezvoltare", "40", "gold", "40"],
        ["124", " ", "actiune", "9", "gold", "9"]
    ]
    assert(minim(lst, "actiune")) == 9
    assert(minim(lst, "romantic")) == 38
    assert(minim(lst, "dezvoltare")) == 40


def test_redo():
    versiuni_redo = []
    versiuni_undo = []
    lst = [
        [123, "ion", "actiune", 90, "gold", 90],
        [234, "idiotul", "self improvement", 123, "silver", 123],
        [456, "minunea", "sad", 100, "none", 100]
    ]
    lst = aplicare_reducere(lst)
    start = False
    salvare_versiune_undo(lst, versiuni_undo)
    lst = modificare_gen(lst, "idiotul", "psihologic")
    start = False
    salvare_versiune_undo(lst, versiuni_undo)
    salvare_versiune_redo(lst, versiuni_redo)
    lst = undo(lst, versiuni_undo)
    salvare_versiune_redo(lst, versiuni_redo)
    lst = undo(lst, versiuni_undo)
    start = True
    assert(redo(lst, versiuni_redo, start)) == [
        [123, "ion", "actiune", 90, "gold", 76.5],
        [234, "idiotul", "self improvement", 123, "silver", 110.7],
        [456, "minunea", "sad", 100, "none", 100]
    ]
    assert(redo(lst, versiuni_redo, start)) == [
        [123, "ion", "actiune", 90, "gold", 76.5],
        [234, "idiotul", "psihologic", 123, "silver", 110.7],
        [456, "minunea", "sad", 100, "none", 100]
    ]


def test_live_task_7():
    lst = []
    versiuni_undo = []
    versiuni_redo = []
    start = False

    lst.append("o1")
    salvare_versiune_undo(lst, versiuni_undo)
    start = False
    lst.append("o2")
    salvare_versiune_undo(lst, versiuni_undo)
    lst.append("o3")
    salvare_versiune_undo(lst, versiuni_undo)

    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)
    start = True
    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)
    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)
    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)

    lst.append("o1")
    salvare_versiune_undo(lst, versiuni_undo)
    lst.append("o2")
    salvare_versiune_undo(lst, versiuni_undo)
    lst.append("o3")
    salvare_versiune_undo(lst, versiuni_undo)
    start = False

    lst = redo(lst, versiuni_redo, start)
    salvare_versiune_undo(lst, versiuni_undo)

    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)
    start = True
    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)
    lst = redo(lst, versiuni_redo, start)
    salvare_versiune_undo(lst, versiuni_undo)
    lst = redo(lst, versiuni_redo, start)
    salvare_versiune_undo(lst, versiuni_undo)

    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)
    start = True
    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)

    lst.append("o4")
    salvare_versiune_undo(lst, versiuni_undo)
    start = False

    redo(lst, versiuni_redo, start)
    salvare_versiune_undo(lst, versiuni_undo)
    versiuni_redo.clear()

    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)
    start = True
    if len(versiuni_undo) != 0:
        salvare_versiune_redo(versiuni_undo[len(versiuni_undo) - 1], versiuni_redo)
    lst = undo(lst, versiuni_undo)

    lst = redo(lst, versiuni_redo, start)
    salvare_versiune_undo(lst, versiuni_undo)
    lst = redo(lst, versiuni_redo, start)
    salvare_versiune_undo(lst, versiuni_undo)

    lst = redo(lst, versiuni_redo, start)
    assert lst == ["o1", "o4"]


def all_tests():
    test_modificare_vanzare()
    test_modificare_gen()
    test_stergere_vanzare()
    test_aplicare_reducere()
    test_undo()
    test_pret_minim_pt_fiecare_gen()
    test_ordonare_dupa_pret()
    test_minim()
    test_redo()
    test_live_task_7()
