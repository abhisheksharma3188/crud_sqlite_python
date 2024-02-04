import sqlite3

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Commit the transaction and close the connection
conn.commit()
conn.close()
