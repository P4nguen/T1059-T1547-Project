import sqlite3

def view_database():
    conn = sqlite3.connect('command_outputs.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM command_outputs')
    rows = cursor.fetchall()

    for row in rows:
        command_id, command, output = row
        print(f"Command ID: {command_id}")
        print(f"Command: {command}")
        print(f"Output: {output}")
        print('-' * 50)

    conn.close()

if __name__ == "__main__":
    view_database()
