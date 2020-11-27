import os.path
import DoubleStemmer as ds
import LSI as lsi
import BaseDeDatos as db
import FreqT as freqt
import SimDis as sd
import FreqT as freqt

def main():

    database = db.BaseDeDatos()
    simdis = sd.SimDis()
    
    database.dropCreate()
    lsi_ = lsi.LSI()
    stemmer = ds.DoubleStemmer()
    
    directory = './TestFiles/'
    list_files = os.listdir(directory)

    for file in list_files:
        if file.endswith(".txt"):
            stemmer.stemText(f"TestFiles/{file}")

    lsi_.listFiles()
    lsi_.retrieveData()
    print("\nTEMA SELECCIONADO: FACTORES GLOBALES Y AMBIENTALES\n")

    while 1:

        print("1. Ver los documentos de prueba")
        print("2. Evaluar dos documentos por su grado de similiud")
        print("3. Dar una consulta Q")
        print("4. Cerrar el programa")
        users_input = int(input("Escoge una de las opciones de arriba: "))

        if users_input == 1:
            print()
            
            for file in list_files:
                print(f"{list_files.index(file)+1}. {file}")

            print()
        
        elif users_input == 2:
            freqTMatrix = freqt.FreqT()
            print("1. Evaluar con el producto interno.")
            print("2. Evaluar con coeficientes de dice.")
            print("3. Evaluar con la distancia de Manhattan.")
            evaluacion = int(input("Escoge una de las opciones: "))

            print("\n\nPOR FAVOR ESCOGE DOS NÚMEROS ENTRE 1 Y 10...\n\n")
            doc_1 = int(input("Escribe el numero del 1° documento: "))
            doc_2 = int(input("Escribe el numero del 2° documento: "))
            
            if evaluacion == 1:
                simdis.internProduct(doc_1-1, doc_2-1, freqTMatrix.getMatrix())
            elif evaluacion == 2:
                simdis.diceCoeficients(doc_1-1, doc_2-1, freqTMatrix.getMatrix())
            else:
                simdis.manhattanDistance(doc_1-1, doc_2-1, freqTMatrix.getMatrix())
        
        elif users_input == 3:
            print("FAVOR DE INSERTAR TU CONSULTA EN INGLÉS.\n")
            users_query = str(input("Inserta tu consulta: "))
            best_three = simdis.qQuery(users_query)
            print(f"\nLos mejores documentos son:")
            print()
            
            for file in list_files:
                for best in best_three:
                    if best == list_files.index(file):
                        print(file)
            print()
        elif users_input == 4:
            break
        
        else:
            print("OPCIÓN INVALIDA!!!")

if __name__ == '__main__':
    main()
