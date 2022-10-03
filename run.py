import random

HANGMAN = ['''
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#=
     @                                 _ _ _ _            $          \ | / 
    @@@                               |                  €€€        -  @  -
   @@@@@                              |                 |###|        / | \ 
    ||         =========              |                 | x |
    ||        ===========             |                 |   |__________
    ||        | x  _  x |             |                 | _  ##########|
    ||        |   | |   |             |                 || |           |
                                   #==#==#              
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#=    
    
    ''', '''
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



game_start_graphic = '''

-------------------- W E L C O M E   T O   H A R R Y ' S --------------------

HH    HH     AAA      NNn   NN     GGGGG   MMm  mMM     AAA      NNn   NN
HH    HH    A    A    NN n  NN   GG        MM mm MM    A    A    NN n  NN   
HHHHHHHH   AAAAAAAA   NN  n NN  GG   GGG   MM    MM   AAAAAAAA   NN  n NN       
HH    HH   AA    AA   NN   nNN   GG   GG   MM    MM   AA    AA   NN   nNN   
HH    HH   AA    AA   NN    NN    GGGGG    MM    MM   AA    AA   NN    NN

#==#==#==#==#==#==#==#==  CREATED BY ANDREW CARGILL  #==#==#==#==#==#==#==#==#

\n'''

## Rules of the game
def rules():
    print("THE RULES ARE SIMPLE... YOU JUST NEED TO GUESS THE WORD")
    print("BUT, IF YOU MAKE 6 WRONG GUESSES THEN IT'S THE END FOR POOR HARRY!")
    print("GOOD LUCK.\n")



# this is where all words are stored  
animal_words = ["bull", "cow", "duck", "mouse", "cat", "dog", "horse", "goat", "tiger"]

color_words = ["blue", "red", "purple", "grey", "pink", "orange", "black", "white"]

animal_game = True

#A blank list that will show any correct letters
guess_list = ["- ", "- ", "- ", "- ", "- ", "- ", "- ", "- "]

#default_list for new games
default_list = ["- ", "- ", "- ", "- ", "- ", "- ", "- ", "- "]

#Word as displayed to user
game_word_display = []

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
    magic_word = random.choice(game_words_selector())
    answer = magic_word.upper()
    for letter in answer:
        answer_word_list.append(letter)
        answer_length = len(answer_word_list)
    create_game_word_display(answer_length)

def game_words_selector():
    if animal_game == True:
        return animal_words
    else:
        return color_words

        
#Creates a list of the word without letters
def create_game_word_display(x):
    global game_word_display
    game_start_graphic = []
    for i in range(x):
        game_word_display.append("- ")

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
        print("That was too easy, would you like to play again?")
        play_again()
    elif hangman_int == 6:
        print("R.I.P Harry!")
        print("Maybe next time!... Would you like to play again?")
        play_again()
    else: 
        y = input("Guess a letter: ")
        check_guess(y)

def play_again():
    x = input("press 'Y' for yes or 'Return' to head home: ")
    if x.lower() == "y":
        choose_game()
    else:
        welcome_screen()

#checks guess for previous use, length & numeric
def check_guess(y):
    global letter_guess
    if y.upper() in used_letters:
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
    
def welcome_screen():
    print(game_start_graphic)
    rules()
    y = input("Press 'return' start\n")
    print("\n")
    print("Ok, so you've read the rules...")
    print("Now which kind of word do you want to guess?")
    print("\n")
    choose_game()

def choose_game():
    enter = input("Type 'A' for Animals or 'C' for Colors: ")
    check_game_input(enter)

def check_game_input(x):
    global animal_game
    if x.lower() == "a":
        animal_game = True
        load_game()
    elif x.lower() == "c":
        animal_game = False
        load_game()
    else:
        print("Try again my friend!\n")
        choose_game()

# Resets games global variables
def load_game():
    global hangman_int
    global answer_word_list
    global bad_guesses
    global used_letters
    global game_word_display
    hangman_int = 0 
    game_word_display = []
    answer_word_list =[]
    bad_guesses =[]
    used_letters=[]
    
    #generates new word a populates relevant variables
    random_word()  

    #First Display
    print("TESTING this is the magic_word:  " + answer) #for testing

    print(HANGMAN[0])
    line_break = "\n"
    word_text = "Here's the word to guess:    "
    print(game_word_display)
    print(line_break)

    print(line_break)
    print("-----------------------")
    wrong_guesses_text = "Wrong guesses: \n"
    print(bad_guesses)
    print(line_break)
    enter_next_letter()

"""
This functions starts the game
"""


welcome_screen()




