import random

def choose_random_word():
    # File operations
    with open("hangman_game_words.txt", "r") as file:
        # Source of the words: https://www.hangmanwords.com/words
        words = file.readlines()
    return random.choice(words).strip().lower()

def display_word(word, guessed_letters):
    # Display the current state of the word, with guessed letters revealed and others hidden as underscores
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman_game():
    word_to_guess = choose_random_word()
    guessed_letters = []
    attempts = 5
    
    print("Welcome to Hangman!")
    
    # Main game loop
    while attempts > 0:
        print("\nAttempts left:", attempts)
        print(display_word(word_to_guess, guessed_letters))

        # Get a letter from the user
        guess = input("Guess a letter: ").lower()

        # Check for invalid input (non-alphabetic or more than one letter)
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has been guessed before
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess!")

        # Check if the entire word has been guessed
        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    # End of the game: either the word is guessed or the attempts are exhausted
    if attempts == 0:
        print("Sorry, you ran out of attempts. The correct word was:", word_to_guess)

if __name__ == "__main__":
    hangman_game()
