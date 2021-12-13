import random
import time

# max nubmer
n = 10

# users list
user1_list = []
user2_list = []

# generating 5 random numbers for 2 users
def generating_random():

    for i in range(5):
        user1_random = random.randint(1, n)
        user2_random = random.randint(1, n)
        
        # storing random values in user lists
        user1_list.append(user1_random)
        user2_list.append(user2_random)


def logic(p_boss):
   
    if p_boss in user1_list:
        time.sleep(1)
        user1_list.remove(p_boss)
        print(f"user1 list:  {user1_list} removed number: {p_boss}")

    if p_boss in user2_list:
        time.sleep(1)
        user2_list.remove(p_boss)
        print(f"user2 list:  {user2_list} removed number: {p_boss}")


def play_game():

    greet = "Welcome to game"
    print(greet)

    # generating user lists with random numbers
    generating_random()

    # newly randomly generated lists
    print(f"Originally generated lists --> user1 list: {user1_list}   user2 list: {user2_list}")
    
    while True:

        try:
            # boss = int(input(f"Enter between 1 and {n}: "))
            boss = random.randint(1, n)
            # print(boss)
            time.sleep(1)
            if boss in user1_list or boss in user2_list:  
                print("Boss shown value: ", boss)
                logic(boss)

                if len(user1_list) < 1 and len(user2_list) < 1:
                    print('Match tie')
                    break

                if len(user1_list) < 1:
                    print('user1 wins')
                    break
                    
                if len(user2_list) < 1:
                    print("user2 wins")
                    break
            else:    
                print(f'Boss showing again : {boss}')

        except ValueError as e:
            print(e)    


# below if block prevents code from running if this file is imported in another file
if __name__ == "__main__":
    play_game()