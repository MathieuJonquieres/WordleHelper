WORD_SIZE = 5
'''
Permet d'ajouter une lettre ou de la retirer en fonction du booleen en entree
La lettre sera ajoute/retire de la liste au rang pos, toute si pos = 0 
'''
def ajouterLettre(possible : list, lettre :str, pos:int):
    lettre = convertisseurMinuscule(lettre)
    match pos:
        case 0:
            for indice in range(WORD_SIZE):
                if lettre not in possible[indice]:
                    possible[indice].append(lettre)
                    possible[indice].sort()
        case others:
            if lettre not in possible[pos-1]:
                possible[pos-1].append(lettre)
                possible[pos-1].sort()

def retirerLettre(possible : list, lettre :str):
     for indice in range(WORD_SIZE):
        if lettre in possible[indice]:
            possible[indice].remove(lettre)

def ajouterMalPlace(possible, malPlace, lettreUtil, lettre, pos):
    if (lettre not in malPlace) and (lettre in possible[pos]):
        malPlace[lettre]=[]
        for i in range(WORD_SIZE):
            malPlace[lettre]+=[i+1]
    if lettre in malPlace:
        if pos in malPlace[lettre]:
            malPlace[lettre].remove(pos)
            possible[pos].remove(lettre)
    lettreUtil.add(lettre)
         

def lettreInput(text:str):
    lettre = input(text)
    while(len(lettre)!=1 
            & (ord('a')<=ord(lettre[0])<=ord('z')
            or ord('A')<=ord(lettre[0])<=ord('Z'))):
                lettre = input(text)
    lettre = convertisseurMinuscule(lettre)
    return lettre

def posInput(text, minPos:int):
    pos = -1
    while pos>WORD_SIZE or pos<minPos:
        pos = int(input(text))
    return pos

def convertisseurMinuscule(lettre:str):
    if(ord('A')<=ord(lettre[0])<=ord('Z')):
        lettre = str(chr(ord(lettre[0])-(ord('A')-ord('a'))))
    return lettre