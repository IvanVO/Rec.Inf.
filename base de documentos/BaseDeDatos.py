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

    def insertContent(self, documents_content):
        
        connection = mysql.connector.connect(**credentials)
        cursor = connection.cursor()
        print("Inserting document's content to the database")

        try:
            cursor = connection.cursor()
            query = "INSERT INTO documentos (doc) VALUES (%s)"
            
            # Insert data to table
            insert_content = (documents_content,)
            result = cursor.execute(query, insert_content)
            connection.commit()
            
            print("documents content inserted successfully as a text into documentos table", result)

        except mysql.connector.Error as error:
            print("Failed inserting document's content data to table documentos {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

   