from random import randint


def guess_the_number_user(num):
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


def guess_the_number_computer(num):
    print(f"Hey computer!! Guess a number between 1 and {num}")
    low = 1
    high = num
    feedback = ''
    while feedback.lower() != 'c':
        if low != high:
            guess_number = int(randint(low, high))
        else:
            guess_number = low # or it can be high b/c both are same
        feedback = input(f"Is the {guess_number} is too low(l) or too high(h) or correct(c)??")
        if feedback.lower() == 'l'.lower():
            low = guess_number + 1
        elif feedback.lower() == 'h':
            high = guess_number - 1

    print(f"Yay, congrats!! you have guessed the number{guess_number} correctly!!")


def main():
    game = int(input("If you want to guess a number, press 1\nYou want computer to guess a number, press 2: "))
    if game == 1:
        guess_the_number_user(1000)
    elif game == 2:
        guess_the_number_computer(1000)
    else:
        print("Invalid input!!")


if __name__ == '__main__':
    main()