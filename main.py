# Bonuses:
# 1. Rock paper scissors is played with best 2 out of 3
# 2. You can draw circles in addition to the other listed shapes
# 3. Code maintenance for adding shapes is easily done, by extending the list of dictionaries
# 4. For currency conversion, only denominations that have values are listed 
        # (if 1.50 is entered, only dollars and quarters will be listed)

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
    updated_score = run_rpc(score)

    # Overall win condition for user
    if(
        updated_score["user"] == 3
        or
        updated_score["user"] == 2 and updated_score["computer"] < 1
    ):
        return "user", updated_score
    # Overall win condition for computer
    elif(
        updated_score["computer"] == 3
        or
        updated_score["computer"] == 2 and updated_score["user"] < 1
    ):
        return "computer", updated_score
    # Continues game if no winner determined
    else:
        return rpc_winner(updated_score)


def convert_rpc_choice(input):
    # convert to a string in cases of ints, defensive programming
    choice = str(input)
    if(choice == "1"):
        return "rock"
    if(choice == "2"):
        return "paper"
    elif(choice == "3"):
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
    final_choice = convert_rpc_choice(comp_choice)
    return final_choice

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
    shapes = [
        {
         "name": "diamond",
         "draw": draw_circle
        },
        {
         "name": "triangle",
         "draw": draw_triangle
        },
        {
         "name": "rectangle",
         "draw": draw_rectangle
        }
    ]

    # Uses list comprehension to iterate over all shapes and only return names
    shape = shape_choice([s['name'] for s in shapes])
    symbol = symbol_choice()
   
    # Searches through the list of dictionaries and finds the one that 
    # matches what the user chose
    found_shape = next((s for s in shapes if s["name"] == shape))

    # calls the associated draw function
    found_shape["draw"](symbol)

    print("Thanks for drawing with us today!")
    press_enter()

def draw_triangle(symbol):
    length = dimension_choice("Length")

    for i in range(length, 0, -1):
        for j in range(i):
            print(symbol, end="")
        print()
    

def draw_rectangle(symbol):
    length = dimension_choice("Length")
    width = dimension_choice("Width")

    for i in range(width):
        for j in range(length):
            print(symbol, end="")
        print()

def draw_circle(symbol):
    radius = dimension_choice("Radius")

    for i in range(radius):
        spaces = radius - i
        for j in range(spaces, 0, -1):
            print(" ", end="")
        for j in range((radius - spaces) * 2, 0, -1):
            print(symbol, end = "")
        print()

    for i in range(radius, 0, -1):
        spaces = radius - i
        for j in range(spaces, 0, -1):
            print(" ", end="")
        for j in range((radius - spaces) * 2, 0, -1):
            print(symbol, end = "")
        print()


def shape_choice(shapes):
    user_choice = input(f"What would you like to draw? {shapes}\n").lower()
    if not user_choice in shapes:
        invalid()
        return shape_choice(shapes)
    return user_choice
    
def symbol_choice():
    choice = input("Enter the symbol you would like to user to draw the shapes with: ")
    if(len(choice) == 1):
        return choice
    print("Please choose a single character!")
    press_enter()
    return symbol_choice()

# Passes in the direction you are entering in (e.g. length, width)
def dimension_choice(dim):
    choice = input(f"Please enter a size for the {dim}: ")
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
    amount = curr_amount_choice()
    curr_breakdown(amount)
    print("\nThanks for using our conversion service today!")
    press_enter()

def curr_amount_choice():
    choice = input("Please enter the amount of money you have: ")
    try:
        num = float(choice)
        if(num < 0):
            print("Please enter a positive value")
            return curr_amount_choice()
        return num
    except ValueError:
        print("Please enter a float value")
        press_enter()
        return curr_amount_choice()

def curr_breakdown(amount):
    # multiplies by 100 to make calculation easier to handle
    prepped_num = int(amount * 100)
    
    # Dollars
    rem = handle_breakdown(prepped_num, 100, "Dollar")

    # Quarters
    rem = handle_breakdown(rem, 25, "Quarter")

    # Dimes
    rem = handle_breakdown(rem, 10, "Dime")

    # Nickels
    rem = handle_breakdown(rem, 5, "Nickel")

    # Pennies
    rem = handle_breakdown(rem, 1, "Pennie")

    
def handle_breakdown(rem, div, name):
    # check for 0 in rem to know when breakdown to prevent continuing printing
    if(not rem or rem == 0):
        return
    
    # Gets the number of that denomination is available
    count = int(rem / div)

    # Checks to see if there are any of this denomination before printing
    if(count < 1):
        return int(rem % div)
    
    print(f"You have {count} {name}(s)")

    # Returns the remainder, to continue calculation
    return int(rem % div)
    

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