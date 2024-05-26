import random
import player_pick

# play with computer
def game_with_computer():
    player_name = input("Enter Player's name: ")
    computer = "21GPT"
    players = [player_name, computer]

    turn = random.choice(range(len(players)))
    print(f"\n{players[turn]} won the toss and will play first!")

    total_matches_picked = 0
    matches_left = 21

    while total_matches_picked < 21:
        if players[turn] != computer:
            turn_matches_picked = player_pick.get_player_pick(players[turn], total_matches_picked, matches_left)
        else:
            turn_matches_picked = get_computer_pick(total_matches_picked, matches_left)
            print(f"{computer} picked {turn_matches_picked} match." if turn_matches_picked == 1 else f"{computer} picked {turn_matches_picked} matches.")

        total_matches_picked += turn_matches_picked
        matches_left -= turn_matches_picked
        print(f"\n~Total matches picked: {total_matches_picked}/21.")
        print(f"~Total Matches left: {matches_left}.\n")

        turn = (turn + 1) % len(players)

    print(f"{players[turn]} is the winner!\n")
    if len(players) == 2:
        print(f"{players[(turn + 1) % 2]} is the loser!\n")

def get_computer_pick(total_matches_picked, matches_left):
    if total_matches_picked % 4 != 0:
        return 4 - (total_matches_picked % 4)
    elif matches_left == 1:
        return 1
    else:
        return random.choice([1, 2, 3])
