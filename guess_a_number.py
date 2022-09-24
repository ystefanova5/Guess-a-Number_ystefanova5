import random

computer_number = random.randint(1, 100)
the_guess_is_correct = False

while not the_guess_is_correct:
    player_input = int(input("Guess the number (1-100): "))
    if player_input not in range(1, 101):
        print("Invalid input. Try again...")
        continue
    if player_input == computer_number:
        the_guess_is_correct = True
        print(f"You guessed it! The number is {computer_number}")
        break
    else:
        if player_input > computer_number:
            print("Too high! Try with a lower number...")
        elif player_input < computer_number:
            print("Too low! Try with a higher number...")