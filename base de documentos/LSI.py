import BaseDeDatos as db
import os.path

class LSI:
    def __init__(self):
        pass

    def storeToDb(self, filename, list_of_dictionaries, index):
        database = db.BaseDeDatos()

        db_tables_list = []
        # Create database tables
        db_table_name = database.createTable(filename)

        # Creating a list of the db tables names.
        db_tables_list.append(db_table_name)
        # write in the file the key and its value in the file
        for key, value in list_of_dictionaries[index].items():
            # For the database
            database.insertTermsFreq(db_table_name, key, value)

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
            words = line.split(" ")

            for word in words:
                if word in dictionary:
                    # Increment count of word by 1
                    dictionary[word] = dictionary[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    dictionary[word] = 1
        
        return dictionary


    def listFiles(self):
        directory = './LematizedFiles/'
        
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

        directory = './LematizedFiles/'
        list_files = os.listdir(directory)
        
        table_name = ""
        list_of_table_names = []

        for file_name in list_files:
            for name in file_name:
                if name != " ":
                    table_name += name
                else: 
                    break
            
            list_of_table_names.append(table_name)
            table_name = ""
        
        database.retreiveFromDatabase(list_of_table_names)

