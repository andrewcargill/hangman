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

#Word as displayed to user
game_word_display =[]

#answer in list form
answer_word_list = []

#displays the current letter guesses
letter_guess = ""

#The word currently being used
answer =""

#index for hangman image
hangman_int = 0

#list of bad guesses
bad_guesses =[2,4,5]

#list of good guesses
good_guesses = ""


#Generates a random word and creates a list of word letters
def random_word():
    magic_word = random.choice(word_bank)
    magic_word_list =[]
    print(magic_word_list)
    for letter in magic_word:
        magic_word_list.append(letter)
        magic_word_length = len(magic_word_list)
        

    return magic_word,magic_word_list,magic_word_length


#Creates a list of the word without letters
# (DEV: build the list from 0)
def word_display(x):
    n = len(guess_list)
    for i in range(0, n - x):
        guess_list.pop()
    return guess_list

"""

"""

#checks if players guess is correct
#populates answer_word_list with correct word
#over-writes letter_guess with current guess
def user_guess(guess, y):
    global answer_word_list
    global letter_guess
    answer_word_list = y
    guess = guess.lower()  #Players guess (letter)
    letter_guess = guess 
    check_true()

    #print(letter_guess) #for testing
    #print(game_word_display) #for testing
    #print(answer_word_list) #for testing
    #print(answer) #for testing
    #print(hangman_int) #for testing
    #print(bad_guesses) #for testing
    #print(good_guesses) #for testing

#checks if guessed letter is in the word
# NEEDS to check if single character! & Used before?
def check_true():
    global letter_guess
    global game_word_display
    if letter_guess in answer_word_list:
        print(HANGMAN[hangman_int])
        update_game_word_display()
    else:
        print("no")
        bad_guesses()
        hangman_stepper()
        print(HANGMAN[hangman_int])


#Adds guessed letter to user_word_display
#Adds guessed letter to good_guesses
def update_game_word_display():
    global game_word_display
    global good_guesses
    letter_index = answer_word_list.index(letter_guess) #Finds index - USE CODE
    game_word_display[letter_index] = letter_guess.upper() # updates display_word - USE CODE(C)
    good_guesses = " " + letter_guess.upper() #FIX must add too - not over-write
    print(game_word_display)
    print(good_guesses) #for testing

#Adds the letter in the bad guesses variable
def bad_guesses():
    global bad_guesses
    bad_guesses = " " + letter_guess.upper() #FIX must add too - not over-write
    print("its a bad guess" + bad_guesses)

#Increases index of hangman variable
def hangman_stepper():
    global hangman_int
    hangman_int = hangman_int+1
    print(hangman_int)
    

"""    
    
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(HANGMAN[0])  #Needs to take previous Hangman and return same - NEW FUNCTION(E)
        print("-=-=        =-=-=-=-=-=-=-")
        print("\n")
        print("Yes! '" + guess.upper()+ "' was a great guess!") # Text - USE CODE(D)
        letter_index = answer.index(guess) #Finds index - USE CODE
        WORD_LIST[letter_index] = guess.upper() # updates display_word - USE CODE(C)
        print("\n")
        print(WORD_LIST)
        print("\n")
        print("wrong guesses: ") ### Wrong guess - CREATE FUNCTION TO MANAGE & RETURN(B)
        print("\n")
        print(WORD_LIST)
        next_guess = input("...Give me another letter to try!: ") #SEND TO NEW FUNCTION(A)
        
    else:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(HANGMAN[1]) # needs to take pervious hangman and add 1 - CREATE FUNCTION(E)
        print("-=-=        =-=-=-=-=-=-=-")
        print("\n")
        print("Sorry '" + guess.upper() + "' isn't in the word!") #Text - USE CODE(D)
        print("\n")
        print(WORD_LIST) #New function(C)
        print("\n")
        print("wrong guesses: ")
        print(guess.upper()) ### this needs to be a list - CREATE FUNCTION (B)
        print("\n")
        print(WORD_LIST)
        next_guess = input("Have another guess: ") # SEND TO NEW FUNCTION (A)
 """

# Start game input   
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
    global answer
    graphic = HANGMAN
    print(graphic[0])
    line_break = "\n"
    word_text = "Here's the word to guess:    "
    answer = magic_word #for testing
    print("TESTING this is the magic_word:  " + answer) #for testing
    #print(magic_word_list) #for testing (this is a list of the word)
    #print(magic_word_length) #for testing (this is how many characters)
    print(line_break + word_text + line_break)
    global game_word_display
    game_word_display = word_display(magic_word_length) #for testing (word displayed)
    print(game_word_display)
    print(line_break)
    wrong_guesses_text = "Wrong guesses: \n"
    wrong_guesses ="A B C"
    print(wrong_guesses_text + wrong_guesses + line_break)
    guess = input("Choose a letter:  ")
    print(line_break)
    user_guess(guess, magic_word_list)

"""
This functions starts the game
"""
game_start()
enter_name()
game_start_input()




