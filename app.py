from resolver import resoudre
from resolver import motUnique
from lettersModifier import ajouterLettre
from lettersModifier import retirerLettre
from lettersModifier import lettreInput
from lettersModifier import WORD_SIZE
from lettersModifier import convertisseurMinuscule
from lettersModifier import posInput
from lettersModifier import ajouterMalPlace

def solution(possible, malPlace, mots):
    lettreUtil = set()
    while True:
        choixFonction=-1
        while choixFonction<0 or choixFonction>4:
            choixFonction = int(input("Entrez la fonction a utiliser :\n" \
            "                       0 : Voir les lettres possibles\n" \
            "                       1 : Afficher toutes les possibilités\n" \
            "                       2 : Afficher les mots composés de",WORD_SIZE,"lettres non utilisées\n"
            "                       3 : Changer les possibilites\n" \
            "                       4 : Quitter\n" \
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

            case 2:
                print(motUnique(mots,possible,malPlace))

            case 3 :
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
                        lettre,pos = lettreInput("Lettre à ajouter : ")
                        pos = posInput("Entrez la position de la lettre à ajouter (0=all) : ",0)
                        ajouterLettre(possible,lettre,pos)

                    case 1:
                        lettre = lettreInput("Entrez la lettre à retirer : ")
                        retirerLettre(possible,lettre)
                        lettreUtil.add(lettre)

                    case 2:
                        lettre = lettreInput("Lettre mal placée : ")
                        pos = posInput("Entrez la position de la lettre mal placée : ",1)
                        ajouterMalPlace(possible, malPlace, lettreUtil, lettre, pos)

                    case 3:
                        lettre,pos = lettreInput("Lettre à fixer : ")
                        pos = posInput("Entrez la position de la lettre à fixer : ",1)
                        possible[pos-1]=[convertisseurMinuscule(lettre)]
                        
            case 4:
                exit(0)

