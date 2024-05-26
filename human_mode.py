import random

# play with a friend
def multiplayer_game():
    player1_name = input("Enter 1st player's name: ")
    player2_name = input("Enter 2nd player's name: ")
    players = [player1_name, player2_name]

    turn = random.choice(range(len(players)))
    print(f"\n{players[turn]} won the toss and will play first!")
        
    total_matches_picked = 0
    matches_left = 21
    print(f"\n~Total matches picked: {total_matches_picked}/21.")
    print(f"~Total Matches left: {matches_left}.\n")

    while total_matches_picked < 21:
        turn_matches_picked = get_valid_pick(players[turn], matches_left)
        total_matches_picked += turn_matches_picked
        matches_left -= turn_matches_picked
        
        print(f"\n~Total matches picked: {total_matches_picked}/21.")
        print(f"~Total Matches left: {matches_left}.\n")

        turn = (turn + 1) % len(players)

    print(f"{players[turn]} is the winner!\n")

def get_valid_pick(player_name, matches_left):
    while True:
        pick = int(input(f"{player_name}, pick matches between 1 and 3: "))
        if matches_left >= 3:
            if 1 <= pick <= 3:
                return pick
            print(f"\nInvalid input! You can only pick 1, 2 or 3 matches.\nTry again!\n")
        else:
            if 1 <= pick <= matches_left:
                return pick
            print(f"\nInvalid input! You have only {matches_left} match left to pick.\nTry again!\n" if matches_left == 1 else f"\nInvalid input! You have only {matches_left} matches left to pick.\nTry again!\n")
