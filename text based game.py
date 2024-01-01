import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in front of a mysterious cave.")
    print("Do you want to enter? (yes/no)")

def make_choice():
    choice = input("> ").lower()
    return choice

def explore_cave():
    print("\nYou enter the cave and discover two paths.")
    print("One path leads deeper into the cave, and the other goes up.")
    print("Which path do you choose? (deep/up)")

def deep_path():
    print("\nAs you venture deeper, you encounter a treasure chest.")
    print("Do you want to open it? (yes/no)")

def open_chest():
    print("\nYou open the chest and find a shiny key inside.")
    print("There are more paths ahead. Where do you want to go? (left/right)")

def left_path():
    print("\nYou use the shiny key to unlock a door.")
    print("Behind the door, you find a room with a magical portal.")
    print("Do you want to enter the portal? (yes/no)")

def enter_portal():
    print("\nCongratulations! You've successfully navigated the cave and entered a magical realm.")
    print("You win!")

def game_over():
    print("\nGame over! You didn't make the right choices.")
    print("Feel free to play again!")

def play_game():
    introduction()
    choice = make_choice()

    if choice == "yes":
        explore_cave()
        choice = make_choice()

        if choice == "deep":
            deep_path()
            choice = make_choice()

            if choice == "yes":
                open_chest()
                choice = make_choice()

                if choice == "left":
                    left_path()
                    choice = make_choice()

                    if choice == "yes":
                        enter_portal()
                    else:
                        game_over()
                else:
                    game_over()
            else:
                game_over()
        elif choice == "up":
            print("\nYou climb up but slip and fall. Ouch! You lose.")
        else:
            game_over()
    else:
        print("\nYou decide not to enter the cave. The adventure ends here. Play again anytime!")

if __name__ == "__main__":
    play_game()
