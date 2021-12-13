"""
Number guessing Game
"""
import time
import random

attempts_list = {}  # attempts_list structure --> {key : value} --> { id : [name, attempts]}
best_score = {}   # best_score structure --> {key : value} --> { id : [name, attempts]}


def minimum_attempts():
    """
        Display the players who are having minimum attempts
    """
    time.sleep(1)  # pause 1 sec
    print(f"{'*' * 40}\nMinimum Attempts")
    for best_player_id in list(best_score):
        print(f"Player ID: {best_player_id} -- {best_score[best_player_id][0]} with "
              f"{best_score[best_player_id][1]} attempt(s)")
    print(f"{'*' * 40}\n")


def score(player_name, player_id, player_attempts):
    """
    Fetching the high score from the dictionary of the 'attempts_list'
    """

    print(f"{'-'*40}\nPlayer ID: {player_id} took {player_attempts} attempt(s)=\n{'-'*40}\n")

    if len(attempts_list) < 1:
        attempts_list[player_id] = [player_name, player_attempts]
        best_score[player_id] = [player_name, player_attempts]
    else:
        attempts_list[player_id] = [player_name, player_attempts]
        for best_player_id in list(best_score):
            best_player_name = best_score[best_player_id][0]
            best_player_attempts = best_score[best_player_id][1]

            if best_player_attempts < player_attempts:
                pass
            elif best_player_attempts > player_attempts:
                print(f"{best_player_name} is having {best_player_attempts} attempt(s)--removing")
                time.sleep(1)  # pause 1 sec
                del best_score[best_player_id]
                best_score[player_id] = [player_name, player_attempts]
            else:
                best_score[player_id] = [player_name, player_attempts]

    minimum_attempts()


def start_game():
    """
    Starting/entry point
    """
    attempts = 0
    guess = random.randint(1, 10)
    u_name = input("Enter your name: ")
    while True:
        try:
            u_id = int(input("Create your player ID (1-4): "))
            break
        except ValueError as e:
            print(e)
            print("try again ...please enter 4 digit number")

    if len(attempts_list) < 1:
        print(f"Ohh. {u_name}, you are the first one to play this game")

    while u_id in attempts_list:
        u_id = int(input("Player id already exits... enter different ID: "))

    u_pick = int(input("Pick a number between 1 - 10: "))
    
    while True:
        if u_pick == guess:
            attempts += 1
            print("you got it !")
            score(u_name, u_id, attempts)
            break

        elif u_pick < guess:
            print("Guessed number is high")
            attempts += 1

        elif u_pick > guess:
            print("Guessed number is low")
            attempts += 1

        u_pick = int(input("Try again: "))

    again = False

    while not again:
        play_again = input("Want to play again (y/n): ")
        if play_again.lower() == 'y':
            start_game()
        else:
            again = True
    # while True:
        # if u_pick == guess:
        #     attempts += 1
        #     print("you got it !")
        #     score(u_name, u_id, attempts)

            # play_again = input("Want to play again (y/n): ")

            # while True:
            #     if not (play_again.lower() == "y" and play_again.lower() == "n") :
            #         print("Please press either 'y' for yes or 'n' for no ")
            #     elif play_again.lower() == "y":
            #         print("Initiating game again ...")
            #         time.sleep(2)
            #         start_game()
            #     elif play_again.lower() == "n":
            #         break       

if __name__ == "__main__":
    start_game()

