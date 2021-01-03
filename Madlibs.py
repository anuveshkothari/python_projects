
from Madlib import code,Happy,Hunger_games,Zombie
import random

if __name__ == "__main__":
    m = random.choice([Hunger_games,Zombie,Happy,code])
    m.madlib()
