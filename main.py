import random
import time
hands = {
    "rock": [
        "    _______",
        "---'   ____)",
        "      (_____)",
        "      (_____)",
        "      (____)",
        "---.__(___)"
    ],
    "paper": [
        "    _______",
        "---'   ____)____",
        "          ______)",
        "          _______)",
        "         _______)",
        "---.__________)"
    ],
    "scissors": [
        "    _______",
        "---'   ____)____",
        "          ______)",
        "       __________)",
        "      (____)",
        "---.__(___)"
    ]
}

options = ["rock" , "paper" , "scissors"]
def options_display():
    print("ROCK \nPAPER \nSCISSOR")
def init_display():
    for times in range(1):
        print("--- ROCK PAPER SCISSOR GAME ---")
        print("--- PLAY AGAINST THE MACHINE ! ---")
beats = { "rock" : "scissor",
          "paper" : "rock",
          "scissor" : "paper"
}
init_display()
while True:
    options_display()
    player_choice = str(input("What do you choose: "))
    computer_choice = random.choice(options)
    print("Rock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissor...")
    time.sleep(0.5)
    print("!!!")
    print(f"PLAYER ({player_choice}) vs COMPUTER ({computer_choice})")
    #Pas trouvé de méthode pour afficher les ascii
    for player_line in hands[player_choice]:
        print(f"{player_line}")
    for computer_line in hands[computer_choice]:
        print(f"{computer_line}")
    #On peut faire également comme ça pour qu'ils soient paralleles avec "zip"
    #for player_line , computer_line in zip(hands[player_choice] , hands[computer_choice]):
        #print(f"{player_line}           {computer_line}")

    if computer_choice == player_choice:
        print("It's a tie!")
    elif beats[player_choice] == computer_choice:
        print("You won!")
    else:
        print("The machine won!")

