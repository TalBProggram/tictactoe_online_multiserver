# client for XO game

import socket
import select
from os import system
import platform

max_massage_length = 2000
server_ip = '127.0.0.1'
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
client_socket.connect((server_ip, server_port))  # connect to main server

current_os = platform.system()
while True:
    data = client_socket.recv(max_massage_length).decode()
    if current_os == 'Windows':
        system('cls')  # clear screen
    else:
        system("clear")
    if "won" in data or "lost" in data or "tie" in data:
        print(data)
        break
    else:
        print(data)
    # loop until you get an acceptable input
    right_input = False  # loop stopper
    while not right_input:
        numberToSwitch = input("Which slot do you choose: ")
        if len(numberToSwitch) == 1 and \
                type(numberToSwitch) == str and \
                10 > int(numberToSwitch) > 0 and \
                numberToSwitch in data:  # check if input
            # is acceptable
            client_socket.send(numberToSwitch.encode())
            temp_board = client_socket.recv(max_massage_length).decode()
            if current_os == 'Windows':
                system('cls')  # clear screen
            else:
                system("clear")
            print(temp_board)
            right_input = True
        else:
            print("You have to enter ONE number between 1-9 which is not already taken!")

client_socket.close()
