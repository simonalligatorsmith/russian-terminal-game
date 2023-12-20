# A game to practice Russian pronouns
{"писатель":"Саймон"}

from collections import namedtuple
from random import sample
from os import system


nom_pros = dict(zip(['case_name','sg_1', 'sg_2', 'sg_3_m', 'sg_3_f', 'sg_3_x', 'pl_1', 'pl_2', 'pl_3'],
                    ['Nominative','я','ты','он','она','оно','мы','вы','они']))

# print out a pronoun table with one pronoun missing
# return the missing pronoun, which will be used by the game loop
def show_game_table(pronoun_dict):

    # Select random tuple indexed representing a pronoun to blank out (not the case name)
    keys = list(pronoun_dict.keys())
    keys.remove('case_name')
    toRemove = sample(keys,1)[0]

    # Blank out one word
    removedPronoun = pronoun_dict[toRemove]
    pronoun_dict[toRemove] = "« »"

    # Print table with blanks
    print(
    f"{pronoun_dict['case_name']} Pronouns\n"+
    "-----------------------\n"+
    f"| {pronoun_dict['sg_1']}".ljust(11)   + f"| {pronoun_dict['pl_1']}".ljust(11) + "|\n" +
    f"| {pronoun_dict['sg_2']}".ljust(11)   + f"| {pronoun_dict['pl_2']}".ljust(11) + "|\n" +
    f"| {pronoun_dict['sg_3_m']}".ljust(11) + f"| {pronoun_dict['pl_3']}".ljust(11) + "|\n" +
    f"| {pronoun_dict['sg_3_f']}".ljust(11) +  "|          |\n" +
    f"| {pronoun_dict['sg_3_x']}".ljust(11) +  "|          |\n" +
    "-----------------------"
    )

    # return the removed pronoun, which makes guessing game easier to implement
    return removedPronoun

#print(sample(Pronoun._fields[1:],1))
#show_table(nom_pros)

while True:
    missing_pronoun = show_game_table(nom_pros.copy())
    guess = input("\n\nType the missing pronoun: ")

    if guess == missing_pronoun:
        input("Correct!\nPress *enter* to continue")

    elif guess == 'quit' or guess == 'йгше':
        break
        # exit game

    else:
        input("Not quite.\nPress *enter* to try again")


    #clear screen
    system('clear')
