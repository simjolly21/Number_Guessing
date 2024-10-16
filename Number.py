# Solve this problem by using Python

import random
import time

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Difficulty levels and their respective chances
    difficulty_levels = {
        'easy': 10,
        'medium': 5,
        'hard': 3
    }

    while True:
        # Difficulty selection
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            difficulty = 'easy'
            chances = difficulty_levels[difficulty]
        elif choice == '2':
            difficulty = 'medium'
            chances = difficulty_levels[difficulty]
        elif choice == '3':
            difficulty = 'hard'
            chances = difficulty_levels[difficulty]
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        number_to_guess = random.randint(1, 100)
        attempts = 0
        start_time = time.time()

        print(f"\nGreat! You have selected the {difficulty.capitalize()} difficulty level.")
        print(f"You have {chances} chances to guess the correct number.")

        while attempts < chances:
            try:
                guess = int(input("\nEnter your guess: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    attempts -= 1
                    continue

                if guess == number_to_guess:
                    elapsed_time = time.time() - start_time
                    print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                    print(f"It took you {elapsed_time:.2f} seconds.")
                    break
                elif guess < number_to_guess:
                    print("Incorrect! The number is greater than your guess.")
                else:
                    print("Incorrect! The number is less than your guess.")

                if attempts == chances:
                    print(f"Sorry, you've run out of chances. The correct number was {number_to_guess}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    number_guessing_game()
