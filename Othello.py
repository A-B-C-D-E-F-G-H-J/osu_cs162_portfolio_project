# Author: Andrew Duc Nguyen
# GitHub username: A-B-C-D-E-F-G-H-J
# Date: 06/09/2023
# Description: A program for the Othello board game in text form. Has a
#               Player class and an Othello class.

class Player:
    """
    Creates a Player object that is used to represent one of the two players
    playing Othello.

    :param player_name: The name of the player
    :param color: The color of the player's pieces (white/black)
    :param pieces: The number of pieces that the player has on the board.
    """
    def __init__(self, player_name, color, pieces=0):
        """
        Initializes the Player class

        :param player_name: The name of the player
        :param color: The color of the player's pieces (white/black)
        :param pieces: The number of pieces that the player has on the board.
        """
        self._player_name = player_name
        self._color = color
        self._piece = 0

    def get_name(self):
        """
        Returns the name of the player object
        :return: self._player_name as a string
        """
        return self._player_name

    def get_color(self):
        """
        Returns the color of the player's piece

        :return: self._color as a string
        """
        return self._color

    def change_pieces(self, change):
        """
        Adjusts the number of pieces that the player has on the board

        :param change: int => the number of pieces that are added or
        subtracted from the total amount of pieces that the player had on the board
        :return: self_piece as an integer
        """
        self._piece += change


