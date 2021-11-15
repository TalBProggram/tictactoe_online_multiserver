# client for XO game

import socket
import select
from os import system
max_massage_length = 2000
server_ip = '127.0.0.1'
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
client_socket.connect((server_ip, server_port))  # connect to main server

while True:
    data = client_socket.recv(max_massage_length).decode()
    system('cls')  # clear screen
    if "won" in data or "lost" in data:
        print(data)
        break
    print(data)
    if "tie" in data:
        break
    numberToSwitch = input("Which slot do you choose: ")
    if len(numberToSwitch) == 1 and type(numberToSwitch) == str and 10 > int(numberToSwitch) > 0:  # check if input
        # is acceptable
        client_socket.send(numberToSwitch.encode())
    else:
        print("You have to enter ONE number between 1-9...")
        input("Which slot do you choose: ")
        client_socket.send(numberToSwitch.encode())

client_socket.close()