
class Player:
    def __init__(self, player_ip, player_sign, player_socket):
        self.player_ip = player_ip
        self.player_sign = player_sign
        self.mySocket = player_socket

    def set_player_sign(self, given_player_sign):
        self.player_sign = given_player_sign

    def __str__(self):  # print
        return self.player_ip + ', ' + self.player_sign

    def to_string(self):
        return self.player_ip + ', ' + self.player_sign


########################################################

def check_if_over(board):  # if its over, it returns True , sign. if not over it returns False,'*'
    for i in range(0, 3):
        if board.board_view[i][0] == board.board_view[i][1] == board.board_view[i][2]:
            return True

    for i in range(0, 3):
        if board.board_view[0][i] == board.board_view[1][i] == board.board_view[2][i]:
            return True
    # אלכסונים
    if board.board_view[0][0] == board.board_view[1][1] == board.board_view[2][2] or board.board_view[0][2] == \
            board.board_view[1][1] == board.board_view[2][0]:
        return True
    return False  # if no one has won


def check_if_tie(board):
    # checks if there is a tie
    flag = True
    for inList in board.board_view:
        for slot in inList:
            if slot != 'X' and slot != "O":
                flag = False
    return flag

