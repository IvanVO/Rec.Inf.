import os.path
import DoubleStemmer as ds
import LSI as lsi
import BaseDeDatos as db
def main():
    database = db.BaseDeDatos()
    
    database.dropCreate()
    stemmer = ds.DoubleStemmer()
    lsi_ = lsi.LSI()

    directory = './TestFiles/'
    list_files = os.listdir(directory)
    
    for file in list_files:
       if file.endswith(".txt"):    
           stemmer.stemText(f"TestFiles/{file}")

    lsi_.listFiles()
    lsi_.retrieveData()


if __name__ == '__main__':
    main()
