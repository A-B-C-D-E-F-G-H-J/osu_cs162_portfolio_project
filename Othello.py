# Author: Andrew Duc Nguyen
# GitHub username: A-B-C-D-E-F-G-H-J
# Date:
# Description:

class Player:
    """

    """

    def __init__(self, player_name, color):
        self.player_name = player_name
        self.color = color



class Othello:
    """

    """

    def __init__(self):
        self._board = []
        for row in range(10):
            if row >= 1 and row <=8:
                row = ['.']*10
                row[0], row[9] = '*', '*'
                self._board.append(row)
            else:
                self._board.append(['*']*10)
        self._board[4][4], self._board[5][5] = 'O', 'O'
        self._board[4][5], self._board[5][4] = 'X', 'X'


    def print_board(self):
        """"""
        for row in self._board:
            print(*row)


game = Othello()

game.print_board()
