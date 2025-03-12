import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('migrations_test.db')
cursor = conn.cursor()

# Query the schema of the students table
cursor.execute("PRAGMA table_info(students);")
columns = cursor.fetchall()

# Print the schema
for column in columns:
    print(column)

# Close the connection
conn.close()
