import human_mode
import computer_mode
# multiplayer or play with computer?
def game_mode():
    game_mode = input("Play with a friend (press 'F') or Play with Computer (press 'C'): ").upper()
    return game_mode

game_mode = game_mode()

if game_mode == "F":
    print("\nYou'll play with a friend.\n")
    human_mode.multiplayer_game() 
elif game_mode == "C":
    print("\nYou'll play with the computer.\n")
    computer_mode.game_with_computer()
else:
    print("Incorrect choice! Try again.")
    # game_mode()

