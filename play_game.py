"""
 Author: Lori White
"""
# Main program
import game_board

def get_option(choice):
    """
     Gets the user's choice for exiting the program
    """
    option = ""
    contain = False
    while not contain:
        try:
            option = input(f"\nDo you wish to {choice}? (Y/N)  ").upper()
            contain = check_option(option)
        except AssertionError as error:
            print(f"{error} Please, try again.")
    return "Y" in option

def check_option(option):
    """
     Checks if the user entered Y or N!
    """
    assert ("Y" in option or "N" in option), "You must enter Y or N!"
    return True

G = game_board.Game()
PLAY_AGAIN = True

while PLAY_AGAIN:
    print("\n*****************************\n* " \
        + "Welcome to Tic-Tac-Toe!!! *\n*****************************\n")
    G.game_reset()
    while not G.is_over:
        for number in range(0, len(G.players)):
            G.place_token(G.players[number])
            G.check_for_end()
            if G.is_over:
                break
    G.display_game_board()
    G.get_outcome()
    PLAY_AGAIN = get_option("play again")
