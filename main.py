from resolver import resoudre
from resolver import WORD_SIZE
from time import sleep
import json

def retirerLettre(possible : list, pos:int, lettre :str):
    if ord('A')<=ord(lettre[0])<=ord('Z'):
        lettre = str(chr(ord(lettre[0]) - (ord('A')-ord('a'))))
    match pos:
        case 0:
            for indice in range(WORD_SIZE):
                if lettre in possible[indice]:
                    possible[indice].remove(lettre)
        case others:
            if lettre in possible[pos-1]:
                possible[pos-1].remove(lettre)

def solution(possible,mots):
    while True:
        entree = int(input("Entrez la fonction a utiliser :\n" \
        "                       0 : voir les lettres possibles\n" \
        "                       1 : afficher toutes les possibilités\n" \
        "                       2 : retirer les possibilites\n"
        "                       3 : quitter\n"
        "Entrez votre choix : "))

        match entree:
            case 0 :
                for indice in range(WORD_SIZE):
                    print("Possibiltés au rang",indice+1,":",possible[indice])
            
            case 1:
                mots = resoudre(mots, possible)
                print(mots)

            case 2 :
                lettre = input("Lettre a retirer : ")
                while(len(lettre)!=1 
                      & (ord('a')<=ord(lettre[0])<=ord('z')
                       or ord('A')<=ord(lettre[0])<=ord('Z'))):
                    lettre = input("Lettre a retirer : ")

                pos = int(input("Entrez la position de la lettre à retirer (0=all) : "))
                while pos>5 or pos<0:
                    pos = int(input("Entrez la position de la lettre à retirer (0=all) : "))

                retirerLettre(possible,pos,lettre)

            case 3:
                exit(0)
        sleep(1)

def start(options : int):
    with open('data.json') as json_file:
        dictionnaire = list(json.load(json_file))

    mots = []
    for mot in dictionnaire:
        if(len(mot)==WORD_SIZE):
            mots.append(mot)

    if(options==0):
            """
            possible=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
            """
            possible=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
            
            
    else:
        possible=[]
        for indice in range(WORD_SIZE):
            possible.append([])
            for letters in range(26):
                possible[indice].append(chr(ord('a')+letters))

    solution(possible,mots)

'''
Choisir 0 pour pouvoir choisir les lettres a l'avance depuis l'editeur
    (permet d'avoir un ensemble de lettres déjà prédéfinies)

Choisir un autre entier pour commencer avec toutes les lettres
    (plus long car il faut éditer les lettres possibles depuis la console avec l'option 2)
'''
start(0)