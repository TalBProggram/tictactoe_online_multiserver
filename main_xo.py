import socket
import SubServer
import select
import Player


max_msg_length = 1000
server_ip = '0.0.0.0'
server_port = 5555
loss_massage = "You have lost the game :("
win_massage = "You have won the game :)"
tie_massage = "It's a tie!"
# setup server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen()

client_sockets = []
client_ips = []
player_list = []
running_subserver_list = []  # the currently running subservers
stop_loop = False

# a loop that divides the players joining into subservers
while not stop_loop:
    readList, writeList, errorList = select.select([server_socket] + client_sockets, client_sockets, [])
    # first loop that adds new players

    for currentSocket in readList:

        if currentSocket is server_socket:
            connection, client_address = currentSocket.accept()
            client_sockets.append(connection)
            client_ips.append(client_address)
            # add a player
            player_list.append(Player(client_address, "", connection))
            print("A player joined - ", client_address)

            if len(client_sockets) == 2:  # if two players joined, stop looking for players
                newSubServer = SubServer(player_list.pop(), player_list.pop())  # create a new subserver
                newSubServer.board.create_new_board()  # create the board
                running_subserver_list.append(newSubServer)  # add to running subserver list
                # removes the players from player_list, puts them in a subserver object and adds them
                # to the running subservers list
                print("A new Subserver has been created - ",
                      newSubServer.player1.player_ip, newSubServer.player2.player_ip)
        else:
            # if the subserver sends data the players turn does not matter, it matters only when
            # the server has to send data to the subserver
            for socket_subServer in running_subserver_list:

                if socket_subServer.player1.mySocket == currentSocket:
                    # read from player1
                    data = socket_subServer.player1.mySocket.recv(max_msg_length).decode()  # receive the massage
                    socket_subServer.board.switch_slot(int(data), socket_subServer.player1.player_sign)
                    # switch the turn
                    socket_subServer.turn = socket_subServer.player2

                if socket_subServer.player2.mySocket == currentSocket:
                    # read from player2
                    data = socket_subServer.player2.mySocket.recv(max_msg_length).decode()  # receive the massage
                    socket_subServer.board.switch_slot(int(data), socket_subServer.player2.player_sign)
                    # switch the turn
                    socket_subServer.turn = socket_subServer.player1

    for currentSocket in writeList:
        # loop on writeable sockets
        for socket_subServer in running_subserver_list:

            if socket_subServer.Check_if_won_in():
                # if someone has won the game
                # send the lost and won massages
                socket_subServer.turn.mySocket.send(win_massage.encode())

                if socket_subServer.turn == socket_subServer.player1:
                    # send loss massage
                    socket_subServer.player2.mySocket.send(loss_massage.encode())

                else:
                    socket_subServer.player1.mySocket.send(loss_massage.encode())

                # close the sockets
                socket_subServer.player1.mySocket.close()
                socket_subServer.player2.mySocket.close()
                # remove from subserver list
                running_subserver_list.remove(socket_subServer)

            if socket_subServer.Check_if_tie_in():
                # send the players the tie massages
                socket_subServer.player1.mySocket.send(tie_massage.encode())
                socket_subServer.player2.mySocket.send(tie_massage.encode())
                # close the sockets
                socket_subServer.player1.mySocket.close()
                socket_subServer.player2.mySocket.close()
                # remove from subserver list
                running_subserver_list.remove(socket_subServer)

            if socket_subServer.turn.mySocket == currentSocket:
                # if the socket ready for writing is the player which its his turn

                if socket_subServer.turn == socket_subServer.player1:
                    socket_subServer.player1.mySocket.send(socket_subServer.board.to_string().encode())  # send
                    # the board to the socket

                if socket_subServer.turn == socket_subServer.player2:
                    socket_subServer.player2.mySocket.send(socket_subServer.board.to_string().encode())  # send
                    # the board to the socket



