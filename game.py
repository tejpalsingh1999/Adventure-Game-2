import time
import random

sword = 0
flower = 0
required = ("\nUse only A, B, or C\n")
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
game_characters = ['Grumpy Mutant', 'Monstrous Nether Gorilla',
                   'Vampsnake', 'Hidden Assassin Elephant']
char = random.choice(game_characters)


def print_pause(string):
    print(string)
    time.sleep(2)


def intro(char):
    print_pause("After a drunken night out "
                "with friends, you awaken the ")
    print_pause("next morning in a thick, dank forest."
                " Head spinning and ")
    print_pause("fighting the urge to vomit, you stand"
                " and marvel at your new, ")
    print_pause("unfamiliar setting. The peace quickly"
                " fades when you hear a ")
    print_pause("grotesque sound emitting behind"
                " you. A " + char + " is ")
    print_pause("running towards you. You will:")
    print_pause("\nA. Grab a nearby rock and throw it at the orc\n"
                "B. Lie down and wait to be mauled\n"
                "C. Run\n")
    choice = input(">>> ")
    if choice in answer_A:
        option_rock(char)
    elif choice in answer_B:
        print_pause("\nWelp, that was quick. "
                    "\n\nYou died!")
        play_again()
    elif choice in answer_C:
        option_run()
    else:
        print(required)
    intro(char)


def option_rock(char):
    print_pause("\nThe " + char + " is stunned, "
                "but regains control. He begins")
    print_pause("running towards you again. Will you:")
    print_pause("\nA. Run\n"
                "B. Throw another rock\n"
                "C. Run towards a nearby cave\n")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print_pause("\nYou decided to throw another rock,"
                    " as if the first ")
        print_pause("rock thrown did much damage. "
                    "The rock flew well over the ")
        print_pause(char + " head. You missed. "
                    "\n\nYou died!")
        play_again()
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock(char)


def option_cave():
    print_pause("\nYou were hesitant, since the "
                "cave was dark and ")
    print_pause("ominous. Before you fully enter, "
                "you notice a shiny sword on ")
    print_pause("the ground. Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1
    else:
        sword = 0
    print_pause("\nWhat do you do next?\n")
    print_pause("\nA. Hide in silence\n"
                "B. Fight\n"
                "C. Run\n")
    choice = input(">>> ")
    if choice in answer_A:
        print_pause("\nReally? You're going to hide in the dark? I think ")
        print_pause(+ char + " can see very well in the dark, "
                    "right? Not sure, but ")
        print_pause("I'm going with YES, so...\n\nYou died!")
        play_again()
    elif choice in answer_B:
        if sword > 0:
            print_pause("\nYou laid in wait. "
                        "The shimmering sword attracted ")
            print_pause("the " + char + ", which thought you"
                        " were no match. As he walked ")
            print_pause("closer and closer, your heart "
                        "beat rapidly. As the " + char)
            print_pause("reached out to grab the sword, "
                        "you pierced the blade into ")
            print_pause("its chest. \n\nYou survived!")
            play_again()
        else:
            print_pause("\nYou should have picked up that sword. You're "
                        "defenseless. \n\nYou died!")
            play_again()
    elif choice in answer_C:
        print_pause("As the " + char + " enters the dark cave, you sliently ")
        print_pause("sneak out. You're several feet away, but the " + char)
        print_pause("around and sees you running.")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print_pause("\nYou run as quickly as possible, but the " + char)
    print_pause("speed is too great. You will:")
    print_pause("\nA. Hide behind boulder\n"
                "B. Trapped, so you fight\n"
                "C. Run towards an abandoned town\n")
    choice = input(">>> ")
    if choice in answer_A:
        print_pause("You're easily spotted.")
        print_pause("\n\nYou died!")
        play_again()
    elif choice in answer_B:
        print_pause("\nYou're no match for an " + char)
        print_pause("\n\nYou died!")
        play_again()
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print_pause("\nWhile frantically running, you notice a rusted ")
    print_pause("sword lying in the mud. You quickly"
                " reach down and grab it, ")
    print_pause("but miss. You try to calm your "
                "heavy breathing as you hide ")
    print_pause("behind a delapitated building,"
                " waiting for the " + char + " to come ")
    print_pause("charging around the corner. "
                "You notice a purple flower ")
    print_pause("near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1
    else:
        flower = 0
        print_pause("You hear its heavy footsteps"
                    " and ready yourself for ")
        print_pause("the impending " + char)

    if flower > 0:
        print_pause("\nYou quickly hold out the purple flower, somehow ")
        print_pause("hoping it will stop the " + char + ". It does! The "
                    + char + " was looking ")
        print_pause("for love. ")
        print_pause("\n\nThis got weird, but you survived!")
        play_again()
    else:
        print_pause("\nMaybe you should have picked up the flower. ")
        print_pause("\n\nYou died!")
        play_again()


def play_again():
    game_characters = ['Grumpy Mutant', 'Monstrous Nether Gorilla',
                       'Vampsnake', 'Hidden Assassin Elephant']
    char = random.choice(game_characters)
    print_pause("\n\nWould you like to play again ?")
    print_pause("Y-Yes\nN-No")
    ans = input()
    if ans in yes:
        print_pause("\n\nRESTARTING \n\n")
        intro(char)
    elif ans in no:
        print_pause("Thanks for playing")
        exit()
    else:
        play_again()


if __name__ == '__main__':
    intro(char)
