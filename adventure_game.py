import random
import time


def get_user_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        else:
            return get_user_input(prompt, options)


def runaway():
    print_pause(
        "You run back into the field. Luckily, "
        "you don't seem to have been followed.",
        2)
    field()


def house(weapon):
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps a %s."
        % game_character,
        3)
    print_pause("The %s attacks you!" % game_character)
    response = get_user_input("Would you like to (1) fight or (2) run away?!",
                              ["1", "2"])
    if response == "1":
        fight(weapon)
    elif response == "2":
        runaway()


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause(
        "You discard your silly old dagger and take the sword with you.", 3)
    print_pause("You walk back out to the field.")
    field("Sword")


def fight(weapon):
    if weapon == 'dagger':
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the %s." % game_character)
        print_pause("You have been defeated!")
    else:
        print_pause(
            "As the %s moves to attack, you unsheath your new sword."
            % game_character,
            3)
        print_pause(
            "The Sword of Ogoroth shines brightly in your hand as you brace "
            "yourself for the attack.",
            3)
        print_pause(
            "But the %s takes one look at your shiny new toy and runs away!"
            % game_character,
            3)
        print_pause(
            "You have rid the town of the %s. You are victorious!"
            % game_character)
    check_end_game()


def field(weapon="dagger"):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    response = get_user_input("Please enter 1 or 2.", ["1", "2"])

    if "1" in response:
        house(weapon)

    elif "2" in response:
        cave()


def print_pause(message, pause=2):
    print(message)
    time.sleep(pause)


def intro():
    print_pause(
        "You find yourself standing in an open field, filled with grass and"
        " yellow wildflowers.",
        3)
    print_pause(
        "Rumor has it that a %s is somewhere around here, "
        "and has been terrifying "
        ""
        "the nearby village." % game_character, 3)
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective)"
        " dagger.\n",
        2)


def get_game_character():
    game_characters = ["dragon", "pirate", "wicked fairie", "troll"]
    return random.choice(game_characters)


def check_end_game():
    print_pause("GAME OVER")
    response = get_user_input("Would you like to play again?"
                              " (y/n)", ["y", "n"])
    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        field()
    else:
        print_pause("Thanks for playing! See you next time.")


if __name__ == '__main__':
    game_character = get_game_character()
    intro()
    field()
