import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Update user by ID
user_id = 1  # Replace with the desired user ID
new_email = "new_email@example.com"

cursor.execute('UPDATE users SET email = ? WHERE id = ?', (new_email, user_id))

# Commit the transaction and close the connection
conn.commit()
conn.close()
