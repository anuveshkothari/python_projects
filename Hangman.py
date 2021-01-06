from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words) # choose a random word from a list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in a word
    used_letter = set()  # set of used letters
    alphabets = set(string.ascii_uppercase)
    lives = 5

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cdef']) = 'a b cd'
        print("You have", lives, "left, You have used these letters: ", " ".join(used_letter))

        current_word = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(current_word))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets.difference(used_letter):
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -=1
        elif user_letter in used_letter:
            print('You have already guessed the letter. Please try again.')
        else:
            print('Invalid Character. Please try again')

    # after guessing the word
    if lives > 0:
        print("You won!!, Word is:", word)
    else:
        print('You lose!!, Word was:', word)


if __name__ == '__main__':
    hangman()




