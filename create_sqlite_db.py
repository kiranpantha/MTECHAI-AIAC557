import sqlite3

# Connect to the database or create one if it doesn't exist
conn = sqlite3.connect('my_data.sqlite3')
c = conn.cursor()

# Create a table to store the scraped data
c.execute('''
    CREATE TABLE IF NOT EXISTS scraped_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        name TEXT,
        weightUnit TEXT,
        minimumAmount TEXT,
        maximumAmount TEXT,
        averageAmount TEXT,
        UNIQUE(date, name) ON CONFLICT REPLACE
    )
''')

# Commit and close the connection
conn.commit()
conn.close()
