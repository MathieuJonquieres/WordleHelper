WORD_SIZE = 5

def resoudre(mots, possible):
    resultats=mots
    #Parcours inversé pour ordre alphabetique
    for i in range(WORD_SIZE-1,-1,-1):
        resultats=filtrerLettreFixeMot(possible, resultats,i)
    return resultats

def filtrerLettreFixeMot(possible:list, mots:list,  pos:int):
    resultats=[]
    for lettre in possible[pos]:
        for mot in mots:
            #Ajoute si la lettre est bien place
            if mot[pos]==lettre:
                resultats.append(mot)
    return resultats