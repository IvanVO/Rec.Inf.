import Stemmer

class DoubleStemmer:

    def __init__(self):

        self.irregularEndings = []

        irregularEndingsFile = open("irregularEndings.txt", "r")

        for suffix in irregularEndingsFile:

            self.irregularEndings.append(suffix.replace('\n', ''))

    def stemWordPre(self, word):

        irregularNounsPlural = []
        irregularNouns = []

        irregularNounsPluralFile = open("irregularNounsPlural.txt", "r")
        irregularNounsFile = open("irregularNouns.txt", "r")

        for pluralNoun in irregularNounsPluralFile:

            irregularNounsPlural.append(pluralNoun.replace('\n', ''))

        for noun in irregularNounsFile:

            irregularNouns.append(noun.replace('\n', ''))

        where = None

        try:
            where = irregularNounsPlural.index(word)
        except:
            #print("No está")
            pass

        if where != None:

            #print(irregularNouns[where])
            return irregularNouns[where]

    def stemWordAgain(self, word):
        
        for ending in self.irregularEndings:

            if word.endswith(ending):

                newWord = word.replace(ending, "")

                if len(newWord) > 2:

                    #print(newWord)
                    return newWord

                else:
                    return None


doubleStem = DoubleStemmer()

while True:

    stemmer = Stemmer.Stemmer('english')

    ogWord = input('==> Word: ')
    
    #word = stemmer.stemWord(ogWord)
    word = doubleStem.stemWordPre(ogWord)

    #if ogWord == word:
    if word == None:

        #print("[No es sustantivo irregular]")
        
        word = stemmer.stemWord(ogWord)

        if ogWord == word:    

            #print("[No sirvió Snowball, pero ntp, la respuesta es:]")

            result = doubleStem.stemWordAgain(ogWord)

            if result != None:
                print(result)
            else:
                print("Te la pelaste")
                pass

        else:
            print(word)

    else:
        print(word)
