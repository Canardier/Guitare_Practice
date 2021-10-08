def schema_gamme(notes, gamme, my_note):
    i = my_note
    print("|-------|-GAMME-|-------|")
    print("|note\t|nature\t|space\t|")
    print("|_______|_______|_______|")
    my_gamme_result = []
    for space in gamme:
        my_gamme_result.append([notes[i%12][0], space[1], space[2]])  
        print("|{}\t|{}\t|{}\t|".format(notes[i%12][0],space[2], space[0]))
        i+=space[1]
    print("|_______|_______|_______|")
    # print(my_gamme_result)
    return my_gamme_result

def schema_triade(triade):
    heigth = 0
    width = 0
    print("|-------|TRIADE |-------|")
    print("|note\t|nature\t|space\t|")
    print("|_______|_______|_______|")
    for note in triade:
        print("|{}\t|{}\t|{}\t|".format(note[0],note[2], note[1]))
    print("|_______|_______|_______|")

def schema_line_triade(index, notes, gamme, triade):
    i = index
    my_line = "|"
    while i < 16 + index:
        if triade[0][0] == notes[i%12][0]:
            my_line += triade[0][0] + "\t|"
        elif triade[1][0] == notes[i%12][0]:
            my_line += triade[1][0] + "\t|"
        elif triade[2][0] == notes[i%12][0]:
            my_line += triade[2][0] + "\t|"
        else :
            my_line += " \t|"
        i += 1
    return (my_line)