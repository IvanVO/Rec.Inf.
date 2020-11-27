import os.path
import string, random
import numpy as np
from numpy import sqrt, power
from numpy.linalg import svd
import random as rand
import DoubleStemmer as ds
import FreqT as freqt

class SimDis:
    def __init__(self):
        pass

    """-----------------Similitud-----------------"""
    def internProduct(self, doc_A, doc_B, freqT):
        # Assigned freqT to X
        X = freqT
        # Variable para la sumatoria de la formula

        T, S, D = svd(X, full_matrices=False)
        S = np.diag(S) # Matriz singunlar
        R = S.shape[1] # 
        print(f"{S}\n")
        del_ = int(input(f"Escriba la cantidad de documentos no pertinentes: "))
        k = R - del_ # Valor para saber cuantos docs eliminar de la matriz
        Tp = np.delete(T, np.s_[k::], 1)
        Sp = np.delete(np.delete(S, np.s_[k::], 0), np.s_[k::], 1)
        Dp = np.delete(D, np.s_[k::], 0)

        new_freqT = Tp @ Sp @ Dp
        # Extraction of doc A and doc B from freqT

        M = new_freqT.shape[0]

        doc_A = new_freqT[:,doc_A]
        doc_B = new_freqT[:,doc_B]
        
        sim_list = []
        zip_obj = zip(doc_A, doc_B)

        # Adding both documents to a list
        for i in range(0, M):
            for doc_A, doc_B in zip_obj:
                sim_list.append(doc_A * doc_B)

        doc_similarity = 0
        for i in sim_list:
            doc_similarity += i

        # Product intern distance of the originial Matrix
        print(doc_similarity)

        return doc_similarity

    def diceCoeficients(self, doc_A, doc_B, freqT):
        # Assigned freqT to X
        X = freqT

        numerator_value = 0
        denomiantor_value1 = 0
        denomiantor_value2 = 0
        doc_similarity = 0
        sim_list = []

        # SVD
        T, S, D = svd(X, full_matrices=False)
        S = np.diag(S) # Matriz singunlar
        R = S.shape[1] # 
        print(f"{S}\n")
        del_ = int(input(f"Escriba la cantidad de documentos no pertinentes: "))
        k = R - del_ # Valor para saber cuantos docs eliminar de la matriz
        Tp = np.delete(T, np.s_[k::], 1)
        Sp = np.delete(np.delete(S, np.s_[k::], 0), np.s_[k::], 1)
        Dp = np.delete(D, np.s_[k::], 0)

        new_freqT = Tp @ Sp @ Dp
        # Variable para la sumatoria de la formula
        M = new_freqT.shape[0]

        # Extraction of doc A and doc B from freqT
        doc_A = new_freqT[:,doc_A]
        doc_B = new_freqT[:,doc_B]

        # Converting doc_A and doc_B to list
        docA_list = doc_A.tolist()
        docB_list = doc_B.tolist()

        zip_obj = zip(doc_A, doc_B)

        for i in range(0, M):
            for doc_A, doc_B in zip_obj:
                sim_list.append(doc_A * doc_B)

        numerator_value = sum(sim_list)
        numerator_value *= 2
        # print("numerator: ", numerator_value)

        sim_list = []
        for i in docA_list:
            sim_list.append(np.power(i, 2))

        denomiantor_value1 = sum(sim_list)
        # print("denominator value 1: ", denomiantor_value1)

        sim_list = []
        for i in docB_list:
            sim_list.append(np.power(i, 2))

        denomiantor_value2 = sum(sim_list)
        # print("denominator value 2: ", denomiantor_value2)

        doc_similarity = numerator_value / (denomiantor_value1 + denomiantor_value2)

        print(doc_similarity)

        return doc_similarity

    """-----------------Disimilitud-----------------"""
    def manhattanDistance(self, doc_A, doc_B, freqT):
        # Assigned freqT to X
        X = freqT

        # SVD
        T, S, D = svd(X, full_matrices=False)
        S = np.diag(S) # Matriz singunlar
        R = S.shape[1] # 
        print(f"{S}\n")
        del_ = int(input(f"Escriba la cantidad de documentos no pertinentes: "))
        k = R - del_ # Valor para saber cuantos docs eliminar de la matriz
        Tp = np.delete(T, np.s_[k::], 1)
        Sp = np.delete(np.delete(S, np.s_[k::], 0), np.s_[k::], 1)
        Dp = np.delete(D, np.s_[k::], 0)

        new_freqT = Tp @ Sp @ Dp

        # Variable para la sumatoria de la formula
        M = new_freqT.shape[0]

        # Extraction of doc A and doc B from freqT
        doc_A = new_freqT[:,doc_A]
        doc_B = new_freqT[:,doc_B]
        
        sim_list = []
        zip_obj = zip(doc_A, doc_B)

        for i in range(0, M):
            for doc_A, doc_B in zip_obj:
                sim_list.append(abs(doc_A - doc_B))

        # print(f"{sim_list}\t", end='')
        doc_similarity = 0

        for i in sim_list:
            doc_similarity += i

        # Product intern distance of the originial Matrix
        print()
        print(doc_similarity)

        return doc_similarity
        
    """-----------------Euclidian Distance-----------------"""
    def euclidianDistance(self, query_list, instance):

        matrix_doc = instance.getMatrix()
        distances_list = []

        for i in range((instance.docs-1)+1):
            list_ = []
            for j in range(len(instance.termsList)):
                column_term_freq = matrix_doc[j][i]
                list_.append(column_term_freq)

            if len(list_) == len(instance.termsList):        
                og_simList = []
                for i in query_list:
                    for j in list_:
                        og_simList.append(i - j)

                og_powList = np.power(og_simList, 2)
                og_distance = sqrt(sum(og_powList))
                distances_list.append(og_distance)
                
        best_three = sorted(range(len(distances_list)), key = lambda sub: distances_list[sub])[:3]

        return best_three

    """-----------------Q query-----------------"""
    def qQuery(self, query):
        directory = "./Queries/"
        filename = "UsersQuery.txt"
        query_terms = []
        list_query = []
        distances = []
        stemmer = ds.DoubleStemmer()
        freqt_ = freqt.FreqT()
        terms = freqt_.termsList
        matrix = freqt_.getMatrix()

        # 1. Creating a directory, a file and saving the query Q in a file.
        file_path = os.path.join(directory, filename)

        if not os.path.isdir(directory):
            os.mkdir(directory)

        if not os.path.exists(filename):
            with open(file_path, 'w') as file:
                file.write(query)

        # 2. Stemming the query Q from the created file
        stemmer.stemText(file_path)

        # 3. Recuperar los terminos lematizados del archivo.
        file = open("./LemQueries/UsersQuery LEM.txt", 'r')

        # 4. Comparar la lista de terminos de freqT con cada termino de la conuslta.
            # Si el termino de Q != termino en la lista de freqT --> a la lista vacía le ponemos un cero en esa posición.
            # Si es lo contrario entonces pon un 1 en esa posición de la "lista vacía".
        # print(len(terms))
        for each_term in file.readlines():
            query_terms.append(each_term[:-1])

        # print(query_terms)
        for term in query_terms:
            for dbTerm in terms:
                if term == dbTerm:
                    list_query.append(1)
                else:
                    list_query.append(0)
        
        # print(list_query)

        # 5. Sacar la distancia de la consulta Q con cada documento.
        query = self.euclidianDistance(list_query, freqt_)

        # 6. Regresar las 3 distancias más cortas.
        return query