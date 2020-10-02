import Stemmer

class DoubleStemmer:

    def __init__(self):

        self.stemmer = Stemmer.Stemmer('english')

        # -------------------------------- Read and store irregular nouns

        self.irregularNounsPlural = []
        self.irregularNouns = []

        irregularNounsPluralFile = open("WordsList/irregularNounsPlural.txt", "r")
        irregularNounsFile = open("WordsList/irregularNouns.txt", "r")

        for pluralNoun in irregularNounsPluralFile:

            self.irregularNounsPlural.append(pluralNoun.replace('\n', ''))

        for noun in irregularNounsFile:

            self.irregularNouns.append(noun.replace('\n', ''))

        # ------------------------- Read and store irregular verb endings

        self.irregularEndings = []

        irregularEndingsFile = open("WordsList/irregularEndings.txt", "r")

        for suffix in irregularEndingsFile:

            self.irregularEndings.append(suffix.replace('\n', ''))

        # --------------------------------------------- Remove stop words

        self.stopList = []

        stopListFile = open("WordsList/stop.txt", "r")

        for stopWord in stopListFile.readlines():

            stop_word = stopWord.strip()
            self.stopList.append(stop_word)

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

        output = self.getOutputName(text)

        # ------------------------------ Remove punctuation marks in text

        punctuation_marks = [".", ":", ";", ",", "?", '"', "'", "(", ")", "!", "-"]

        f = open(text, "r")
        w = open(output, "w")
            
        for line in f.readlines():

            items = line.split()

            for i in items:

                i = i.lower()

                if i == "—":
                    i = i.replace("—", '')
                elif i == ".":
                    i = i.replace(".", '')

                for p in punctuation_marks:

                    if i.find(p):
                        i = i.replace(p, '')
                        i = i.replace('"', "")

                for sw in self.stopList:
                    if i == sw:
                        i = i.replace(sw, '')

                #print(i)
                word = self.stemWordPre(i)
                #print(word)
                if word != None:
                    w.write(f"{word.lower()} ")

    def getOutputName(self, text):

        name = str(text)

        index = name.find('/')
        index += 1

        output = ""

        for i in range(index, len(name)-4):
            
            output += str(name[i])

        output += " LEMMATIZED.txt"
        #print(output)

        return output