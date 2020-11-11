import time

import random

rucksack = []

monsters = ['wicked fairie', 'pirate', 'dragon', 'gorgon', 'troll', 'Karen']
monster = random.choice(monsters)

items = ['fork', 'hammer', 'cheese grater', 'power cord', 'vacuum', 'toaster']
item = random.choice(items)


limbs = ['arm', 'tail', 'leg', 'head']
limb = random.choice(limbs)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Sorry, I do not understand {option}.')


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wild flowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


def field(rucksack):
    doorcave = valid_input("Enter 1 to knock on the door of the house. "
                           "Enter 2 to peer into the cave.\n", ["1", "2"])
    if doorcave == "1":
        house(rucksack)  # go to the house
    elif doorcave == "2":
        cave(rucksack)  # go to the cave
    else:
        field(rucksack)


def house(rucksack):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens "
                "and out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    fight(rucksack)


def cave(rucksack):
    print_pause("You peer cautiously into the cave.")
    if item in rucksack:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {item} of Ogoroth!")
        print_pause(f"You discard your silly old dagger and take the {item} "
                    "with you.")
        rucksack.append(item)
        print_pause("You walk back out to the field.")
    field(rucksack)


def fight(rucksack):
    fightrun = valid_input("Would you like to (1) fight or (2) run away?\n",
                           ["1", "2"])
    if fightrun == '1':
        if item in rucksack:
            print_pause(f"As the {monster} moves to attack, you "
                        "unsheath your new {item}.")
            print_pause(f"The {item} of Ogoroth shines brightly "
                        "in your hand as you brace yourself for "
                        "the attack.")
            damages(rucksack)
        else:
            print_pause("You feel a bit under-prepared for this, what "
                        "with only having a tiny dagger.")
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {monster}.")
            print_pause("You have been defeated!")
            playagain()
    elif fightrun == '2':
        coward(rucksack)
    else:
        fight(rucksack)


def damages(rucksack):
    def herodamage():
        herodamage = random.randrange(1, 100)
        return herodamage

    def monsterdamage():
        monsterdamage = random.randrange(1, 100)
        return monsterdamage
    herodamage = herodamage()
    monsterdamage = monsterdamage()
    print_pause(f"You deal the {monster} {herodamage} damage.")
    print_pause(f"The {monster} deals you {monsterdamage} damage.")
    yourdamage = 0
    enemydamage = 0
    yourdamage += herodamage
    enemydamage += monsterdamage
    if yourdamage > enemydamage:
        print_pause(f"You have dealt the {monster} a significant blow.")
        print_pause(f"The {monster}'s {limb} falls off!")
    else:
        print_pause(f"The {monster} has badly wounded you.")
    fightagain(rucksack, yourdamage, enemydamage)


def fightagain(rucksack, yourdamage, enemydamage):
    fightagain = valid_input("Would you like to (1) strike again or "
                             "(2) run away?\n", ["1", "2"])
    if fightagain == '1':
        lastbattle(rucksack, yourdamage, enemydamage)
    elif fightagain == '2':
        coward(rucksack)
    else:
        fightagain(rucksack, yourdamage, enemydamage)


def lastbattle(rucksack, yourdamage, enemydamage):
    def herodamage():
        herodamage = random.randrange(1, 100)
        return herodamage

    def monsterdamage():
        monsterdamage = random.randrange(1, 100)
        return monsterdamage

    herodamage = herodamage()
    monsterdamage = monsterdamage()
    print_pause(f"You deal the {monster} {herodamage} damage.")
    print_pause(f"The {monster} deals you {monsterdamage} damage.")
    yourdamage += herodamage
    enemydamage += monsterdamage
    print_pause(f"You have inflicted {yourdamage} total damage "
                f"on the {monster}.")
    print_pause(f"The {monster} has inflicted {enemydamage} "
                "total damage on you.")
    if yourdamage > enemydamage:
        print_pause(f"Your strike finishes the {monster}!")
        print_pause(f"You have rid the town of the {monster}.\n"
                    "You are victorious!")
    else:
        print_pause(f"The {monster} has badly wounded you and you can "
                    "no longer fight.")
        print_pause("You have been defeated!")
    playagain()


def coward(rucksack):
    print_pause("You run back to the field. Luckily, you don't seem to "
                "have been followed.")
    field(rucksack)


def playagain():
    print_pause("GAME OVER\n")
    playagain = valid_input("Would you like to play again? (y/n)\n",
                            ["y", "n"]).lower()
    if 'y' in playagain:
        print_pause("Excellent! Restarting the game...\n")
        play_game(rucksack)
    elif 'n' in playagain:
        print_pause("Thanks for playing! See you next time.")
    else:
        playagain()


def play_game(rucksack):
    rucksack = []
    intro()
    field(rucksack)


play_game(rucksack)
