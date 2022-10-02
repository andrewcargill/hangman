import random

HANGMAN = ['''
        _ _ _ _
       |       
       |       
       |      
       |      
       |      
       |      
    #==#==#''', '''
        _ _ _ _
       |       |
       |       0
       |       
       |      
       |      
       |     
    #==#==#''', '''
        _ _ _ _
       |       |
       |       0
       |       | 
       |       |
       |      
       |     
    #==#==#''', '''
        _ _ _ _
       |       |
       |       0
       |      /|\ 
       |       |
       |       
       |     
    #==#==#''', '''
        _ _ _ _
       |       |
       |       0
       |      /|\ 
       |       |
       |      / 
       |     -   
    #==#==#''', '''
        _ _ _ _
       |       |
       |       0
       |      /|\ 
       |       |
       |      / \ 
       |     -   - 
    #==#==#''']

#for x in range(len(HANGMAN)):
#    print(HANGMAN[x])

class game_start():
    game_start_graphic = '''
              @                        @         @ 
    @        @@                       @@        @@  
   @@       @@@@                     @@@@      @@@@ 
   ||        ||                       ||        ||
——————  W E L C O M E   T O   H A R R Y ' S  —————————

HHH      HHH      AAA      NNN       NNN      GGGGG
HHH      HHH    AAA AAA    NNN N     NNN    GGG    GGG
HHH      HHH   AAA   AAA   NNN  N    NNN  GGG
HHHHHHHHHHHH  AAAAAAAAAAA  NNN   N   NNN  GGG    
HHH      HHH  AAA     AAA  NNN    N  NNN  GGG    GGGGG
HHH      HHH  AAA     AAA  NNN     N NNN   GGG     GGG
HHH      HHH  AAA     AAA  NNN      NNNN    GGGGGGG

MMM      MMM      AAA      NNN       NNN     _ _ _ _
MMMM    MMMM    AAA AAA    NNN N     NNN    |       |
MMM M  M MMM   AAA   AAA   NNN  N    NNN    |       0
MMM  MM  MMM  AAAAAAAAAA   NNN   N   NNN    |      /|\  
MMM      MMM  AAA    AAA   NNN    N  NNN    |       |
MMM      MMM  AAA    AAA   NNN     N NNN    |      / \ 
MMM      MMM  AAA    AAA   NNN      NNNN    |     -   -  
                                            |
#==#==#==#==  CREATED BY ANDREW CARGILL  #==#==#==#==#

\n'''
    print(game_start_graphic)

## Rules of the game
def enter_name():
    print("THE RULES ARE SIMPLE... YOU JUST NEED TO GUESS THE WORD!")
    print("BUT, IF YOU MAKE 5 WRONG GUESSES THEN POOR HARRY HANGS!")
    print("GOOD LUCK.\n")


# this is where all words are stored  
word_bank = ["ramble", "tan", "pick", "run", "distance", "today", "thanks", "plant", "insect"]

#A blank list that will show any correct letters
guess_list = ["- ", "- ", "- ", "- ", "- ", "- ", "- ", "- "]

#Generates a random word and breaks down into a list of letters
def random_word():
    magic_word = random.choice(word_bank)
    magic_word_list = []
    for letter in magic_word:
        magic_word_list.append(letter)
        magic_word_length = len(magic_word_list)
        

    return magic_word,magic_word_list,magic_word_length


#Creates a display of the word without letters
def word_display(x):
    n = len(guess_list)
    for i in range(0, n - x):
        guess_list.pop()
    return guess_list
 
 
 # if letter is in word 
    ## DONE message to user "Nice! X is a great guess"
    ## DONE Update the display_word
    ## DONE show same 'hangman'
# else if letter is not in word
    ## DONE message to user "Unlucky, thats not in word"
    ## DONE add a step to the hangman 
    ## DONE add the letter to the wrong guesses 

# DONE Then - ask for a new letter


def user_guess(guess, answer, display_word):
    guess = guess.lower()  #Players guess (letter)
    
    if guess in answer:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(HANGMAN[0]) #Needs to take previous Hangman and return same - NEW FUNCTION(E)
        print("-=-=        =-=-=-=-=-=-=-")
        print("\n")
        print("Yes! '" + guess.upper()+ "' was a great guess!") # Text - USE CODE(D)
        letter_index = answer.index(guess) #Finds index - USE CODE
        display_word[letter_index] = guess.upper() # updates display_word - USE CODE(C)
        print("\n")
        print(display_word)
        print("\n")
        print("wrong guesses: ") ### Wrong guess - CREATE FUNCTION TO MANAGE & RETURN(B)
        print("\n")
        next_guess = input("...Give me another letter to try!: ") #SEND TO NEW FUNCTION(A)
    else:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(HANGMAN[1]) # needs to take pervious hangman and add 1 - CREATE FUNCTION(E)
        print("-=-=        =-=-=-=-=-=-=-")
        print("\n")
        print("Sorry '" + guess.upper() + "' isn't in the word!") #Text - USE CODE(D)
        print("\n")
        print(display_word) #New function(C)
        print("\n")
        print("wrong guesses: ")
        print(guess.upper()) ### this needs to be a list - CREATE FUNCTION (B)
        print("\n")
        next_guess = input("Have another guess: ") # SEND TO NEW FUNCTION (A)
        print()
    """
    if bool(letter_index) == True:
        print("unlucky, try again")
        display_word[letter_index] = guess #updates the display_word (list)
    else:
        print("The letter " + guess + " was in the word!")
        display_word[letter_index] = guess #updates the display_word (list)
    #print(guess) #Testing: index of letters in word
    #print(answer) #testing: the word
    #print(display_word) #testing: the current display
   """ 

## Start game input   
def game_start_input():
    while True:
        game_start = input("To start: Enter 'E' for easy or 'H' for hard: ")

        if game_start.lower() == "h":
            print("lets go!")
            begin_game = load_game()
            return True
        elif game_start.lower() == "e":
            print("you choose easy game!")
        else:
            print("Try again my friend!")

## Displays game elements
def load_game():

    # DONE function that generates a word in 'magic_word'
    # DONE function that generates guess display word from magic word
    # DONE function that listens to the 'guess'
    # function that steps the index of 'graphic' if wrong
    # function that updates 'wrong_guesses' with wrong letters
    # DONE function that updates 'magic_word'
    
    random_word()

    magic_word,magic_word_list,magic_word_length = random_word()
    
    graphic = HANGMAN
    print(graphic[0])
    line_break = "\n"
    word_text = "Here's the word to guess:    "
    magic_word = magic_word #for testing
    print("TESTING this is the magic_word:  " + magic_word) #for testing
    #print(magic_word_list) #for testing (this is a list of the word)
    #print(magic_word_length) #for testing (this is how many characters)
    print(line_break + word_text + line_break)
    word = word_display(magic_word_length) #for testing (word displayed)
    print(word)
    print(line_break)
    wrong_guesses_text = "Wrong guesses: \n"
    wrong_guesses ="A B C"
    print(wrong_guesses_text + wrong_guesses + line_break)
    guess = input("Choose a letter:  ")
    print(line_break)
    user_guess(guess, magic_word_list, word)

"""
This functions starts the game
"""
game_start()
enter_name()
game_start_input()




