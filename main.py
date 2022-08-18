import random 
print("Welcome to the Number Guessing Game!")

EASY_LEVEL = 10
HARD_LEVEL = 5
number = random.randint(1,100)

def level():
    level = input("Do you want to play 'hard' or 'easy'? ")
    if level == "hard":
        return HARD_LEVEL
    elif level == "easy":
        return EASY_LEVEL

def correct(guess, number, turns):
    if guess > number:
        print("Too high")
        return turns - 1
    if guess < number:
        print("Too low ")
        return turns - 1
    elif guess == number:
        print("Correct!")

def play():
    guess = 0
    turns = level()
    while guess != number:
        print(f"You have {turns} guesses left")
        guess = int(input("What is your guess? "))
        turns = correct(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses")
            return
        elif guess != number:
            print("Guess again.")

play()


