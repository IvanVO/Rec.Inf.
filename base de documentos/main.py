import BaseDeDatos as db
import DoubleStemmer as ds

def main():

    stemmer = ds.DoubleStemmer()
    database = db.BaseDeDatos()
    #stemmer.stemText("TestFiles/Liquid Water on Mars.txt")
    # stemmer.stemText("TestFiles/First Presidential Debate.txt")
    stemmed = stemmer.stemText("TestFiles/Galaxies trapped in a black hole.txt")
    database.insertBLOB(stemmed)

if __name__ == '__main__':
    main()
