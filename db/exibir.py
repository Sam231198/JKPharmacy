from db.connectSQLite import sqlite

sqlite.execute("DROP DATABASE db_jkpharmacy")
sqlite.close()