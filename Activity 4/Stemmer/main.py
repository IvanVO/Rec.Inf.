import DoubleStemmer as ds

def main():
    
    stemmer = ds.DoubleStemmer()

    stemmer.stemText("Liquid Water on Mars.txt")

if __name__ == '__main__':
    main()