import random

def random_guessing_game():
  while True:
    number = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < number:
            print("The number is higher!")
        elif guess > number:
            print("The number is lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    play_again=input("Do you want to play again? (yes/no)").lower()
    if play_again != "yes":
          break
random_guessing_game()
