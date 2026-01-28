import art
import random

def check_answer(user_guess, answer, turns):
    if user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess < answer:
        print("Too low.")
        return turns - 1 

def set_difficulty(EASY_LEVEL_TURNS, HARD_LEVEL_TURNS):
    level = input("Choose a difficulty. Type 'easy' or 'hard': " ).lower()
    return EASY_LEVEL_TURNS if level == "easy" else HARD_LEVEL_TURNS

def game():   
    print(art.logo)
    print("Welcome to the guessing game! I'm thinking of a number between 1 and 100. Can you guess it?")
    
    EASY_LEVEL_TURNS = 10
    HARD_LEVEL_TURNS = 5
    answer = random.randint(1, 100)
    turns = set_difficulty(EASY_LEVEL_TURNS, HARD_LEVEL_TURNS)
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if guess == answer:
            print("\nYou win!, thx for playing :)")
            return
        if turns == 0:
            print("\nYou've run out of guesses, you lose.")
            print(f"The answer was: {answer}")
            return  
        
if __name__ == "__main__":
    game()
