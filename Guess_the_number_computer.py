from random import randint

def Guess_the_number(num):
    random_number = randint(1,num)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f"Guess the number between 1 to {num}: "))
        if guess_number > random_number:
            print("Sorry! guess again, too high")
        elif guess_number < random_number:
            print("Sorry! guess again, too low")
        else:
            print("Wow! you guessed the number correctly")


if __name__ == '__main__':
    Guess_the_number(100)