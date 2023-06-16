from guitare import * 
from schema import *

import json

def cli_version():
    i = 0
    notes = note_init()
    for note in notes:
        print("{}-{}:{}".format(i, notes[i][0], notes[i][1]))
        i+=1
    my_note = input("choose number for get note: \n---->$:")
    my_scale = input("What scale want u see ? \n0-major \n1-minor (default major)?\n---->$:")
    if (my_scale == ""):
        my_scale = 0
    scale = gamme_init(int(my_scale))
    scale = gamme_harmonisation(notes, scale, int(my_note))
    triade = triade_init(scale)
    schema_scale(scale)
    schema_triade(triade)
    frette = schema_number_frette()
    E = schema_line_triade(7,notes, scale, triade)
    A = schema_line_triade(0,notes, scale, triade)
    D = schema_line_triade(5,notes, scale, triade)
    G = schema_line_triade(10,notes, scale, triade)
    B = schema_line_triade(2,notes, scale, triade)
    print("{}".format(frette))
    print("1-{}".format(E))
    print("2-{}".format(B))
    print("3-{}".format(G))
    print("4-{}".format(D))
    print("5-{}".format(A))
    print("6-{}".format(E))
    print("{}".format(frette))