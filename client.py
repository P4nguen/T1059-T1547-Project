import socket
import sqlite3

def store_command_output(command, output):
    conn = sqlite3.connect('command_outputs.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO command_outputs (command, output)
    VALUES (?, ?)''', (command, output))

    conn.commit()
    conn.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('your_ip_addreess', 12345))  # Replace with the correct IP address

    while True:
        command = input("Enter the command to execute (or 'exit' to quit): ")
        client_socket.send(command.encode("utf-8"))
        print(f"Sent command: {command}")

        if command.lower() == 'exit':
            print("Exiting the client...")
            client_socket.close()
            break

        result = client_socket.recv(4096).decode("utf-8")
        print(f"Received result: {result}")

        # Store the command and its output in the database
        store_command_output(command, result)

if __name__ == "__main__":
    start_client()
