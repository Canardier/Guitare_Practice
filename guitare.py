def note_init():
    note = [
        ["A", "La"], 
        ["A#", "La#"], 
        ["B", "Si"], 
        ["C", "Do"], 
        ["C#", "Do#"], 
        ["D", "Re"], 
        ["D#", "Re#"], 
        ["E", "Mi"], 
        ["F", "Fa"], 
        ["F#", "Fa#"],
        ["G", "Sol"],
        ["G#", "Sol#"]
    ]
    return note

def gamme_init(gamme):
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
    if gamme == 0:
        return major
    elif gamme == 1:
        return minor
    return major

def triade_init(gammes):
    # print(gammes)
    triade = [
        [gammes[0][0], gammes[0][1] + gammes[1][1], gammes[0][2]], #Fondamental 
        [gammes[2][0], gammes[2][1] + gammes[3][1], gammes[2][2]], #Tierce
        [gammes[4][0], gammes[4][1] + gammes[5][1] + gammes[6][1], gammes[4][2]]  #Quinte
    ]
    return triade



# harmonisation Majeur = M,m,m,M,M,m,m
# harmonisation mineur = m,m,M,m,m,M,M
