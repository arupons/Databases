import MySQLdb
import datetime
import os

connection = MySQLdb.connect(
                host = '127.0.0.1',
                user = 'root',
                passwd = '')  # create the connection
cursor = connection.cursor()     # get the cursor
cursor.execute("USE header") # select the database
cursor.execute("SHOW databases")    # execute 'SHOW TABLES' (but data is not returned)
tables = cursor.fetchall()       # return data from last query
#print tables
#or iterate over the cursor:
for (table_name) in cursor:
        print("Procesando: ",table_name[0])
        print "mysqldump -h localhost -u root "+table_name[0]+" > "+table_name[0]+".sql"
        command = "mysqldump -h localhost -u root "+table_name[0]+" > "+table_name[0]+".sql"
        os.system(command)
        print("Procesado: ",table_name[0])