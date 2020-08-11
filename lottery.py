import random

def menu():
    # Ask player for numbers
    user_numbers = get_player_numbers()
    
    # Calculate lottery numbers
    lottery_numbers = create_lottery_number()
    
    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)

    print("You matched {}. You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))
     

# User can pick six nnumbers
def get_player_numbers():
    number_csv = input("Enter your 6 numbers, seperated by commas: ")
    number_list = number_csv.split(",")
    return {int(number) for number in number_list}

# Lottery calculates 6 random numbers between 1 and 20
def create_lottery_number():
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 20))
    return numbers

menu()
