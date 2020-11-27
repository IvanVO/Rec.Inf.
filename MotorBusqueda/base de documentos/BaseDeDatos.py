import os

import mysql.connector
from mysql.connector import Error, MySQLConnection
 
credentials = {
    'host':"localhost",
    'user':'your_username',
    'password':'your_password',
    'database':'baseDocumentos'
}

class BaseDeDatos:

    def __init__(self):
        pass
    
    def dropCreate(self):
        
        try:
            connection = mysql.connector.connect(**credentials)
            cursor = connection.cursor()
            
            cursor.execute("DROP DATABASE IF EXISTS baseDocumentos")
            cursor.execute("CREATE DATABASE baseDocumentos")

        except mysql.connector.Error as error:
            print(error)
        
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()

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
        

    def retreiveFromDatabase(self, tables):

        try:
            connection = mysql.connector.connect(**credentials)
            cursor = connection.cursor()

            tuple_list = []

            for table in tables:

                table_list = []
                query = f"SELECT term, frequency FROM {table}"
                cursor.execute(query)
                records = cursor.fetchall()

                for record in records:
                    #tuple_list.append(record)
                    table_list.append(record)

                table_list.sort()
                tuple_list.append(table_list)
            
            return tuple_list

        except mysql.connector.Error as error:
            print(error)
        
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
