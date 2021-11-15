import Board
import Player


class SubServer:
    def __init__(self, first_player, second_player):
        self.board = Board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])  # the subserver's board
        self.player1 = first_player
        self.player2 = second_player
        self.turn: Player = self.player1  # a variable which has the current player that should play

    def __str__(self):
        # print the status
        return "Player 1: " + self.player1.to_string() + "'\n'Player 2: " + self.player2.to_string() + \
               f"'\n'Its {self.turn.to_string()}'s turn." + "\n" + "Current board = '\n'" + self.board.to_string()

    def set_signs(self):
        # set signs for the players
        self.player1.set_player_sign("X")
        self.player2.set_player_sign("O")
    def Check_if_won_in(self):
        if check_if_over(self.board):
            # return the current players turn
            return self.turn  # returns the player that won the game

    def Check_if_tie_in(self):
        if check_if_tie(self.board):
            return True  # if its a tie return true



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
