"""
 Author: Lori White
"""
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
        self.game_board = [[], [], []]
        for row in range(0, len(self.game_board)):
            for column in range(0, 3):
                self.game_board[row].append(" ")

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
        placement = ""
        while True:
            self.display_game_board()
            placement = input(f"Player {player.player_name}, where would like to " \
                + "place your \"{player.game_token}\"?\n(Format: row,column where " \
                    + "top = 0, middle row = 1, bottom = 2, left = 0, middle column = " \
                        +"1, and right = 2)\n")
            

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
