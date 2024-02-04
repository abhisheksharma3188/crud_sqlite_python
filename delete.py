import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Delete user by ID
user_id = 1  # Replace with the desired user ID

cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

# Commit the transaction and close the connection
conn.commit()
conn.close()
