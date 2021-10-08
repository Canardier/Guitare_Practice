from guitare import * 
from schema import *

def main():
    i = 0
    notes = note_init()
    for note in notes:
        print("{}-{}:{}".format(i, notes[i][0], notes[i][1]))
        i+=1
    my_note = input("choose number for get note: \n---->$:")
    my_gamme = input("What gamme want u see ? \n0-major \n1-minor (default major)?\n---->$:")
    gamme = gamme_init(int(my_gamme))
    gamme = schema_gamme(notes, gamme, int(my_note))
    triade = triade_init(gamme)
    schema_triade(triade)
    E = schema_line_triade(7,notes, gamme, triade)
    A = schema_line_triade(0,notes, gamme, triade)
    D = schema_line_triade(5,notes, gamme, triade)
    G = schema_line_triade(10,notes, gamme, triade)
    B = schema_line_triade(2,notes, gamme, triade)
    print("1-{}".format(E))
    print("2-{}".format(B))
    print("3-{}".format(G))
    print("4-{}".format(D))
    print("5-{}".format(A))
    print("6-{}".format(E))

if __name__ == "__main__":
    main()