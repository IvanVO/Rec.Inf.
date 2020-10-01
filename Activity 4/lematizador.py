import Stemmer

stemmer_en = Stemmer.Stemmer('english')
punctuation_marks = [".", ":", ";", ",", "?", '"', "'", "(", ")", "!"]
def main():
    f = open("/home/ivanvillanueva/Desktop/Stemmeing/Activity 4/Liquid Water on Mars.txt", "r")
    w = open("/home/ivanvillanueva/Desktop/Stemmeing/Activity 4/testLematizador.txt", "w")

    for line in f.readlines():
        items = line.split()
        for i in items:
            if i == "—":
                i = i.replace("—", '')
            for p in punctuation_marks:
                if i.find(p):
                    i = i.replace(p, '')
                    i = i.replace('"', "")    
            word = stemmer_en.stemWord(i)
            w.write(f"{word.lower()} ")



if __name__ == '__main__':
    main()
