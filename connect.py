import sqlite3

def _config():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        print("Database created and Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return sqliteConnection

def get_resposity_url(_config):
    try:
        cursor = _config.cursor()
        response = cursor.execute('select * from reposity_url')
        print(response)
    except expression as identifier:
        pass