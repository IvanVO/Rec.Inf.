import os

import mysql.connector
from mysql.connector import Error, MySQLConnection
 

credentials = {
    'host':"localhost",
    'user':'ivan',
    'password':'@Vioa_1999',
    'database':'baseDocumentos'
}
class BaseDeDatos:
    def __init__(self):
        pass

    def read_file(self, filename):
        with open(filename, 'rb') as f:
            file = f.read()

        return file

    def insert_blob(self, filename):
        connection = mysql.connector.connect(**credentials)
        cursor = connection.cursor()
        print("Inserting BLOB into documentos table")
        try:
            cursor = connection.cursor()
            query = "INSERT INTO documentos (doc) VALUES (%s)"
            file = self.read_file(filename)

            # Convert data into tuple format
            insert_blob_tuple = (file,)
            result = cursor.execute(query, insert_blob_tuple)
            connection.commit()
            print("file inserted successfully as a BLOB into documentos table", result)

        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def write_file(self, data, filename):
        with open(filename, 'wb') as f:
            f.write(data)

    def read_blob(self, doc_id):
        try:
        connection = mysql.connector.connect(**credentials)

        cursor = connection.cursor()
        read_binary_file = "SELECT * from documentos where id = %s"

        cursor.execute(read_binary_file, (doc_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Content: \n\n", row[1])
            image = row[2]
            file = row[3]
            print("Storing content on disk \n")
            self.write_file()
            write_file(file, bioData)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")