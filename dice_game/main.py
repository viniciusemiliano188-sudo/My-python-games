import random
#Jeux de dés simple qu'affiche un ascii du number roll qu'est sorti
dice_art = {
    1: (
        " ------- ",
        "|       |",
        "|   o   |",
        "|       |",
        " ------- "
    ),
    2: (
        " ------- ",
        "| o     |",
        "|       |",
        "|     o |",
        " ------- "
    ),
    3: (
        " ------- ",
        "| o     |",
        "|   o   |",
        "|     o |",
        " ------- "
    ),
    4: (
        " ------- ",
        "| o   o |",
        "|       |",
        "| o   o |",
        " ------- "
    ),
    5: (
        " ------- ",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        " ------- "
    ),
    6: (
        " ------- ",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        " ------- "
    )
}
def dice_roll():
    d_rolls = int(input("How many dices you want to roll:"))
    #loop for qui lance la variable roll(qui choisi un nombre au hasard entre 1-6) par rapport à la quantité de dés lancés
    for roll in range(d_rolls):
        roll = random.randint(1, 6)
        print(roll)
        #Ensuite on va associer la variable "line" avec la dice_art par rapport à roll et l'afficher
        for line in dice_art[roll]:
            print(line)
while True:
    dice_roll()
