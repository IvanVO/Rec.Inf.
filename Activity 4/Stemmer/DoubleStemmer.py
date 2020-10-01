import Stemmer

class DoubleStemmer:

    def __init__(self):

        self.stemmer = Stemmer.Stemmer('english')

        # -------------------------------- Read and store irregular nouns

        self.irregularNounsPlural = []
        self.irregularNouns = []

        irregularNounsPluralFile = open("irregularNounsPlural.txt", "r")
        irregularNounsFile = open("irregularNouns.txt", "r")

        for pluralNoun in irregularNounsPluralFile:

            self.irregularNounsPlural.append(pluralNoun.replace('\n', ''))

        for noun in irregularNounsFile:

            self.irregularNouns.append(noun.replace('\n', ''))

        # ------------------------- Read and store irregular verb endings

        self.irregularEndings = []

        irregularEndingsFile = open("irregularEndings.txt", "r")

        for suffix in irregularEndingsFile:

            self.irregularEndings.append(suffix.replace('\n', ''))

    def stemWordPre(self, word):

        where = None

        try:
            where = self.irregularNounsPlural.index(word)
        except:
            #print("No está")
            pass

        if where != None:

            #print(irregularNouns[where])
            return self.irregularNouns[where]

        else:

            newWord = self.stemmer.stemWord(word)
            #print(newWord)

            if newWord != word:    

                #print(newWord)
                return newWord

            else:

                #print("[No sirvió Snowball, pero ntp, la respuesta es:]")
                return self.stemWordAgain(newWord)

    def stemWordAgain(self, word):

        for ending in self.irregularEndings:

            if word.endswith(ending):

                newWord = word.replace(ending, "")

                if len(newWord) > 2:

                    #print(newWord)
                    return newWord

                else:
                    return None

    def stemText(self, text):

        # ------------------------------ Remove punctuation marks in text

        punctuation_marks = [".", ":", ";", ",", "?", '"', "'", "(", ")", "!", "-"]

        f = open(text, "r")
        w = open("testLematizador.txt", "w")

        for line in f.readlines():

            items = line.split()

            for i in items:

                if i == "—":
                    i = i.replace("—", '')

                for p in punctuation_marks:

                    if i.find(p):
                        i = i.replace(p, '')
                        i = i.replace('"', "")
  
                #print(i)
                word = self.stemWordPre(i)
                #print(word)
                if word != None:
                    w.write(f"{word.lower()} ")

        

"""
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
"""