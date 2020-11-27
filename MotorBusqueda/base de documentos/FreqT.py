import os.path
import BaseDeDatos as db

freqTMatrix = None
termsList = None
docs = 0

class FreqT:

    def __init__(self):
        
        self.termsList = []
        self.docs = 0
        terms = self.getTerms()
        self.createFreqT(terms)

    def getTerms(self):

        database = db.BaseDeDatos()

        directory = './LematizedFiles/'
        list_files = os.listdir(directory)
        
        table_name = ""
        list_of_table_names = []

        for file_name in list_files:

            self.docs += 1

            for name in file_name:
                if name != " ":
                    table_name += name
                else: 
                    break
            
            list_of_table_names.append(table_name)
            table_name = ""

        terms = database.retreiveFromDatabase(list_of_table_names)

        return terms

    def createFreqT(self, terms):

        old_list_terms = []

        for i in range(self.docs):
            
            for j in range(len(terms[i])):
                
                if terms[i][j][0] not in old_list_terms:
                    old_list_terms.append(terms[i][j][0])

        rows = len(old_list_terms)
        columns = self.docs

        matrix = self.initializeMatrix(rows, columns)

        doc = 0

        for i in range(self.docs):
            
            for j in range(len(terms[i])):

                fila = old_list_terms.index(terms[i][j][0])
                matrix[fila][doc] = terms[i][j][1]

            doc += 1

        self.freqTMatrix = self.removeLessSignificantTerms(matrix, old_list_terms)

    def initializeMatrix(self, rows, columns):

        newMatrix = []

        for i in range(0, rows):

            newRow = []

            for j in range(0, columns):
                
                newRow.append(0)

            newMatrix.append(newRow)

        return newMatrix

    def removeLessSignificantTerms(self, matrix, list_terms):

        terms = len(matrix)
        
        termsToRemove = []
        count = 0

        for j in range(0, terms):

            for i in range(0, self.docs):
                if matrix[j][i] != 0:
                    count += 1

            if count == 1:
                termsToRemove.append(j)

            count = 0
        
        newTerms = len(matrix) - len(termsToRemove) # = 115

        newMatrix = self.initializeMatrix(newTerms, self.docs)

        for i in range(0, len(termsToRemove)):
            
            if i not in termsToRemove:
                self.termsList.append(list_terms[i])

        row = 0
        column = 0

        for j in range(terms):

            if j not in termsToRemove:
                
                for i in range(self.docs):
                    
                    newMatrix[row][column] = matrix[j][i]
                    column += 1

                row += 1
                column = 0

        return newMatrix

    def printMatrix(self):
        
        for i in range(self.docs):

            print("Doc" + str(i+1) + "\t", end='')

        print()

        for j in range(0, len(self.freqTMatrix)):

            for i in range(0, len(self.freqTMatrix[0])):
                print(str(self.freqTMatrix[j][i]) + "\t", end='')

            print(self.termsList[j], end='')
            print()

    def getMatrix(self):
        
        return self.freqTMatrix