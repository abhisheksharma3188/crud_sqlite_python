import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Insert new user
name = "John Doe"
email = "john.doe@example.com"

cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))

# Commit the transaction and close the connection
conn.commit()
conn.close()
