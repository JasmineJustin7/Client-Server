import sqlite3

conn = sqlite3.connect("test_databases.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT, password TEXT)")

# insert data
cursor.execute("INSERT INTO USERS (username, password) VALUES ('ciera.simon', ciera12345)")
cursor.execute("INSERT INTO USERS (username, password) VALUES ('jasmine.justin', jasmine12345)")
cursor.execute("INSERT INTO USERS (username, password) VALUES ('jia.w', jw12345)")
cursor.execute("INSERT INTO USERS (username, password) VALUES ('cjbonario98', cj98)")
cursor.execute("INSERT INTO USERS (username, password) VALUES ('person.random', person12345)")
cursor.execute("INSERT INTO USERS (username, password) VALUES ('sora.roxas', org13)")
cursor.execute("INSERT INTO USERS (username, password) VALUES ('yozora.shibuya', kingdomh4!)")

conn.commit()
conn.close()
