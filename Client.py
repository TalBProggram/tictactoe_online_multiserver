# client for XO game

import socket
import select
import sys
from os import system
import platform

max_massage_length = 2000
server_ip = '127.0.0.1'
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
client_socket.connect((server_ip, server_port))  # connect to main server

current_os = platform.system()
# clear screen and write to the client that its waiting for players
if current_os == 'Windows':
    system('cls')  # clear screen
else:
    system("clear")
print("Waiting for another player...")
while True:
    data = client_socket.recv(max_massage_length).decode()
    if current_os == 'Windows':
        system('cls')  # clear screen
    else:
        system("clear")
    if "won" in data or "lost" in data or "tie" in data:
        print(data)
        # play again part
        print("Would you like to play again?")
        while True:
            answer = input("Y/N\n>>>")
            if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes":
                client_socket.close()  # close the socket
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
                client_socket.connect((server_ip, server_port))  # rejoin to main server
                print("Yay! waiting for another player...")
                break
            elif answer == "n" or answer == "N" or answer == "no" or answer == "No":
                sys.exit()  # close the window
            else:
                print("Please enter a valid answer(Y/N)...")
        continue  # go to the start of the loop
    elif "disconnected" in data or data == "":
        if data == "":
            print("The other player has disconnected,\nwould you like to join another game?")
        print(data)
        # loop until the user answers
        while True:
            answer = input("Y/N\n>>>")
            if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes":
                client_socket.close()  # close the socket
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
                client_socket.connect((server_ip, server_port))  # rejoin to main server
                print("Yay! waiting for another player...")
                break
                # return to the beginning of the loop
            elif answer == "n" or answer == "N" or answer == "no" or answer == "No":
                sys.exit()  # close the window
            else:
                print("Please enter a valid answer(Y/N)...")
        continue
    else:
        print(data)
    # loop until you get an acceptable input
    right_input = False  # loop stopper
    while not right_input:
        numberToSwitch = input("Which slot do you choose: ")
        if len(numberToSwitch) == 1 and \
                numberToSwitch in "123456789" and \
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
