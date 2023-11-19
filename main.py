import sqlite3

connection = sqlite3.connect("Dz10.sl3", 5)

cur = connection.cursor()

cur.execute("CREATE TABLE Dz_10 (name TEXT, temperature TEXT);")

connection.commit()
connection.close()