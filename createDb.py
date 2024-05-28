import sqlite3

def create_database():
    conn = sqlite3.connect('command_outputs.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE command_outputs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        command TEXT NOT NULL,
        output TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
