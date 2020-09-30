import Stemmer

stemmer_en = Stemmer.Stemmer('english')

class Stemmer:
    def __init__(self):
        
def main():
    word = input("Insert a word: ")
    print(stemmer_en.stemWord(word))


if __name__ == '__main__':
    main()
