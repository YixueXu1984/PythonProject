from random import randrange

number = randrange(10)

user_input = input("Would you like to play? (Y/N)").lower()
if user_input == 'n':
    exit(0)

while True:
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
        break
    elif user_number > number:
        print("The number is smaller than your guess.")
    elif user_number < number:
        print("The number is larger than your guess.")
    else:
        print("Oops! Something went wrong...")