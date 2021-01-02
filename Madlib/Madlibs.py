"""
String concatination (how to put string together)
for eg: we want to say something like " Kindly check my profile on _______
"""
# site = "Linkdin"
# number of ways to append a string
# print("Kindly check my profile on "+ site)
# print("Kindly check my profile on {}".format(site))
# print(f"Kindly check my profile on {site}")

from Madlib import code,Happy,Hunger_games,Zombie
import random

if __name__ == "__main__":
    m = random.choice([Hunger_games,Zombie,Happy,code])
    m.madlib()
