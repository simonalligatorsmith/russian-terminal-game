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
    # print word to screen once with no edits
    while True:
        typed_guess = input(f"Type the word \"{word}\"\n")
        # take user input; if match word, move on. else, go to previous step
        if typed_guess == word:
            print("You win!")
            break
        
        else: #
            print("Not quite.")
        

        
    
    # blank out 2 characters of word, replace with underscore
    # require user input of original word
    # repeat blanking-out and underscore-replacing until word is all underscores
    # when user inputs word correctly, congratulate
    # move on to next word


input("Press enter to exit? Sounds kinda backwards to me.")
