WORD_SIZE = 5
'''
Permet d'ajouter une lettre ou de la retirer en fonction du booleen en entree
La lettre sera ajoute/retire de la liste au rang pos, toute si pos = 0 
'''
def modifierLettre(ajout:bool, possible : list, lettre :str, pos:int):
    lettre = convertisseurMinuscule(lettre)
    if ajout:
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
    else:
        match pos:
            case 0:
                for indice in range(WORD_SIZE):
                    if lettre in possible[indice]:
                        if len(possible[indice])==1:
                            print("Une liste ne peut pas contenir moins d'une lettre! (liste a la position",indice+1+")")
                        else:
                            possible[indice].remove(lettre)
            case others:
                if lettre in possible[pos-1]:
                    if len(possible[indice])==1:
                        print("Une liste ne peut pas contenir moins d'une lettre! (liste a la position",indice+1+")")
                    else:
                        possible[pos-1].remove(lettre)

def lettreInput(textLettre:str, textPos:str, minPos:int):
    lettre = input(textLettre)
    while(len(lettre)!=1 
            & (ord('a')<=ord(lettre[0])<=ord('z')
            or ord('A')<=ord(lettre[0])<=ord('Z'))):
                lettre = input(textLettre)
    convertisseurMinuscule(lettre)
    pos = -1
    while pos>WORD_SIZE or pos<minPos:
        pos = int(input(textPos))
    return lettre,pos

def convertisseurMinuscule(lettre:str):
    if(ord('A')<=ord(lettre[0])<=ord('Z')):
        lettre = str(chr(ord(lettre[0])-(ord('A')-ord('a'))))
    return lettre