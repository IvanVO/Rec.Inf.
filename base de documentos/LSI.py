import os.path

def count_terms(file):
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

def list_files():
    directory = './LematizedFiles/'
    list_files = os.listdir(directory)
    list_of_dictionaries = []
    count = 0
    for file in list_files:
        if file.endswith(".txt"):
            list_of_dictionaries.append(count_terms(file))
            # print(len(count_terms(file)))
    for dictionary in list_of_dictionaries:
        print(dictionary)
        # for key in dictionary:
        #     print(key)
        #     count += 1
        
    # print(len(list_of_dictionaries))

def main():
    list_files()
      
if __name__ == '__main__':
    main()