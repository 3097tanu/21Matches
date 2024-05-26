def get_player_pick(player_name, total_matches_picked, matches_left):
    while True:
        turn_matches_picked = int(input(f"{player_name}, pick matches between 1 and 3: "))
        if matches_left >= 3:
            if 1 <= turn_matches_picked <= 3:
                return turn_matches_picked
            print(f"\nInvalid input! You can only pick 1, 2 or 3 matches.\nTry again!\n")
            print(f"~Total matches picked: {total_matches_picked}/21.")
            print(f"~Total Matches left: {matches_left}.\n")
        else:
            if 1 <= turn_matches_picked <= matches_left:
                return turn_matches_picked
            print(f"\nInvalid input! You have only {matches_left} match left to pick.\nTry again!\n" if matches_left == 1 else f"\nInvalid input! You have only {matches_left} matches left to pick.\nTry again!\n")
            print(f"~Total matches picked: {total_matches_picked}/21.")
            print(f"~Total Matches left: {matches_left}.\n")
