## Requirements

To run this project, you will need the following:

Python 3.x installed on both the server and client machines.

SQLite3 (included with Python).

Basic knowledge of using a terminal or command line interface.


## Files Included

client.py: The client script to send commands to the server.

server.py: The server script to receive and execute commands.

createDb.py: A script to create the SQLite database and table.

view_Db.py: A script to view the contents of the database.

command_outputs.db: The SQLite database where command outputs are stored. (you should run the createDb.py on the terminal for this to show up).

 Windows: `python createDb.py` Linux/Mac: `python3 createDb.py`


## Step 1: Edit client.py

In the client.py file, update the IP address to the IP address of the server machine (victim's machine).

`client_socket.connect(('192.168.169.117', 12345)) #Example`


## Step 2: Run createDb.py

Run the create_db.py script on the client machine to create the SQLite database and table.

`python3 create_db.py`

You can delete this and create it again to reset the database.

`rm createDb.py`


## Step 3.1: Setup the Server

On the server machine, create a systemd service to ensure the server script runs on boot.

`sudo nano /etc/systemd/system/server.service`


## 3.2: Add the following content to the file
```
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
```

## 3.3: Reload the systemd daemon and start the service:
```
sudo systemctl daemon-reload

sudo systemctl start server.service

sudo systemctl enable server.service
```

## Step 4: Running the Client

Run the command `python3 client.py` on your terminal while you are on your projects directory 

-> .../Desktop/client.py

Enter the command you want to execute on the server machine. The output will be displayed and stored in the SQLite database.


## Step 5: Reviewing the Database

To view the contents of the database, run the viewDb.py script on the client machine.

`python3 view_db.py`

This will print the stored command outputs.



That's all, you can find more commands for your needs in the text file I added named 'serverServiceCommand.txt' 

## Disclaimer!

This project is created for educational and research purposes only. The intention is to demonstrate and practice concepts related to cybersecurity and ethical hacking in a controlled environment. Unauthorized access to computer systems, networks, or any other form of hacking without explicit permission from the owner is illegal and unethical.

The author of this project does not endorse or condone any illegal activities or misuse of the information provided. Use this knowledge responsibly and only on systems you own or have explicit permission to test.

By using the tools and techniques described in this project, you agree to the following:

You will not use this project or any information within it for any illegal activities or unauthorized access to systems.

You understand the risks and legal implications associated with cybersecurity activities.

You will only perform testing on systems you own or have been granted explicit permission to test.

The author takes no responsibility for any damage caused by the misuse of this project.



