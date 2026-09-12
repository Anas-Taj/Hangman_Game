import random

# Visual representation of the hangman for each incorrect guess (0 to 6)
HANGMAN_STAGES = [
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

def play_hangman():
    # Predefined list of 5 words
    words = ["rabbit", "monkey", "donkey", "python", "jaguar"]
    
    # Randomly select a word from the list
    secret_word = random.choice(words)
    
    # State tracking variables
    guessed_letters = []       # List to track all guessed letters
    incorrect_guesses = 0      # Counter for wrong attempts
    max_incorrect_guesses = 6  # Limit of wrong guesses allowed

    print("========================================")
    print("        WELCOME TO HANGMAN GAME         ")
    print("========================================\n")
    print(f"Guess the secret word related to animals! You have {max_incorrect_guesses} incorrect guesses allowed.\n")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Build the current displayed word with blanks and guessed letters
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        
        # Display current hangman visual stage
        print(HANGMAN_STAGES[incorrect_guesses])

        # Display current word status and game stats
        print(f"Word: {' '.join(display_word)}\n")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}\n")
        
        # Check if the player has guessed all letters (Win condition)
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word correctly!")
            break

        # Get player input
        guess = input("Enter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Invalid input. Please enter a single alphabetical letter.\n")
            continue
        
        if guess in guessed_letters:
            print(f">> You already guessed '{guess}'. Try a different letter.\n")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if guess is in the secret word
        if guess in secret_word:
            print(f">> Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f">> Sorry! '{guess}' is not in the word.\n")

    # Game Over check (Loss condition)
    if incorrect_guesses == max_incorrect_guesses:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("========================================")
        print("              GAME OVER!                ")
        print("========================================")
        print(f"You ran out of guesses! The secret word was: '{secret_word}'.")

if __name__ == "__main__":
    play_hangman()