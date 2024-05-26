import random

# multiplayer or play with computer?
def game_mode():
    game_mode = input("Play with a friend (press 'F') or Play with Computer (press 'C'): ").upper()
    return game_mode

# play with a friend
def multiplayer_game():
    player1_name = input("Enter 1st player's name: ")
    player2_name = input("Enter 2nd player's name: ")
    players = [player1_name, player2_name]

    turn = random.choice(range(len(players)))
    print(f"\n{players[turn]} will play first!")
        
    total_matches_picked = 0
    matches_left = 21
    print(f"\n~Total matches picked: {total_matches_picked}/21.")
    print(f"~Total Matches left: {matches_left}.\n")

    while total_matches_picked < 21:
        while True: #check for correct pick
            turn_matches_picked = int(input(f"{players[turn]}, pick matches between 1 and 3: "))
            if matches_left >=3:
                if turn_matches_picked < 1 or turn_matches_picked > 3:
                    print(f"\nInvalid input! You can only pick 1, 2 or 3 matches.\nTry again!\n")
                    print(f"~Total matches picked: {total_matches_picked}/21.")
                    print(f"~Total Matches left: {matches_left}.\n")
                else:
                    break
            else:
                if turn_matches_picked < 1 or turn_matches_picked > matches_left:
                    print(f"\nInvalid input! You have only {matches_left} match left to pick.\nTry again!\n" if matches_left == 1 else f"\nInvalid input! You have only {matches_left} matches left to pick.\nTry again!\n")
                    print(f"~Total matches picked: {total_matches_picked}/21.")
                    print(f"~Total Matches left: {matches_left}.\n")
                else:
                    break
            
        total_matches_picked = total_matches_picked + turn_matches_picked
        matches_left = matches_left - turn_matches_picked
        
        print(f"\n~Total matches picked: {total_matches_picked}/21.")
        print(f"~Total Matches left: {matches_left}.\n")

        #turn = player2_name if turn == player1_name else player1_name
        turn = (turn+1)%len(players)

    print(f"{players[turn]} is the winner!\n")

# play with computer
def game_with_computer():
    player_name = input("Enter Player's name: ")
    computer = "Computer"
    players = [player_name, computer]

    turn = 0
    # turn = random.choice(range(len(players)))
    print(f"\n{players[turn]} will play first!")

    total_matches_picked = 0
    matches_left = 21
    print(f"\n~Total matches picked: {total_matches_picked}/21.")
    print(f"~Total Matches left: {matches_left}.\n")

    if players[turn] != computer:
        # player plays first
        while total_matches_picked < 21:
            if players[turn] != computer:
                while True: #check for correct pick
                    turn_matches_picked = int(input(f"{players[turn]}, pick matches between 1 and 3: "))
                    if matches_left >=3:
                        if turn_matches_picked < 1 or turn_matches_picked > 3:
                            print(f"\nInvalid input! You can only pick 1, 2 or 3 matches.\nTry again!\n")
                            print(f"~Total matches picked: {total_matches_picked}/21.")
                            print(f"~Total Matches left: {matches_left}.\n")
                        else:
                            break
                    else:
                        if turn_matches_picked < 1 or turn_matches_picked > matches_left:
                            print(f"\nInvalid input! You have only {matches_left} match left to pick.\nTry again!\n" if matches_left == 1 else f"\nInvalid input! You have only {matches_left} matches left to pick.\nTry again!\n")
                            print(f"~Total matches picked: {total_matches_picked}/21.")
                            print(f"~Total Matches left: {matches_left}.\n")
                        else:
                            break
                
                total_matches_picked = total_matches_picked + turn_matches_picked
                matches_left = matches_left - turn_matches_picked
                
                print(f"\n~Total matches picked: {total_matches_picked}/21.")
                print(f"~Total Matches left: {matches_left}.\n")

            else: 
                turn_matches_picked = 4 - (total_matches_picked % 4)
                               
                print(f"Computer picked {turn_matches_picked} match." if turn_matches_picked == 1 else f"Computer picked {turn_matches_picked} matches.")
                
                total_matches_picked = total_matches_picked + turn_matches_picked
                matches_left = matches_left - turn_matches_picked
                
                print(f"\n~Total matches picked: {total_matches_picked}/21.")
                print(f"~Total Matches left: {matches_left}.\n")

            # switch turns
            turn = (turn+1)%len(players)  
            
        print(f"{players[turn]} is the winner!\n")

    else:
        # computer plays first
        print("\nNot available! Let's try again.\n")
        game_with_computer()
        # while total_matches_picked < 21:
        #     while True: #check for correct pick
        #         turn_matches_picked = int(input(f"{players[turn]}, pick matches between 1 and 3: "))
        #         if matches_left >=3:
        #             if turn_matches_picked < 1 or turn_matches_picked > 3:
        #                 print(f"Invalid input! You can only pick 1, 2 or 3 matches.\nTry again!\n")
        #                 print(f"~Total matches picked: {total_matches_picked}/21.")
        #                 print(f"~Total Matches left: {matches_left}.\n")
        #             else:
        #                 break
        #         else:
        #             if turn_matches_picked < 1 or turn_matches_picked > matches_left:
        #                 print(f"Invalid input! You have only {matches_left} matches left to pick.\nTry again!\n")
        #                 print(f"~Total matches picked: {total_matches_picked}/21.")
        #                 print(f"~Total Matches left: {matches_left}.\n")
        #             else:
        #                 break
                
        #     total_matches_picked = total_matches_picked + turn_matches_picked
        #     matches_left = matches_left - turn_matches_picked
            
        #     print(f"\n~Total matches picked: {total_matches_picked}/21.")
        #     print(f"~Total Matches left: {matches_left}.\n")

        #     # switch turns
        #     turn = (turn+1)%len(players)

        # print(f"{players[turn]} is the winner!")

game_mode = game_mode()

if game_mode == "F":
    print("\nYou'll play with a friend.\n")
    multiplayer_game() 
elif game_mode == "C":
    print("\nYou'll play with the computer.\n")
    game_with_computer()
else:
    print("Incorrect choice! Try again.")
    # game_mode()

