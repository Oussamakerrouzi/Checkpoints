import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    while True:
        guess_input = input("Enter your guess: ")
        guess = int(guess_input)
        
        if guess > secret_number:
            print("Your guess is too high. Guess again.")
        elif guess < secret_number:
            print("Your guess is too low. Guess again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break

guess_the_number()