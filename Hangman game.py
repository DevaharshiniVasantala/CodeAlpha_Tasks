import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'aesthetic', 'gossip', 'fashion', 'galaxy']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           |
        ''',
        '''
           ------
           |    |
           |    
           |    
           |    
           |
        '''
    ]
    return stages[tries]

def play():
    word = choose_word().lower()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6
    print("Welcome to Hangman!")

    while tries > 0 and word_letters:
        print(display_hangman(tries))
        print("Word: ", ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Wrong guess.")

    if not word_letters:
        print(f"Congrats! You guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    play()