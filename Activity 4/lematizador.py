import Stemmer
import DoubleStemmer as ds

stemmer_en = Stemmer.Stemmer('english')
punctuation_marks = [".", ":", ";", ",", "?", '"', "'", "(", ")", "!", "-"]

def stemm(f, w):

    for line in f.readlines():
        items = line.split()
        for i in items:
            if i == "—":
                i = i.replace("—", '')
            elif i == ".":
                i = i.replace(".", '')

            for p in punctuation_marks:
                if i.find(p):
                    i = i.replace(p, '')
                    i = i.replace('"', "")

            word = stemmer_en.stemWord(i)
            w.write(f"{word.lower()} ")

def main():
    f = open("Liquid Water on Mars.txt", "r")
    w = open("Lematizador_output.txt", "w")

    stemm(f, w)

if __name__ == '__main__':
    main()
