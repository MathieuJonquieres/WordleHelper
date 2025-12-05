WORD_SIZE = 5

def resoudre(mots, possible):

    resultats=mots
    for i in range(WORD_SIZE):
        for lettre in possible[i]:
            resultats=filtrerLettreFixeMot(resultats,lettre, i)
    return resultats

def filtrerLettreFixeMot(mots:list, lettre:str, pos:int):
    resultats=[]
    for mot in mots:
        #Ajoute si la lettre est bien place
        if mot[pos]==lettre:
            resultats.append(mot)
    return resultats