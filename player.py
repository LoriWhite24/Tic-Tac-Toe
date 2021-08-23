"""
 Author: Lori White
"""
class Player:
    """
     This represents a player in the game.
    """

    def __init__(self):
        """
         Intializes the player
        """
        self.is_first = False
        self.game_token = "O"
        self.is_winner = False
        self.player_name = "name"
        self.num_placed_tokens = 0

    def player_reset(self):
        """
         Resets the player
        """
        self.is_first = False
        self.game_token = "O"
        self.is_winner = False
        self.player_name = "name"
        self.num_placed_tokens = 0

    def place_game_token(self):
        """
         Updates the number of game tokens that player has placed
        """
        self.num_placed_tokens += 1
        if self.is_first and self.num_placed_tokens > 5:
            raise Exception(f"Player 1, {self.player_name}, " \
                + "has exceded the number of game token placement.")
        elif self.num_placed_tokens > 4:
            raise Exception(f"Player 2, {self.player_name}, " \
                + "has exceded the number of game token placement.")

    def get_name(self, is_player_one):
        """
         Prompts player for name based on if they are player one or player two
        """
        if is_player_one:
            self.player_name = input("Player 1, what is your name? ")
            self.is_first = True
            self.game_token = "X"
        else:
            self.player_name = input("Player 2, what is your name? ")
