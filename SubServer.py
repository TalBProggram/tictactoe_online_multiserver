from Board import Board
from Player import Player


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

    def check_if_over(self):  # if its over, it returns True , sign. if not over it returns False,'*'
        for i in range(0, 3):
            if self.board.board_view[i][0] == self.board.board_view[i][1] == self.board.board_view[i][2]:
                return True

        for i in range(0, 3):
            if self.board.board_view[0][i] == self.board.board_view[1][i] == self.board.board_view[2][i]:
                return True
        # אלכסונים
        if self.board.board_view[0][0] == self.board.board_view[1][1] == self.board.board_view[2][2] or self.board.board_view[0][2] == \
                self.board.board_view[1][1] == self.board.board_view[2][0]:
            return True
        return False  # if no one has won

    def check_if_tie(self):
        # checks if there is a tie
        flag = True
        for inList in self.board.board_view:
            for slot in inList:
                if slot != 'X' and slot != "O":
                    flag = False
        return flag
