import random

# play with computer
def game_with_computer():
    player_name = input("Enter Player's name: ")
    computer = "21GPT"
    players = [player_name, computer]

    turn = 1 #remove
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
                
                # total_matches_picked = total_matches_picked + turn_matches_picked
                # matches_left = matches_left - turn_matches_picked
                
                # print(f"\n~Total matches picked: {total_matches_picked}/21.")
                # print(f"~Total Matches left: {matches_left}.\n")

            else: 
                turn_matches_picked = 4 - (total_matches_picked % 4)
                               
                print(f"Computer picked {turn_matches_picked} match." if turn_matches_picked == 1 else f"Computer picked {turn_matches_picked} matches.")
                
                # total_matches_picked = total_matches_picked + turn_matches_picked
                # matches_left = matches_left - turn_matches_picked
                
                # print(f"\n~Total matches picked: {total_matches_picked}/21.")
                # print(f"~Total Matches left: {matches_left}.\n")

            total_matches_picked = total_matches_picked + turn_matches_picked
            matches_left = matches_left - turn_matches_picked
                
            print(f"\n~Total matches picked: {total_matches_picked}/21.")
            print(f"~Total Matches left: {matches_left}.\n")
            
            # switch turns
            turn = (turn+1)%len(players)  
            
        print(f"{players[turn]} is the winner!\n")

    else:
        # computer plays first
        while total_matches_picked < 21:
            if players[turn] != player_name:
                if total_matches_picked % 4 != 0:
                    turn_matches_picked = 4 - (total_matches_picked % 4)
                else:
                    if matches_left == 1:
                        turn_matches_picked = 1
                    else:
                        turn_matches_picked = random.choice([1,2,3])            

                print(f"Computer picked {turn_matches_picked} match." if turn_matches_picked == 1 else f"Computer picked {turn_matches_picked} matches.")

            else:
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
                    
                # total_matches_picked = total_matches_picked + turn_matches_picked
                # matches_left = matches_left - turn_matches_picked
                
                # print(f"\n~Total matches picked: {total_matches_picked}/21.")
                # print(f"~Total Matches left: {matches_left}.\n")
            
                               
            total_matches_picked = total_matches_picked + turn_matches_picked
            matches_left = matches_left - turn_matches_picked
                
            print(f"\n~Total matches picked: {total_matches_picked}/21.")
            print(f"~Total Matches left: {matches_left}.\n")

            # switch turns
            turn = (turn+1)%len(players)

        print(f"{players[turn]} is the winner!")
