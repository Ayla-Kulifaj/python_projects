import random

class Hangman:
    def __init__(self, word_list):
        self.words = word_list
        self.word = random.choice(self.words).upper()
        self.guessed_letters = set()
        self.tries = 6

    def display_word_state(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            return False, "Already guessed"

        self.guessed_letters.add(letter)

        if letter not in self.word:
            self.tries -= 1
            return False, "Incorrect guess"
        
        return True, "Correct guess"

    def is_word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def has_tries_left(self):
        return self.tries > 0

def play_hangman(word_list):
    game = Hangman(word_list)

    while game.has_tries_left():
        print(game.display_word_state())
        guess = input("Enter a letter: ")

        correct, message = game.guess_letter(guess)
        print(message)

        if game.is_word_guessed():
            print(f"Congratulations! You've guessed the word {game.word}!")
            return

    print(f"You've run out of tries. The word was {game.word}.")

if __name__ == "__main__":
    words = ["python", "hangman", "programming", "developer", "challenge"]
    play_hangman(words)