class Othello:
    """
    Creates Othello object to play the Othello game.

    Methods:
        1. print_board
            prints the current board and all the pieces on it.
        2. create_player
            creates a player object, including their name and color
        3. return_winner
            calculates the number of pieces on the board that each player has
            and returns the player with the most pieces as the winner or a tie
            if the number of pieces is the same.
        4. flip_pieces
            converts the appropriate opposing pieces to the current player's
            color
        5. update_board
            iterates through the board and finds which pieces need to be
            flipped. Will flip the pieces and return the number of pieces
            that were flipped
        6. return_available_positions
            iterates through the board and finds the valid positions on the
            board that the current player can place a piece on.
        7. make_move
            takes in the current player's choice valid position that they
            want to place a piece on and places that piece on the board.
        8. play_game
            is the full move of the current player. This includes checking
            the available positions, validating if the current move is valid,
            placing the piece, flipping the opponent's pieces, and finding
            out if a winner must be decided
    """

    def __init__(self):
        """
        Initiates the Othello object

        :param _board: represents the board that the game will be played on
        :param _player_list: holds the 2 player objects that will be playing
        Othello
        :param _option_1: an option dictionary used to convert from the word
        representation of a piece/space on the board and its symbol.
        :param _opption_opp: an option dictionary used to convert from the
        symbol representation of a piece/space on the board and its word.
        """
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

        self._option_1 = {  "black": "X",
                            "white": "O",
                            "empty": ".",
                            "edge": "*",
                            }
        self._option_opp = {"black": 'O',
                            "white": 'X',
                            "O": 'black',
                            "X": 'white',
                            }

    def print_board(self):
        """
        for each row in the board, each value is printed
        :return: prints the board
        """
        for row in self._board:
            print(*row)

    def create_player(self, player_name, color):
        """
        creates the player object used to play the Othello game and appends
        it to the _player_list

        :param player_name: str => player's name
        :param color: str => color player's pieces (white/black)
        """
        self._player_list.append(Player(player_name, color))

    def return_winner(self):
        """
        iterates through the board and counts the number of white and black
        pieces. If the number of both pieces are equal, the game is declared
        a tie. If not, the player with more pieces is declared to be the winner
        :return: Returns the winner of the Othello game or a tie if number of pieces is the same
        """
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
        """
        takes in the conversion list coordinates and converts those pieces to
        the current's player's pieces

        :param color: str => color of the pieces of the current player
        :param conversion:  [list] => list of tuples, where each tuple is a
                            coordinate of the opposing player's piece that will
                            be converted
        :param r:  int => represents row of the position that is being
                            checked to see if a conversion should be done
        :param c:  int => represents the column of the position that is being
                            checked to see if a conversion should be done
        """
        if self._board[r][c] == self._option_1[color]:
            for coord in conversion:
                (r, c) = coord
                self._board[r][c] = self._option_1[color]

            return len(conversion)
        return 0

    def update_board(self, color, piece_position):
        """
        1. Takes in the position of the piece that the current player placed
        on the board.
        2. Visits each position that is adjacent to it.
        3. If an adjacent position has an opposing piece, it will move in
        that direction and add each opposing piece's coordinate to a
        conversion list.
        4. When it reaches a position that does not contain an opposing
        piece, if that position contains the current player's piece,
        all opposing pieces in the conversion list will be converted to the
        current player's pieces. If not, the conversion list will be emptied,
        and the next adjacent space will be visited.

        :param color: str => the color of the current player's pieces
        :param piece_position: tuple => the coordinate of the position that the
                                current player placed their piece on
        """
        (r, c) = piece_position
        conversion = []
        conversion_count = 0

        if self._board[r + 1][c] == self._option_opp[color]:
            temp = (r, c)
            r += 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r += 1
            conversion_count += self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp

        if self._board[r - 1][c] == self._option_opp[color]:
            temp = (r, c)
            r -= 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                r -= 1
            conversion_count += self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp

        if self._board[r][c + 1] == self._option_opp[color]:
            temp = (r, c)
            c += 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                c += 1
            conversion_count += self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp

        if self._board[r][c - 1] == self._option_opp[color]:
            temp = (r, c)
            c -= 1
            while self._board[r][c] == self._option_opp[color]:
                conversion.append((r, c))
                c -= 1
            conversion_count += self.flip_pieces(color, conversion, r, c)
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
            conversion_count += self.flip_pieces(color, conversion, r, c)
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
            conversion_count += self.flip_pieces(color, conversion, r, c)
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
            conversion_count += self.flip_pieces(color, conversion, r, c)
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
            conversion_count +=self.flip_pieces(color, conversion, r, c)
            conversion = []
            (r, c) = temp

        print(f"Board updated. You have flipped a total of "
                f"{conversion_count} of your opponent's pieces. Here is the "
              f"updated board:")

    def return_available_positions(self, color):
        """
        Iterates through the entire board and find the valid moves that the
        current player can make.

        1. Iterates through each position on the board. If a position
        contains the current player's piece, it will look at all adjacent
        spaces.
        2. If an adjacent space contains an opposing piece, it will move in
        that direction until a space does not have an opposing piece.
        3. If the space is an empty space, it will be marked as a valid
        position and its coordinates added to result, which will be converted
        to a list and returned.

        :param color: str => color of current player's piece
        :return: list of tuples. each tuple represents a coordinate that is a
                    a valid position
        """
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
        result = list(result)
        result.sort()
        return result

    def make_move(self, color, piece_position):
        """
        Comprises the process when a player makes a valid move.

        1. Takes in the position that the player will be putting their pieces on.
        2. Places the piece on the board.
        3. Calls the update_board method to convert any appropriate opponent
        pieces to the current player's color.

        :param color: str => color of the current player's pieces
        :param piece_position: tuple => represents the coordinate on the
        board that the player will place their piece on and update the board
        based on that position.
        :return: returns updated board
        """
        (r, c) = piece_position
        self._board[r][c] = self._option_1[color]
        self.update_board(color, piece_position)
        return self._board

    def play_game(self, player_color, piece_position):
        """
        Comprises the full process of a player's turn.

        1. Checks to see if there are any valid positions for the current player
            to place a piece. Return empty list if no valid positions.
            CALL METHOD => return_available_positions
        2. Checks to see if the current player's position chosen to place a
            piece is valid. If not, returns statement "invalid move"
            CALL METHOD => return_available_positions
        3. If position is valid, places the piece on the board and converts
            any appropriate opposing pieces. Updates board
            CALL METHOD => make_move
        4. After board is updates, checks to see if either player has any
            valid moves. If not, finds the winner.
            CALL METHOD => return_winner

        :param player_color: str => color of player's pieces
        :param piece_position: tuple => coordinate that represents the
        position that the player wants to place their piece on
        :return: 1. empty list if no available positions
                 2. "invalid move" if piece_position is invalid
                 3. winner if no more available positions for either player
        """
        if len(self.return_available_positions(player_color)) == 0:
            return []
            #return self.return_available_positions(player_color)
        if piece_position not in self.return_available_positions(player_color):
            return f"Invalid move"
                   #f"{self.return_available_positions(player_color)}"
        else:
            self.make_move(player_color, piece_position)
        if len(self.return_available_positions(player_color)) == 0 and len(
                self.return_available_positions(self._option_opp[
                                                    player_color])) == 0:
            return self.return_winner()





# game = Othello()
#
# game.print_board()
# Andrew = game.create_player("Andrew", "black")
# var = game.return_available_positions("black")
# print(var)
# game.play_game("black", (6,5))
# print(game.print_board())
# game.play_game("white", (6,6))
# print(game.print_board())
# game.play_game("white", (7,5))
# print(game.print_board())
# game.play_game("black", (8,5))
# print(game.print_board())
# print(game.play_game("white", (100, 100)))

# game = Othello()
# game.print_board()
# game.create_player("Helen", "white")
# game.create_player("Leo", "black")
# game.play_game("black", (6,5))
# game.print_board()
# game.play_game("white", (6,6))
# game.print_board()