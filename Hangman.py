import random

# List of 5 predefined words
words = ['apple', 'banana', 'grape', 'orange', 'peach']

# Choose a random word from the list
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

# Create the hidden version of the word (e.g., "_ _ _ _ _")
display_word = ['_'] * len(word_to_guess)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while incorrect_guesses < max_incorrect_guesses and '_' in display_word:
    print("\nWord: ", ' '.join(display_word))
    print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Sorry, '{guess}' is not in the word.")

# End of game
if '_' not in display_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nOut of guesses! The word was:", word_to_guess)
