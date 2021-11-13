
class Board:
    def __init__(self, board_view):
        self.board_view = board_view  # the board

    def to_string(self):
        # returns a string
        to_print = ""
        for inList in self.board_view:
            to_print += '\n'
            for val in inList:
                to_print += str(val) + "  "
        return to_print

    def switch_slot(self, slot_number, sign):  # switches the slot with the sign(x or o)
        # could change later
        if slot_number <= 3:
            self.board_view[0][slot_number - 1] = sign
        elif 4 <= slot_number <= 6:
            if slot_number != 6:
                self.board_view[1][(slot_number % 3) - 1] = sign
            else:
                self.board_view[1][2] = sign
        elif 7 <= slot_number <= 9:
            if slot_number != 9:
                self.board_view[2][(slot_number % 3) - 1] = sign
            else:
                self.board_view[2][2] = sign
        else:
            print("The number given is not valid!")

    def create_new_board(self):  # creates a new board
        self.board_view = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def C_I_W(self):  # check if won
        for i in range(0, 3):
            if self.board_view[i][0] == self.board_view[i][1] == self.board_view[i][2]:
                return True

        for i in range(0, 3):
            if self.board_view[0][i] == self.board_view[1][i] == self.board_view[2][i]:
                return True
        # אלכסונים
        if self.board_view[0][0] == self.board_view[1][1] == self.board_view[2][2] or self.board_view[0][2] == \
                self.board_view[1][1] == self.board_view[2][0]:
            return True
        return False  # if no one has won

    def C_I_T(self):
        # checks if there is a tie
        flag = True
        for inList in self.board_view:
            for slot in inList:
                if slot != 'X' and slot != "O":
                    flag = False
        return flag
