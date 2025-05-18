import random
def hangman_game():
    words=["python","hangman","programming","challenge"]
    word=random.choice(words)
    guessed=["_"]*len(word)
    attempts=6
    guessed_letters = set()
    print("welcome to Hangman!")
    while attempts > 0 and "_" in guessed:
        print("\nWord:","".join(guessed))
        guess=input("Guess a letter:").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("enter a single alphabet.")
        if guess in guessed_letters:
            print("You already guessed that.")
            continue
        if guess in word:
            for i in range(len(word)):
                if word[i]== guess:
                    guessed[i] = guess
        else:
            attempts-=1
            print(f"Wrong guess! Attempts left: {attempts}")
    if "_" not in guessed:
        print("You won! The word was:",word)
    else:
        print("Game over! The word was:",word)
hangman_game()
