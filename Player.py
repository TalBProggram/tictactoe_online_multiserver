
class Player:
    def __init__(self, player_ip, player_socket):
        self.player_ip = player_ip
        self.player_sign = None
        self.mySocket = player_socket

    def set_player_sign(self, given_player_sign):
        self.player_sign = given_player_sign

    def __str__(self):  # print
        return self.player_ip[0] + ', ' + self.player_sign

    def to_string(self):
        return self.player_ip[0] + ', ' + self.player_sign
