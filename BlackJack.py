import random

# variable globale
user_continue = True
new = ""
deck = {"A": [1, 11],
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10}


###################################
def draw_card(result):
    """Function that return a card faces and value. take the result as a """
    face, value = random.choice(list(deck.items()))
    # Ace exceptions
    # face ="A" #testing exceptions
    # value=[1,11]#testing exceptions
    if face == "A" and result <= 10:
        return face, value[1]
    elif face == "A" and result > 10:
        return face, value[0]

    return face, value


# face, value = draw_card(11)#test
# print(face, value)
# print(deck.items())

def start():
    choice = input(f"Do you want to play a{new} game of Blackjack? Type 'yes' or 'no':").lower()
    if choice == "no":
        clear()
        return False
    elif choice == "yes":
        clear()
        return True
    else:
        print("Please type 'yes' or 'no' ")
        clear()
        start()


def game():
    # draw card for the computer and the player
    computer_result = 0
    player_result = 0
    computer_fcards = []
    player_fcards = []
    computer_vcards = []
    player_vcards = []

    for i in range(3):
        player_fcards, player_vcards = draw_card(player_result)
        computer_fcards, computer_vcards = draw_card(computer_result)

    print("computer:")
    print(computer_fcards, computer_vcards)
    print("player:")
    print(player_fcards, player_vcards)


game()
