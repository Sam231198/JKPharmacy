from db.connectSQLite import sqlite
cursor = sqlite.cursor()

cursor.execute("INSERT INTO teste(nome) VALUES ('Samuel')")
sqlite.commit()

cursor.close()
sqlite.close()