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

with open("словарь.txt", encoding='utf_8') as word_file:
    word_list = [w.strip() for w in word_file.readlines()]
    
for word in word_list:

    word_len = len(word) # L
    edited_word = word   # W
    cycles   = 0         # N
    odd_factor = word_len % 2 # will be 1 if word_len is odd, or 0 if word_len is even
    
    print(edited_word)
    
    while cycles < (word_len / 2) + (odd_factor):
        print(f"DEBUG: cycle is {cycles}.")
        edited_word = edited_word[0 : int(word_len/2) + (odd_factor) - cycles] + '_'*((2*cycles) - (odd_factor)) + edited_word[ int(word_len/2) + cycles : ]
        cycles += 1
        print(edited_word)
        
        




    # print word to screen once with no edits
    while True:
        typed_guess = input(f"Type the word \"{word}\"\n")
        # take user input; if match word, move on. else, go to previous step
        if typed_guess == word:
            print("Хорошо!")
            break
        
        else: #
            print("Not quite.")
            
"""
Notes for even, odd word '_' transformer where N is step number, L is length of word, W is word. This algorithm replaces the letters with '_' from the inside out.

    Perform each algorithm till N = L/2 + L%2
    
    EVEN: W = W[0:(L/2)-N] + '_'*2*N + W[(L/2)+N:]
    ODD:  W = W[0:int(L/2)+1+N] + '_'*((2*N)-1) + W[int(L/2)+N:]
    
    BOTH: W = W[0:int(L/2)+(L%2)+N] + '_'*((2*N)-(L%2)) + W[int(L/2)+N:]
"""
        

        
    
    # blank out 2 characters of word, replace with underscore
    # require user input of original word
    # repeat blanking-out and underscore-replacing until word is all underscores
    # when user inputs word correctly, congratulate
    # move on to next word


input("Press enter to exit? Sounds kinda backwards to me.")
