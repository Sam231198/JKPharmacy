from db.connectSQLite import sqlite

cursor = sqlite.cursor()

cursor.execute("""
              CREATE TABLE teste(
                nome varchar(30)
              )
              """)
cursor.close()
sqlite.close()