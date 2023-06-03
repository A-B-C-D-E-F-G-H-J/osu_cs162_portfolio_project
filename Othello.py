# Author: Andrew Duc Nguyen
# GitHub username: A-B-C-D-E-F-G-H-J
# Date:
# Description:

class Player:
    """

    """
    def __init__(self, player_name, color, pieces=0):
        self._player_name = player_name
        self._color = color
        self._piece = 0

    def get_name(self):
        return self._player_name

    def get_color(self):
        return self._color

    def change_pieces(self, change):
        self._piece += change


class Othello:
    """

    """

    def __init__(self):
        self._board = []
        self._player_list = []
        for row in range(10):
            if row >= 1 and row <=8:
                row = ['.']*10
                row[0], row[9] = '*', '*'
                self._board.append(row)
            else:
                self._board.append(['*']*10)
        self._board[4][4], self._board[5][5] = 'O', 'O'
        self._board[4][5], self._board[5][4] = 'X', 'X'
        self._option_1 = {"black": "X",
                        "white": "O",
                        "empty": ".",
                        "edge": "*",
                        }
        self._option_opp = {"black": 'O',
                          "white": 'X',
                        "O": 'black',
                        "X": 'white'}

    def print_board(self):
        """"""
        for row in self._board:
            print(*row)

    def create_player(self, player_name, color):
        """"""
        self._player_list.append(Player(player_name, color))

    def return_winner(self):
        white, black = 0, 0
        for row in self._board:
            for char in row:
                if char == 'O':
                    white += 1
                if char == 'X':
                    black += 1
        if white == black:
            return "It's a tie!"
        if white > black:
            for player in self._player_list:
                if player.get_color() == "white":
                    return f"Winner is white player: {player.get_name()}"
        else:
            for player in self._player_list:
                if player.get_color() == "black":
                    return f"Winner is black player: {player.get_name()}"

    def flip_pieces(self, color, conversion, r, c):
        if self._board[r][c] == self._option_1[color]:
            for coord in conversion:
                (r, c) = coord
                self._board[r][c] = self._option_1[color]

    def update_board(self, color, piece_position):
        (r, c) = piece_position
        conversion = []
        if self._board[r + 1][c] == self._option_opp[color]:
            temp = (r, c)
            r += 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r += 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp
        if self._board[r - 1][c] == self._option_opp[color]:
            temp = (r, c)
            r -= 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r -= 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp
        if self._board[r][c + 1] == self._option_opp[color]:
            temp = (r, c)
            c += 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                c += 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp
        if self._board[r][c - 1] == self._option_opp[color]:
            temp = (r, c)
            c -= 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                c -= 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp
        if self._board[r + 1][c + 1] == self._option_opp[color]:
            temp = (r, c)
            r += 1
            c += 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r += 1
                c += 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp
        if self._board[r + 1][c - 1] == self._option_opp[color]:
            temp = (r, c)
            r += 1
            c -= 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r += 1
                c -= 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp
        if self._board[r - 1][c + 1] == self._option_opp[color]:
            temp = (r, c)
            r -= 1
            c += 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r -= 1
                c += 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp
        if self._board[r - 1][c - 1] == self._option_opp[color]:
            temp = (r, c)
            r -= 1
            c -= 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r -= 1
                c -= 1
            self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp

        print(f"Board updated. You have flipped a total of "
                f"{len(conversion)} of your opponent's pieces")

    def return_available_positions(self, color):
        result = set()
        rows, cols = len(self._board), len(self._board[0])
        for r in range(rows):
            for c in range(cols):
                if self._board[r][c] == self._option_1[color]:
                    if self._board[r + 1][c] == self._option_opp[color]:
                        temp = (r, c)
                        r += 1
                        while self._board[r][c] == self._option_opp[color]:
                            r += 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
                    if self._board[r - 1][c] == self._option_opp[color]:
                        temp = (r, c)
                        r -= 1
                        while self._board[r][c] == self._option_opp[color]:
                            r -= 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
                    if self._board[r][c + 1] == self._option_opp[color]:
                        temp = (r, c)
                        c += 1
                        while self._board[r][c] == self._option_opp[color]:
                            c += 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
                    if self._board[r][c - 1] == self._option_opp[color]:
                        temp = (r, c)
                        c -= 1
                        while self._board[r][c] == self._option_opp[color]:
                            c -= 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
                    if self._board[r + 1][c + 1] == self._option_opp[color]:
                        temp = (r, c)
                        r += 1
                        c += 1
                        while self._board[r][c] == self._option_opp[color]:
                            r += 1
                            c += 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
                    if self._board[r + 1][c - 1] == self._option_opp[color]:
                        temp = (r, c)
                        r += 1
                        c -= 1
                        while self._board[r][c] == self._option_opp[color]:
                            r += 1
                            c -= 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
                    if self._board[r - 1][c + 1] == self._option_opp[color]:
                        temp = (r, c)
                        r -= 1
                        c += 1
                        while self._board[r][c] == self._option_opp[color]:
                            r -= 1
                            c += 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
                    if self._board[r - 1][c - 1] == self._option_opp[color]:
                        temp = (r, c)
                        r -= 1
                        c -= 1
                        while self._board[r][c] == self._option_opp[color]:
                            r -= 1
                            c -= 1
                        if self._board[r][c] == self._option_1["empty"]:
                            result.add((r, c))
                        (r, c) = temp
        return list(result)

    def make_move(self, color, piece_position):
        (r, c) = piece_position
        self._board[r][c] = self._option_1[color]
        self.update_board(color, piece_position)
        print("Move successful. Here is the update board:")
        self.print_board()
        print(f"{self._option_opp[self._option_1[color]]} player, here are "
              f"your available moves:  ")
        print(self.return_available_positions(self._option_opp[self._option_1[
            color]]))

    def play_game(self, player_color, piece_position):
        if len(self.return_available_positions(player_color)) == 0:
            return self.return_available_positions(player_color)
        if piece_position not in self.return_available_positions(player_color):
            print("Invalid Move, here are the valid moves:")
            print(self.return_available_positions(player_color))
        else:
            self.make_move(player_color, piece_position)
        if len(self.return_available_positions(player_color)) == 0 and len(
                self.return_available_positions(self._option_opp[
                                                    player_color])) == 0:
            return self.return_winner()





game = Othello()

game.print_board()
Andrew = game.create_player("Andrew", "black")
var = game.return_available_positions("black")
print(var)
game.play_game("black", (6,5))
print(game.return_available_positions("white"))
game.play_game("white", (6,6))
game.play_game("white", (7,5))
game.play_game("black", (8,5))