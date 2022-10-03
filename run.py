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
       |      /|
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
    print("BUT, IF YOU MAKE 6 WRONG GUESSES THEN IT'S THE END FOR HARRY!")
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
bad_guesses =[]

#list of good guesses
good_guesses = []

#all used letters
used_letters =[]


#Generates a random word and creates a list of word letters
def random_word():
    global answer_word_list
    global answer
    magic_word = random.choice(word_bank)
    answer = magic_word.upper()
    for letter in answer:
        answer_word_list.append(letter)
        answer_length = len(answer_word_list)
    print(answer_length)
    word_display(answer_length)
        


#Creates a list of the word without letters
# (DEV: build the list from 0)
def word_display(x):
    global game_word_display
    n = len(guess_list)
    for i in range(0, n - x):
        guess_list.pop()
    game_word_display = guess_list

#checks if guessed letter is in the word
#updates used_letters variable
def check_true():
    if letter_guess in answer_word_list:
        print(HANGMAN[hangman_int])
        update_game_word_display() #this prints the user_word_display
        enter_next_letter()

    else:
        hangman_stepper()
        print(HANGMAN[hangman_int])
        add_to_bad_guesses()
        print(game_word_display)
        enter_next_letter()

#Adds a correct letter to good guesses list
def add_to_used_letters():
    global used_letters
    used_letters.append(letter_guess.upper())
    print(used_letters)#for testing

def add_to_bad_guesses():
    global bad_guesses
    bad_guesses.append(letter_guess.upper())
    print("Bad guesses")
    print(bad_guesses)#for testing


#checks for end of game (word is fully guessed)
#asks for next letter
def enter_next_letter():
    check = [x.upper() for x in answer_word_list]
    if check == game_word_display:
        print("Well done!! Harry lives! The answer was " + answer + "!!!")
    elif hangman_int == 6:
        print("R.I.P Harry!")
    else: 
        y = input("Guess a letter: ")
        check_guess(y)

#checks guess for previous use, length & numeric
def check_guess(y):
    global letter_guess
    if y in used_letters:
        print("Ooops... You've already used that letter!")
        enter_next_letter()
    elif len(y) > 1:
        print("Slow down my friend... guess one letter at a time!")
        enter_next_letter()
    elif y.isnumeric() == True:
        print("Hint: There's no numbers in the word!")
        enter_next_letter()
    else:
        letter_guess = y.upper()
        add_to_used_letters()#prints for testing
        print(letter_guess)#for testing
        check_true()


#Adds guessed letter to user_word_display
def update_game_word_display():
    global game_word_display
    letter_index = answer_word_list.index(letter_guess) #Finds index - USE CODE
    game_word_display[letter_index] = letter_guess.upper() # updates display_word - USE CODE(C)
    print(game_word_display)

#Increases index of hangman variable
def hangman_stepper():
    global hangman_int
    hangman_int = hangman_int+1
    
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
    random_word()  
    graphic = HANGMAN

    ##PRINTS FIRST GRAPHIC
    print(graphic[0])

    ##UPDATES GLOBAL 'ANSWER'
    line_break = "\n"
    word_text = "Here's the word to guess:    "
    #global answer
    #answer = magic_word.upper() #for testing
    print("TESTING this is the magic_word:  " + answer) #for testing
    print(line_break + word_text + line_break)
    print(answer_word_list)#for testing
    print(game_word_display)
    print(line_break)
    wrong_guesses_text = "Wrong guesses: \n"
    wrong_guesses ="A B C"
    print(wrong_guesses_text + wrong_guesses + line_break)
    enter_next_letter()

"""
This functions starts the game
"""
game_start()
enter_name()
game_start_input()




