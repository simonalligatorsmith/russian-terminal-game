# A game to practice Russian pronouns
{"писатель":"Саймон"}

from collections import namedtuple
from random import sample
from os import system


nom_pros = dict(zip(['case_name','sg_1', 'sg_2', 'sg_3_m', 'sg_3_f', 'sg_3_x', 'pl_1', 'pl_2', 'pl_3'],
                    ['Nominative','я','ты','он','она','оно','мы','вы','они']))

gen_pros = dict(zip(['case_name','sg_1', 'sg_2', 'sg_3_m', 'sg_3_f', 'sg_3_x', 'pl_1', 'pl_2', 'pl_3'],
                    ['Genitive','меня','тебя','его','ёо','его','нас','вас','их']))

dat_pros = dict(zip(['case_name','sg_1', 'sg_2', 'sg_3_m', 'sg_3_f', 'sg_3_x', 'pl_1', 'pl_2', 'pl_3'],
                    ['Dative','мне','тебе','ему','ей','ему','нам','вам','им']))

acc_pros = dict(zip(['case_name','sg_1', 'sg_2', 'sg_3_m', 'sg_3_f', 'sg_3_x', 'pl_1', 'pl_2', 'pl_3'],
                    ['Accusative','меня','тебя','его','её','его','нас','вас','их']))

ins_pros = dict(zip(['case_name','sg_1', 'sg_2', 'sg_3_m', 'sg_3_f', 'sg_3_x', 'pl_1', 'pl_2', 'pl_3'],
                    ['Instrumental','мной','тобой','им','ею','им','нами','вами','ими']))

pre_pros = dict(zip(['case_name','sg_1', 'sg_2', 'sg_3_m', 'sg_3_f', 'sg_3_x', 'pl_1', 'pl_2', 'pl_3'],
                    ['Prepositional','мне','тебе','нём','ней','нём','нас','вас','них']))

pros_list = [nom_pros,gen_pros,dat_pros,acc_pros,ins_pros,pre_pros]

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
    #clear screen
    system('clear')

    # select a random pronoun table index
    pron_index = sample(range(0,6),1)[0]

    missing_pronoun = show_game_table(pros_list[pron_index].copy())
    guess = input("\n\nType the missing pronoun: ")

    if guess == missing_pronoun:
        input("Correct!\nPress *enter* to continue")

    elif guess == 'quit' or guess == 'йгше':
        break
        # exit game

    else:
        input("Not quite.\nPress *enter* to try again")
