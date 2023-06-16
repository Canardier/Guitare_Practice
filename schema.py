class bcolors:
    RED = "\033[93m"
    ENDC = "\033[0m"

"""Print the scale and his harmonisation in tab with nature of note and spacement in T 1/2T
"""
def schema_scale(scale):
    print("|-------|-scale-|-{}-|".format(scale[0][2]))
    print("|note\t|nature\t|space\t|")
    print("|_______|_______|_______|")
    for note in scale:
        if note[1] == 1:
            space = "1/2T"
        elif note[1] == 2:
            space = "T"
        print("|{}\t|{}\t|{}\t|".format(note[0],note[2], space))
    print("|_______|_______|_______|")

"""print the triade in tab
"""
def schema_triade(triade):
    print("|-------|TRIADE |-------|")
    print("|note\t|nature\t|space\t|")
    print("|_______|_______|_______|")
    for note in triade:
        print("|{}\t|{}\t|{}\t|".format(note[0],note[2], note[1]))
    print("|_______|_______|_______|")

"""send line to print"""
def schema_line_triade(index, notes, scale, triade):
    i = index
    my_line = "|"
    while i < 16 + index:
        if triade[0][0] == notes[i%12][0]:
            my_line += bcolors.RED + triade[0][0] + bcolors.ENDC + "\t|"
        elif triade[1][0] == notes[i%12][0]:
            my_line += triade[1][0] + "\t|"
        elif triade[2][0] == notes[i%12][0]:
            my_line += triade[2][0] + "\t|"
        else :
            my_line += " \t|"
        i += 1
    return (my_line)

def schema_number_frette():
    i = 0
    my_line = "     0"
    while i < 14:
        if frette_case(i) == 1:
            my_line += "    {}".format(i)
        my_line += " \t "
        i += 1
    return (my_line)

def frette_case(number):
    frette_point = [3, 5, 7, 9, 12, 13, 15, 17, 19, 21]
    if number in frette_point:
        return 1
    else:
        return 0