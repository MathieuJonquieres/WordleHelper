from lettersModifier import WORD_SIZE
def resolve(wordsList, possibility, incorrect):
    results=wordsList
    for i in range(WORD_SIZE-1,-1,-1):
        results=filterWordLetters(possibility, results,i)
    results = filterWordIncorrectLetters(incorrect, results)
    return results

def uniqueWords(wordsList, possibility, letterUsed):
    results=wordsList
    for i in range(WORD_SIZE-1,-1,-1):
        results=filterWordLetters(possibility, results,i)
    results = filterWordNonUniqueLetters(letterUsed, results)
    return results

def filterWordLetters(possibility:list, wordsList:list, pos:int):
    results=[]
    for letter in possibility[pos]:
        for word in wordsList:
            #Add the letter if the placement is correct
            if word[pos]==letter:
                results.append(word)
    return results

def filterWordIncorrectLetters(incorrect:dict, wordsList):
    results = []
    for word in wordsList:
        ajout=True
        for letter in incorrect:
            if letter not in word:
                ajout = False
        if ajout:
            results.append(word)
    return results

def filterWordNonUniqueLetters(uniqueLetter:set, wordsList):
    results = []
    for word in wordsList:
        add=True
        for letter in uniqueLetter:
            if letter in word:
                add=False
        if add:
            results.append(word)
    return results