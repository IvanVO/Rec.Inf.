import DoubleStemmer as ds

def main():
    
    stemmer = ds.DoubleStemmer()

    #stemmer.stemText("TestFiles/Liquid Water on Mars.txt")
    stemmer.stemText("TestFiles/First Presidential Debate.txt")

if __name__ == '__main__':
    main()