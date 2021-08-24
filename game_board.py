"""
 Author: Lori White
"""
import re
import player as p

class Game:
    """
     This represents the game
    """

    def __init__(self):
        """
         Intializes the game
        """
        self.is_over = False
        self.players = [p.Player(), p.Player()]
        self.game_board = [[None, None, None], [None, None, None], [None, None, None]]
        for row in range(0, len(self.game_board)):
            for column in range(0, 3):
                self.game_board[row][column] = " "

    def game_reset(self):
        """
         Resets the game
        """
        self.is_over = False
        self.players[0].player_reset()
        self.players[1].player_reset()
        for row in range(0, len(self.game_board)):
            for column in range(0, len(self.game_board[row])):
                self.game_board[row][column] = " "

    def place_token(self, player):
        """
         Updates the game board based on where the player chooses to place token.
        """
        placements = []
        while True:
            print("")
            self.display_game_board()
            try:
                placement = input(f"\nPlayer {player.player_name}, where would like to " \
                    + f"place your \"{player.game_token}\"?\n(Format: row,column where " \
                        + "top = 0, middle row = 1, bottom = 2,\n\tleft = 0, middle column = " \
                            +"1, and right = 2)\n").strip()
                placements = self.check_placement(placement)
            except AssertionError as error:
                print(f"\n{error} Please, try again.")
            else:
                break
        try:
            player.place_game_token()
            self.game_board[placements[0]][placements[1]] = player.game_token
        except AssertionError as error:
            print(f"{error}")

    def check_placement(self, placement):
        """
         Checks if the user entered the proper placement.
        """
        assert (re.search("^[0-2],[0-2]$", placement)), "Invalid placement format!"
        placements = [int(value) for value in placement.split(",")]
        assert (self.game_board[placements[0]][placements[1]] != "X" and \
            self.game_board[placements[0]][placements[1]] != "O"), "Invalid placement!"
        return placements

    def check_for_end(self):
        """
         Checks for the end of the game.
        """
        if self.players[0].num_placed_tokens >= 3 or \
            self.players[1].num_placed_tokens >= 3:
            # Checks for a win
            for num in range(0, len(self.players)):
                token = self.players[num].game_token
                token_3 = token + token + token
                # Checks for a diagonal win
                if token_3 == "".join([self.game_board[n][n] for n \
                    in range(0, len(self.game_board))]) or token_3 == \
                        "".join([self.game_board[n][len(self.game_board) \
                            - n - 1] for n in range(0, len(self.game_board))]):
                    self.is_over = True
                    self.players[num].is_winner = True
                else:
                    # Checks for a horizontal win
                    for row in range(0, len(self.game_board)):
                        if token_3 == "".join(self.game_board[row]):
                            self.is_over = True
                            self.players[num].is_winner = True
                            break
                    # Checks for a vertical win
                    for column in range(0, len(self.game_board)):
                        if token_3 == "".join([self.game_board[row][column] for row \
                            in range(0, len(self.game_board))]):
                            self.is_over = True
                            self.players[num].is_winner = True
                            break
        # Checks if the game is over because of a CAT game
        elif self.players[0].num_placed_tokens \
            + self.players[1].num_placed_tokens == 9:
            self.is_over = True

    def get_outcome(self):
        """
         Informs the users on the outcome on the game.
        """
        if self.players[0].is_winner:
            print(f"Congrats, {self.players[0].player_name}!!! You win!!")
        elif self.players[1].is_winner:
            print(f"Congrats, {self.players[1].player_name}!!! You win!!")
        else:
            print(f"Oh sorry, {self.players[0].player_name} and " \
                + "{self.players[1].player_name}. It's a CAT game!!")

    def display_game_board(self):
        """
         Displays the game board.
        """
        output = ["", "", ""]
        for row in range(0, len(self.game_board)):
            output[row] += " " + " | ".join(column for column in self.game_board[row]) + " "
        final = "\n-----------\n".join(line for line in output)
        print(final)
