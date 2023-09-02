# Libraries
import random

def main():
    main_menu()


# Prints and returns main menu input
def main_menu_choice():
    print("1. Rock Paper Scissors")
    print("2. Draw Shapes")
    print("3. Currency Calculator")
    print("4. Exit")
    return input("\nPlease choose an option: ")

# Controls main menu
def main_menu():
    user_choice = main_menu_choice()
    while not (user_choice == "4"):
        route_user(user_choice)
        user_choice = main_menu_choice()

# Directs user to proper game driver
def route_user(user_choice):
    if(user_choice == "1"):
        rock_paper_scissors()
    elif(user_choice == "2"):
        draw_shapes()
    elif(user_choice == "3"):
        currency_converter()
    elif(user_choice == "4"):
        print("Thanks for playing!")
    else:
        invalid()

# Rock Paper Scissor Driver
def rock_paper_scissors():
    rpc_instructions()

    (winner, final_score) = rpc_winner({"user": 0, "computer": 0})

    if(winner == "user"):
        print("\nCongratulations, you won!")
    else:
        print("\nSorry, you lost :(")
    
    # Final Messages of game
    print("Final score was:")
    rpc_score_print(final_score)
    print("\nThanks for playing!")
    press_enter()

def rpc_winner(score):
    score = run_rpc(score)

    # Overall win condition for user
    if(
        score["user"] == 3
        or
        score["user"] == 2 and score["computer"] < 1
    ):
        return "user", score
    # Overall win condition for computer
    elif(
        score["computer"] == 3
        or
        score["computer"] == 2 and score["user"] < 1
    ):
        return "computer", score
    # Continues game if no winner determined
    else:
        return rpc_winner(score)


def convert_rpc_choice(choice):
    if(choice == "1"):
        return "rock"
    if(choice == "2"):
        return "paper"
    else:
        return "scissors"
        

def run_rpc(score):
    choices = {
        "computer": comp_rpc_choice(),
        "user": user_rpc_choice()
    }
    # Defines a tie and recalls function
    if(choices["user"] == choices["computer"]):
        print(f"You both chose: {choices['user']}")
        press_enter()
        return run_rpc(score)
    # Defines victory for user
    elif(
        choices["user"] == "scissors" and choices["computer"] == "paper"
        or
        choices["user"] == "rock" and choices["computer"] == "scissors"
        or
        choices["user"] == "papaer" and choices["computer"] == "rock"
    ):
        score["user"] = score["user"] + 1
        rpc_choice_print(choices)
        rpc_score_print(score)
        return  score
    # Other case is computer wins
    else:
        score["computer"] = score["computer"] + 1
        rpc_choice_print(choices)
        rpc_score_print(score)
        return score
        
def rpc_choice_print(choices):
    print(f"User choice: {choices['user']} Computer choice: {choices['computer']}")


def rpc_score_print(score):
    print(f"User: {score['user']} Computer: {score['computer']}")

    


def comp_rpc_choice():
    comp_choice = random.randint(1, 3)
    return convert_rpc_choice(comp_choice)

def rpc_instructions():
    print("This game is played by choosing one of the following options")
    print("After you choose one option, the computer will randomly choose an option")
    print("best 2 of 3 games wins")

def user_rpc_choice():
    message = "1. Rock\n2. Paper\n3. Scissors"
    print(message)
    user_choice = input("\nPlease choose an option: ")
    if not (user_choice == "1" or user_choice == "2" or user_choice == "3"):
        invalid()
        return user_rpc_choice()
    return convert_rpc_choice(user_choice)


def draw_shapes():
    shape = shape_choice()
    symbol = symbol_choice()
    if(shape == "triangle"):
        draw_triangle(symbol)
    elif(shape == "rectangle"):
        draw_rectangle(symbol)

    print("Thanks for drawing with us today!")
    press_enter()

def draw_triangle(symbol):
    length = dimension_choice("Length")

    for i in range(length, 0, -1):
        for j in i:
            print(symbol, end="")
        print()
    

def draw_rectangle(symbol):
    length = dimension_choice("Length")
    width = dimension_choice("Width")

    for i in width:
        for j in length:
            print(symbol, end="")
        print

def shape_choice():
    user_choice = input("What would you like to draw? (triangle, rectangle)\n").lower()
    if not (user_choice == "rectangle" or user_choice == "triangle"):
        invalid()
        return shape_choice()
    return user_choice
    
def symbol_choice():
    choice = input("Enter the symbol you would like to user to draw the shapes with: ")
    if(choice.count == 1):
        return choice
    print("Please choose a single character!")
    press_enter()
    return symbol_choice()

def dimension_choice(dim):
    choice = input(f"Please enter a size for the {dim}")
    try:
        num = int(choice)
        if(num < 2):
            print("Please enter a number greater than 1")
            press_enter()
            return dimension_choice(dim)
        return num
    except ValueError:
        print("Please enter an integer value!")
        press_enter()
        return dimension_choice(dim)
    
def currency_converter():
    print("currency")

# Utility functions

# Generic invalid input with a request to press enter
def invalid():
    print("\nYou have chosen an invalid option.")
    press_enter()

# Prompts user to press enter to continue
def press_enter():
    print("\nPress enter to continue,")
    input()
    print("\n\n")

# Starts program
main()