# Problem Set 2, hangman.py

# Name: Jiwon, Choi
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def print_hangman_title():
    print(r"""
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
    """)



def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def is_word_guessed(secret_word, letters_guessed):
    
    letters_guessed = "".join(letters_guessed)

    if secret_word == letters_guessed :
        return True 
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    guessed=""
    for i in secret_word:
        if i in letters_guessed:
            guessed+=i
        elif i not in letters_guessed:
            guessed+="_"
    return guessed
#print(get_guessed_word("apple",["e","t","t","p","u"]))
            
        
        

def get_available_letters(letters_guessed):

    alphabet="abcdefghijklmnopqrstuvwxyz"
    if letters_guessed == "":
        return alphabet
    for i in letters_guessed:
        if i in alphabet:
            alphabet=alphabet.replace(i,"")
    return alphabet
#print(get_available_letters(["a","b","z","y"]))
         

def hangman(secret_word):
    print_hangman_title()
    
    chance, warn =6, 3

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warn} warnings left.")
    print("<- - - - - - ->\n")
    choose=""

    while chance>0 :
        print(f"You have {chance} guesses left")
        print(f"Available letters:{get_available_letters(choose)}")
        choose2=input("Please guess a letter: ")

        if choose2=="*":
            hangman_with_hints(get_guessed_word(secret_word, choose))

        elif choose2 not in "abcdefghijklmnopqrstuvwxyz":
            if warn ==0 or warn=="no": 
                chance-=1
                warn="no"
            else: 
                warn-=1
            print(f"Oops! That is not a valid letter. You have {warn} warnings left: {get_guessed_word(secret_word, choose)}")
        elif choose2 in get_guessed_word(secret_word, choose):
            if warn ==0 or warn=="no": 
                chance-=1
                warn="no"
            else: 
                warn-=1
            print(f"Oops! You've already guessed that letter. You have {warn} warnings left:{get_guessed_word(secret_word, choose)}")
            
        else:
           choose+=choose2
           if choose2 in secret_word:
            print("Good guess: ",get_guessed_word(secret_word, choose))
           else:
            if choose2 in "aeiuo":
                chance-=2
            else:
                chance-=1
            print("Oops! That letter is not in my word.")

        if is_word_guessed(secret_word, get_guessed_word(secret_word, choose))==True:
            print("Congratulations, you won!")
            print(f"Your total score for this game is:{chance*len(secret_word)}")
            chance=5
            break
    
        print("-------------------------")
    if chance!=5:
        print(f'Sorry, you ran out of guesses. The word was "{secret_word}".')

#hangman(choose_word(load_words()))

def match_with_gaps(my_word, other_word):

    if len(my_word)!=len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i]==other_word[i] or my_word[i]=="_":
                continue
            else:
                return False
        return True
        

def show_possible_matches(my_word):
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()

    possible=[]
    for word in wordlist:
        if len(word)==len(my_word):
            if match_with_gaps(my_word,word):
                possible.append(word)
    
    if possible:
        print("Possible word matches are:")
        print(" ".join(possible))
    else:
        print("No match found")
                            
            



def hangman_with_hints(secret_word):

    print()
    print("[hints] You chose a hint, I'll show you the possible words.")
    return show_possible_matches(secret_word)

 



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = choose_word(load_words())
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(load_words())
    #hangman_with_hints(secret_word)
