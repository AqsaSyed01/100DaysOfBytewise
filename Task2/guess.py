import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    
    print("Guess the number game!")
    print("I have generated a random number between 1 and 100.")
    
    # Loop until the user guesses the number
    while guess != number_to_guess:
        try:
            # Take input from the user
            guess = int(input("Enter your guess: "))
            
            # Provide feedback to the user
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number: {number_to_guess}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
        
# Run the game
guess_the_number()
