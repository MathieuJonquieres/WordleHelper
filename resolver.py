from lettersModifier import WORD_SIZE
def resoudre(mots, possible, malPlace):
    resultats=mots
    #Parcours inversé pour ordre alphabetique
    for i in range(WORD_SIZE-1,-1,-1):
        resultats=filtrerLettreMot(possible, resultats,i)
    resultats = filtrerLettreMalPlaceMot(malPlace, resultats)
    return resultats

def motUnique(mots, possible, lettreUtil):
    resultats=mots
    for i in range(WORD_SIZE-1,-1,-1):
        resultats=filtrerLettreMot(possible, resultats,i)
    resultats = filtrerLettreNonUniqueMot(lettreUtil, resultats)
    return resultats



def filtrerLettreMot(possible:list, mots:list, pos:int):
    resultats=[]
    for lettre in possible[pos]:
        for mot in mots:
            #Ajoute si la lettre est bien place
            if mot[pos]==lettre:
                resultats.append(mot)
    return resultats

def filtrerLettreMalPlaceMot(malPlace:dict, mots):
    """
    resultats = []
    for mot in mots:
        ajout=True
        for lettre in malPlace:
            ok=False
            for pos in malPlace[lettre]:
                if lettre == mot[pos-1]:
                    ok=True
            if not ok:
                ajout=False
        if ajout:
            resultats.append(mot)
    return resultats
    """

    resultats = []
    for mot in mots:
        ajout=True
        for lettre in malPlace:
            if lettre not in mot:
                ajout = False
        if ajout:
            resultats.append(mot)
    return resultats

def filtrerLettreNonUniqueMot(lettreUnique:set, mots):
    resultats = []
    for mot in mots:
        ajout=True
        for lettre in mot:
            if lettre in lettreUnique:
                ajout=False
        if ajout:
            resultats.append(mot)
    return resultats