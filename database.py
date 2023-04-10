import sqlite3


def create_tables():
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    # Check if the addresses table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='addresses'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Create the addresses table if it doesn't exist
        cursor.execute('''
                CREATE TABLE addresses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    street TEXT NOT NULL,
                    city TEXT NOT NULL,
                    state TEXT NOT NULL,
                    zip TEXT NOT NULL,
                    latitude REAL,
                    longitude REAL
                )
            ''')
        print("Table 'addresses' created successfully.")
    else:
        print("Table 'addresses' already exists.")

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
