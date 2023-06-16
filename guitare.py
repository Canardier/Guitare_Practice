def note_init():
    """Return an array of note
    """
    note = [
        ["A", "La", 0], 
        ["A#", "La#", 1], 
        ["B", "Si", 2], 
        ["C", "Do", 3], 
        ["C#", "Do#", 4], 
        ["D", "Re", 5], 
        ["D#", "Re#", 6], 
        ["E", "Mi", 7], 
        ["F", "Fa", 8], 
        ["F#", "Fa#", 9],
        ["G", "Sol", 10],
        ["G#", "Sol#", 11]
    ]
    return note

def gamme_init(scale):
    """Return Major Or Minor scale
    Take in parameter the choice 0 or 1 for scale Major or Minor
    """
    pentatonic_major = [
        ["T", 2, "Major"],
        ["T", 2, "Minor"],
        ["T1/2", 3, "Minor"],
        ["T", 2, "Major"],
        ["T1/2", 3, "Major"],
    ]
    pentatonic_minor = [
        ["T1/2", 3, "Minor"],
        ["T", 2, "Major"],
        ["T1/2", 3, "Minor"],
        ["T", 2, "Minor"],
        ["T", 2, "Major"],
    ]
    major = [
        ["T", 2, "Major"],
        ["T", 2, "Minor"],
        ["1/2T", 1, "Minor"],
        ["T", 2, "Major"],
        ["T", 2, "Major"],
        ["T", 2, "Minor"],
        ["1/2T", 1, "Minor"],
    ]
    minor = [
        ["T", 2, "Minor"],
        ["1/2T", 1, "Minor"],
        ["T", 2, "Major"],
        ["T", 2, "Minor"],
        ["1/2T", 1, "Minor"],
        ["T", 2, "Major"],
        ["T", 2, "Major"],
    ]
    if scale == 0:
        return major
    elif scale == 1:
        return minor
    return major

"""Return the result of scale and his armonisation like this 
[['A', 2, 'Minor'], ['B', 1, 'Minor'], ['C', 2, 'Major'], ['D', 2, 'Minor'], ['E', 1, 'Minor'], ['F', 2, 'Major'], ['G', 2, 'Major']]

take in parameter note (all note)
take in parameter the scale (selected in prompt) 
take in parameter the my_note (selected in prompt)
"""
def gamme_harmonisation(notes, scale, my_note):
    i = my_note
    my_gamme_result = []
    for space in scale:
        my_gamme_result.append([notes[i%12][0], space[1], space[2]])  
        i+=space[1]
    return my_gamme_result

def triade_init(gammes):
    """Return array of the triade note from scale selected
    Take in parameter the gammes 
    """
    triade = [
        [gammes[0][0], gammes[0][1] + gammes[1][1], gammes[0][2]], #Fondamental 
        [gammes[2][0], gammes[2][1] + gammes[3][1], gammes[2][2]], #Tierce
        [gammes[4][0], gammes[4][1] + gammes[5][1] + gammes[6][1], gammes[4][2]]  #Quinte
    ]
    return triade



# harmonisation Majeur = M,m,m,M,M,m,m
# harmonisation mineur = m,m,M,m,m,M,M
