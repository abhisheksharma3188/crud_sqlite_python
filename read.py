import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Retrieve all users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

# Display the users
for user in users:
    print(user)

# Close the connection
conn.close()
