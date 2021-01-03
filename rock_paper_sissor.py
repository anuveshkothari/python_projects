from random import choice

def is_play():
    player = input("what's your choice? 'r' for rock, 'p' for paper, 's' for sissor: ")
    computer = choice(['r', 's', 'p'])
    # r>s, s>p, p>r
    if is_player_win(player, computer):
        print("Yay, congrats!! you won")
    else:
        print("Sorry!! you lose, better luck next time")

def is_player_win(player, computer):

    if (player =='r' and computer == 's') or (player == 's' and computer == 'p') \
            or (player == 'p' and computer == 'r'):
        return True
    return False

if __name__ == '__main__':
    is_play()
