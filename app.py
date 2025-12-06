from resolver import resoudre
from lettersModifier import modifierLettre
from lettersModifier import lettreInput
from lettersModifier import WORD_SIZE
from lettersModifier import convertisseurMinuscule

def solution(possible, malPlace, mots):
    while True:
        choixFonction=-1
        while choixFonction<0 or choixFonction>3:
            choixFonction = int(input("Entrez la fonction a utiliser :\n" \
            "                       0 : Voir les lettres possibles\n" \
            "                       1 : Afficher toutes les possibilités\n" \
            "                       2 : Changer les possibilites\n"
            "                       3 : Quitter\n"
            "Entrez votre choix : "))

        match choixFonction:
            case 0 :
                for indice in range(WORD_SIZE):
                    print("Possibiltés au rang",indice+1,":",possible[indice])
                for lettre in malPlace:
                    print("Positions possibles de la lettre :",lettre,":",malPlace[lettre])
            case 1:
                mots = resoudre(mots, possible, malPlace)
                print(mots)

            case 2 :
                choixChangement=-1
                while(choixChangement<0 or choixChangement>3):
                    choixChangement = int(input("MODIFICATION : Entrez la modification a faire :\n" \
                    "                       0 : Ajouter une possibilité\n" \
                    "                       1 : Retirer une possibilité\n" \
                    "                       2 : Ajouter une lettre mal placé\n"
                    "                       3 : Fixer une possibilité\n"
                    "Entrez votre choix : "))
                match choixChangement:
                    case 0:
                        lettre,pos = lettreInput("Lettre à ajouter : ",
                                                 "Entrez la position de la lettre à ajouter (0=all) : ",0)
                        modifierLettre(True,possible,lettre,pos)

                    case 1:
                        lettre,pos = lettreInput("Lettre a retirer : ",
                                                 "Entrez la position de la lettre à retirer (0=all) : ",0)
                        modifierLettre(False,possible,lettre,pos)
                    case 2:
                        lettre,pos = lettreInput("Lettre mal placée : ",
                                                 "Entrez la position de la lettre mal placée : ",1)
                        lettre = convertisseurMinuscule(lettre)
                        if lettre not in malPlace:
                            malPlace[lettre]=[]
                            for i in range(WORD_SIZE):
                                malPlace[lettre]+=[i+1]
                        if (pos) in malPlace[lettre]:
                            malPlace[lettre].remove(pos)
                        

                    case 3:
                        lettre,pos = lettreInput("Lettre à fixer : ",
                                                 "Entrez la position de la lettre à fixer : ",1)
                        
                        possible[pos-1]=[convertisseurMinuscule(lettre)]
                        
            case 3:
                exit(0)