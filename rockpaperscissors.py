import random   #modules

def game():
    choices=['rock','paper','scissors']
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    computer_choice=random.choice(choices)
    if user_choice==computer_choice:
        return f"You chose {user_choice}. Computer choice {computer_choice}. It's a tie!"
    elif(user_choice=='rock' and computer_choice=='scissors') or\
        (user_choice=='scissors' and computer_choice=='paper') or\
        (user_choice=='paper' and computer_choice=='rock'):
        return f"You chose {user_choice}. Computer chose {computer_choice}. You win!"
    else:
        return f"You chose {user_choice}. Computer chose {computer_choice}. You lose!"

def main():
    while True:
        print(game())
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

main()
