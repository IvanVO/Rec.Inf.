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


    def createTable(self, filename):
        
        table_name = ""
        
        for name in filename:
            if name != " ":
                table_name += name
            else: 
                break

        try:
            connection = mysql.connector.connect(**credentials)
            cursor = connection.cursor()
            
            create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, term VARCHAR(50) NOT NULL, frequency INT(15) NOT NULL)"

            cursor.execute(create_table)

        except mysql.connector.Error as error:
            print(error)
        
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()

        return table_name

    def insertTermsFreq(self, table_name, term, frequency):
        try:
            connection = mysql.connector.connect(**credentials)
            cursor = connection.cursor()

            query = f"INSERT INTO {table_name} (term, frequency) VALUES (%s, %s)"

            values = (term, frequency,)
            
            cursor.execute(query, values)
            
            connection.commit()

        except mysql.connector.Error as error:
            print(error)
        
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
        

    def retreiveFromDatabase(self, table_name):
        try:            
            connection = mysql.connector.connect(**credentials)
            cursor = connection.cursor()

            query = f"SELECT term, frequency FROM {table_name}"
            cursor.execute(query)

            records = cursor.fetchall()
            
            for record in records:
                print(type(record))

        except mysql.connector.Error as error:
            print(error)
        
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()