{"писатель":"Саймон"}
"""
Terminal game that helps you learn spelling of words
DONE - MVP (minimum viable product)
    10 words. Output one to screen, makes you type it out and enter it. Takes away 2 letters each time until word is blank and you type from memory. Then congratulate and move on to next word
    
    
Next:
    store learned/practiced words in another file (database one day) along with date of practice
        review learned words periodically
        
    get big wordlist from frequency list
    
"""
from os import system
from random import sample
# clear screen
system('cls')

with open("словарь.txt", encoding='utf_8') as word_file:
    word_list = [w.strip() for w in word_file.readlines()]
    
    #sample 10 random words. Allow to customize amount, or too much input required?
    word_list = sample(word_list,k=10)
    
    
input("Welcome to the spelling game! Type the words as their letters disappear.\n" +
      "Enter 'help' if you need help, 'skip' to skip a word. Press ENTER to start the game.\n")
    
for word in word_list:
    """
    Notes for even, odd word '_' transformer where N is step number, L is length of word, W is word. This algorithm replaces the letters with '_' from the inside out.

        Perform each algorithm till N = L/2 + L%2
        
        EVEN: W = W[0:(L/2)-N] + '_'*2*N + W[(L/2)+N:]
        ODD:  W = W[0:int(L/2)+1+N] + '_'*((2*N)-1) + W[int(L/2)+N:]
        
        BOTH: W = W[0:int(L/2)+(L%2)+N] + '_'*((2*N)-(L%2)) + W[int(L/2)+N:]
    """

    word_len = len(word) # Length of word
    edited_word = word   # Same as word from list, but gets edited
    rounds   = 0         # Num of rounds completed for this word
    odd_factor = word_len % 2 # is 1 if word_len is odd, or 0 if even
    
    while rounds < (word_len / 2):
        #print(f"rounds is {rounds}\nformula for edited_word pt_2 is {int(word_len/2) + rounds  + odd_factor}")
        """
        The list comprehension below is complex, but this is how it works.
        
        Right slice:
            take characters from start of word until the index halfway through the word + the odd_factor for odd numbers, minus number of rounds.
        Underscore portion:
            write a number of underscores equal to twice the number of rounds, minus the odd_factor
        Left slice:
            take characters from index @ halfway through the word, plus the number of rounds, minus the final subterm which is equivalent to "add the odd_factor to this index if this is the first cycle, otherwise do nothing."
        """
        edited_word = edited_word[0 : int(word_len/2) + odd_factor - rounds] + \
                      '_'*((2*rounds) - odd_factor) + \
                      edited_word[ int(word_len/2) + rounds  + int(not rounds)*odd_factor : ]
        rounds += 1


        # handle input of correct input, incorrect input, "help", or "skip"
        while True:
            typed_guess = input(f"Type the word \"{edited_word}\"\n")
            # take user input; if match word, move on. else, go to previous step
            if typed_guess == word:
                input("Хорошо! *Enter* to continue\n")
                # clear screen
                system('cls')
                break
                
            elif typed_guess == 'help':
                # reset the word
                input("No worries, let's take it from the top.")
                system('cls')
                edited_word = word
                rounds = 1
                
            elif typed_guess == 'skip':
                # skip to next word
                input("Skipping to next word - *Enter*")
                system('cls')
                rounds = word_len/2
                break
            
            else: #
                input("Not quite. *Enter* to continue\n")
                # clear screen
                system('cls')

# Outro message         
input("GAME OVER ... but only cause you beat it!!😁")
