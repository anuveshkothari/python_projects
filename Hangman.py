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

    while len(word_letters) > 0:
        # letters used
        # ' '.join(['a', 'b', 'cdef']) = 'a b cd'
        print("You have used these letters: ", " ".join(used_letter))

        # current word is [W - R D]
        # current_word = []
        # for letter in word:
        #     if letter in used_letter:
        #         current_word.append(letter)
        #     else:
        #         current_word.append('-')
        current_word = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(current_word))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets.difference(used_letter):
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letter:
            print('You have already guessed the letter. Please try again.')
        else:
            print('Invalid Character. Please try again')

    # after guessing the word
    print(word)


if __name__ == '__main__':
    hangman()




