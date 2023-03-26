#create table scripts
import sqlite3



connection = sqlite3.connect('ElectionData.db')
cursor = connection.cursor()

#  # THE INTEGER PRIMARY KEY IS AN AUTOINCREMENT FEATURE

# cursor.execute( "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,  username text, password text)")


connection.commit()

connection.close()