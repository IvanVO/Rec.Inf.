import mysql.connector
from mysql.connector import Error


class BaseDeDatos:
    db = mysql.connector.connect(
        host = "localhost",
        user = "ivan",
        password = "@Vioa_1999",
        database = "baseDocumentos"
    )
    def __init__(self):
        pass
# cursor = db.cursor()

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def insertBLOB(self, testfile):
        
        # with open(testfile, 'rb') as file:
        #     binaryData = file.read()

        print("Inserting BLOB into documentos table")
        try:
            cursor = self.db.cursor()
            query = "INSERT INTO documentos (doc) VALUES (%s)"
            file = self.convertToBinaryData(testfile)

            # Convert data into tuple format
            insert_blob_tuple = (file,)
            result = cursor.execute(query, insert_blob_tuple)
            self.db.commit()
            print("file inserted successfully as a BLOB into documentos table", result)

        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))

        finally:
            if (self.db.is_connected()):
                cursor.close()
                self.db.close()
                print("MySQL connection is closed")