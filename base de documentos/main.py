import os.path
import DoubleStemmer as ds
import LSI as lsi

def main():

    stemmer = ds.DoubleStemmer()
    
    directory = './TestFiles/'
    list_files = os.listdir(directory)
    
    for file in list_files:
        if file.endswith(".txt"):    
            stemmer.stemText(f"TestFiles/{file}")

    lsi.list_files()

if __name__ == '__main__':
    main()
