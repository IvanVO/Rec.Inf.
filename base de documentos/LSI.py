import BaseDeDatos as db
import os.path

class LSI:
    def __init__(self):
        pass

    def storeToDb(self, filename, list_of_dictionaries, index):
        database = db.BaseDeDatos()

        '''documents_content = ""
        directory = "./CSVFiles/"

        # Create the name of the file
        csv_file_name = f"{filename[:-4]} & TERM FREC.txt"
        
        # Save the files name in the directory
        file_path = os.path.join(directory, csv_file_name)

        # If file directory does not exists create it
        if not os.path.isdir(directory):
            os.mkdir(directory)

        file = open(file_path, 'w')'''

        db_tables_list = []
        # Create database tables
        db_table_name = database.createTable(filename)

        # Creating a list of the db tables names.
        db_tables_list.append(db_table_name)
        # write in the file the key and its value in the file
        for key, value in list_of_dictionaries[index].items():
            # For the database
            database.insertTermsFreq(db_table_name, key, value)
            '''# For the file
            #file.write(f"{key},{value}\n")

        #file.close()'''
        

    def count_terms(self, file):
        content = open(f"./LematizedFiles/{file}", 'r')
        dictionary = dict()

        # List of the terms
        term_list = []

        for line in content:
            # Remove the leading spaces and newline character
            line = line.strip()

            # Convert the characters in line to lowercase to avoid case mismatch
            line = line.lower()

            # Split the line into words
            words = line.split(" ")

            # Iterate over each word in line
            for word in words:
                # Check if the word is already in dictionary
                if word in dictionary:
                    # Increment count of word by 1
                    dictionary[word] = dictionary[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    dictionary[word] = 1
        
        return dictionary


    def listFiles(self):

        directory = './LematizedFiles/'
        csv_directory = './CSVFiles/'
        
        list_files = os.listdir(directory)
        list_of_dictionaries = []
        count = 0

        for file in list_files:
            if file.endswith(".txt"):
                list_of_dictionaries.append(self.count_terms(file))
            store_dictionaries = self.storeToDb(file, list_of_dictionaries, count)
            count += 1

        return store_dictionaries


    def retrieveData(self):
        database = db.BaseDeDatos()
        database.retreiveFromDatabase("Covid")

