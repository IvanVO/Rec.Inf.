import os.path
import DoubleStemmer as ds

def main():

    stemmer = ds.DoubleStemmer()
    directory = './TestFiles/'
    list_files = os.listdir(directory)
    for file in list_files:
        if file.endswith(".txt"):    
            # print(f"{directory}{file}")
            stemmer.stemText(f"TestFiles/{file}")

if __name__ == '__main__':
    main()
"""
Covid pandemic has little impact on rise in CO2.txt
Winters are Warming and Climate Change is the Driver.txt
Fact-checking the US and China on climate and environment.txt
Creating An Environment Where Personal Growth Leads To Business Growth.txt

"""