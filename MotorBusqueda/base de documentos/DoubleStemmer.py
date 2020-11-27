import os.path
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
            pass

        if where != None:
            return self.irregularNouns[where]
        else:
            newWord = self.stemmer.stemWord(word)
            if newWord != word:    
                return newWord
            else:
                return self.stemWordAgain(newWord)

    def stemWordAgain(self, word):
        for ending in self.irregularEndings:
            if word.endswith(ending):
                newWord = word.replace(ending, "")
                if len(newWord) > 2:
                    return newWord
                else:
                    return None

    def stemText(self, text):
        output = self.getOutputName(text)
        
        # ------------------------------ Remove punctuation marks in text
        punctuation_marks = [".", ":", ";", ",", "?", '"', "'", "(", ")", "!", "-", "[", "]", "’"]

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
                        i = i.replace("[", "")
                        i = i.replace("(", "")

                for sw in self.stopList:
                    if i == sw:
                        i = i.replace(sw, '')

                word = self.stemWordPre(i)

                if output[5] == 'Q':
                    if word != None:
                        w.write(f"{word.lower()}\n")
                else:
                    if word != None:
                        w.write(f"{word.lower()} ")
               

        f.close()
        w.close()

    def getOutputName(self, text):
        directory = "./LematizedFiles/"
        query_directory = "./LemQueries/"

        name = str(text)
        index = name.find('/')
        index += 1
        output = ""
        
        for i in range(index, len(name)-4):
            output += str(name[i])
        
        output += " LEM.txt"

        if text[2] == 'Q':
            f = open(text, 'r')

            file_path = os.path.join(query_directory, output[8:])
            
            if not os.path.isdir(query_directory):
                os.mkdir(query_directory)

            return file_path

        else:
            file_path = os.path.join(directory, output)

            if not os.path.isdir(directory):
                os.mkdir(directory)

            return file_path