from lettersModifier import WORD_SIZE
def resoudre(mots, possible, malPlace):
    resultats=mots
    #Parcours inversé pour ordre alphabetique
    for i in range(WORD_SIZE-1,-1,-1):
        resultats=filtrerLettreMot(possible, resultats,i)
    resultats = filtrerLettreMalPlaceMot(malPlace, resultats)
    return resultats

def filtrerLettreMot(possible:list, mots:list, pos:int):
    resultats=[]
    for lettre in possible[pos]:
        for mot in mots:
            #Ajoute si la lettre est bien place
            if mot[pos]==lettre:
                resultats.append(mot)
    return resultats

def filtrerLettreMalPlaceMot(malPlace, mots):
    resultats = []
    for mot in mots:
        ok=True
        for pos in range(WORD_SIZE):
            if mot[pos] in malPlace:
                if pos not in malPlace[mot[pos]]:
                    ok = False
        if ok:
            resultats.append(mot)
    return resultats