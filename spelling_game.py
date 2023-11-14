{"писатель":"Саймон"}
"""
Terminal game that helps you learn spelling of words
MVP (minimum viable product)
    10 words. Output one to screen, makes you type it out and enter it. Takes away 2 letters each time until word is blank and you type from memory. Then congratulate and move on to next word
    
    
Next:
    store learned/practiced words in another file (database one day) along with date of practice
        review learned words periodically
        
    get big wordlist from frequency list
    
"""
from os import system
from random import shuffle
# clear screen
system('cls')

with open("словарь.txt", encoding='utf_8') as word_file:
    word_list = [w.strip() for w in word_file.readlines()]
    # shuffle wordlist so you practice something different each time
    shuffle(word_list)
    
    
input("Welcome to the spelling game! Type the words as their letters disappear. Enter the word 'help' if you need help.\n**press ENTER to continue*")
    
for word in word_list:
    """
    Notes for even, odd word '_' transformer where N is step number, L is length of word, W is word. This algorithm replaces the letters with '_' from the inside out.

        Perform each algorithm till N = L/2 + L%2
        
        EVEN: W = W[0:(L/2)-N] + '_'*2*N + W[(L/2)+N:]
        ODD:  W = W[0:int(L/2)+1+N] + '_'*((2*N)-1) + W[int(L/2)+N:]
        
        BOTH: W = W[0:int(L/2)+(L%2)+N] + '_'*((2*N)-(L%2)) + W[int(L/2)+N:]
    """

    word_len = len(word) # L
    edited_word = word   # W
    cycles   = 0         # N
    odd_factor = word_len % 2 # will be 1 if word_len is odd, or 0 if word_len is even
    
    #print(f"The word is {edited_word}\nodd_factor is {odd_factor}\nint(word_len / 2) is {int(word_len/2)}")
    
    while cycles < (word_len / 2):
        #print(f"cycles is {cycles}\nformula for edited_word pt_2 is {int(word_len/2) + cycles  + odd_factor}")
        """
        This blasphemy of a list comprehension slowly replaces the middle character(s) with underscores.
        It does this by splitting the word into the right slice, underscore portion, and left slice.
        The slices work like so:
        
        Right slice:
            take characters from start of word until index halfway through the word + the odd_factor for odd numbers, minus number of cycles.
        Underscore portion:
            write a number of underscores equal to twice the number of underscores, minus the odd_factor
        Left slice:
            take characters from index @ halfway through the word, plus the number of cycles, minus the ugly term that says "add the odd_factor if this is the first cycle, otherwise do nothing.
        """
        edited_word = edited_word[0 : int(word_len/2) + odd_factor - cycles] + '_'*((2*cycles) - odd_factor) + edited_word[ int(word_len/2) + cycles  + int(not cycles)*odd_factor : ]
        cycles += 1
        #print(edited_word)
        

        # print word to screen once with no edits
        while True:
            typed_guess = input(f"Type the word \"{edited_word}\"\n")
            # take user input; if match word, move on. else, go to previous step
            if typed_guess == word:
                input("Хорошо! *Enter* to continue\n")
                # clear screen
                os.system('cls')
                break
                
            elif typed_guess == 'help':
                # reset the word
                input("No worries, let's take it from the top.")
                edited_word = word
                cycles = 1
            
            else: #
                input("Not quite. *Enter* to continue\n")
                # clear screen
                os.system('cls')
            
    print("Nice work!")

        

        
    
    # blank out 2 characters of word, replace with underscore
    # require user input of original word
    # repeat blanking-out and underscore-replacing until word is all underscores
    # when user inputs word correctly, congratulate
    # move on to next word


input("Press enter to exit? Sounds kinda backwards to me.")
