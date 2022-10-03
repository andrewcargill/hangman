import random

HANGMAN = ['''
        _ _ _ _
       |       |
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



game_start_graphic = '''

-------------------- W E L C O M E   T O   H A R R Y ' S --------------------

 HH    HH     AAAA     NNn   NN    GGGGG    MMm  mMM     AAAA     NNn   NN
 HH    HH    A    A    NN n  NN   GG        MM mm MM    A    A    NN n  NN   
 HHHHHHHH   AAAAAAAA   NN  n NN  GG   GGG   MM    MM   AAAAAAAA   NN  n NN       
 HH    HH   AA    AA   NN   nNN   GG   GG   MM    MM   AA    AA   NN   nNN   
 HH    HH   AA    AA   NN    NN    GGGGG    MM    MM   AA    AA   NN    NN

#==#==#==#==#==#==#==#==  CREATED BY ANDREW CARGILL  #==#==#==#==#==#==#==#==#

\n'''

first_guess_graphic = '''
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#=
                                                                     \ | /   
    @@                                 _ _ _ _            $         -  @  - 
   @@@@                               |                  €€€         / | \ 
  @@@@@@                              |                 |###|        
    ||         =========              |                 | x |
    ||        ===========             |                 |   |__________
    ||        | x  _  x |             |                 | _  ##########|
    ||        |   | |   |             |                 || |           |
                                   #==#==#              
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#=    
    '''

## Rules of the game
def rules():
    print(" THE RULES ARE SIMPLE... YOU JUST NEED TO GUESS THE WORD")
    print(" BUT, IF YOU MAKE 6 WRONG GUESSES THEN IT'S THE END FOR POOR HARRY!")
    print(" GOOD LUCK.\n")



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
#if it is - updates game_word_display
#if not - updates hangman index & adds to bad guesses
def check_true():
    if letter_guess in answer_word_list:
        update_game_word_display()
        game_loop_display()
    #    print(type_for_game_header())
    #    print(HANGMAN[hangman_int]) 
    #    print("\n")
    #    print(" WORD TO GUESS:  " + list_to_string(game_word_display))
    #    print("\n")
    #    print(" WRONG GUESSES: " + list_to_string(bad_guesses))
    #    print("\n") 
        print(" Well done! '" + letter_guess + "' was in the word.")
        enter_next_letter() 
    else:
        hangman_stepper() 
        add_to_bad_guesses()
        game_loop_display()
    #    print(HANGMAN[hangman_int]) 
         
    #    print(game_word_display) 
        print(" Unlucky... '" + letter_guess + "' wasn't in the word.")
        enter_next_letter() 

def game_loop_display():
    print(type_for_game_header())
    print(HANGMAN[hangman_int]) 
    print("\n")
    print(" WORD TO GUESS:  " + list_to_string(game_word_display))
    print("\n")
    print(" WRONG GUESSES: " + list_to_string(bad_guesses))
    print("\n") 


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
        print(" YOU SAVED HARRY! The answer was " + answer + "!!!")
        print(" That was too easy, would you like to play again?")
        play_again()
    elif hangman_int == 6:
        print(" R.I.P Harry!")
        print(" Maybe next time!... Would you like to play again?")
        play_again()
    else: 
        y = input(" Guess a letter: ")
        check_guess(y)

def play_again():
    x = input(" press 'Y' for yes or 'Return' to head home: ")
    if x.lower() == "y":
        choose_game()
    else:
        welcome_screen()

#checks guess for previous use, length & numeric
#Adds to used_letters if new letter is guessed
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
#Returns as a string
def update_game_word_display():
    global game_word_display
    letter_index = answer_word_list.index(letter_guess) #Finds index - 
    game_word_display[letter_index] = letter_guess.upper() # updates display_word - 
    

#Increases index of hangman variable
def hangman_stepper():
    global hangman_int
    hangman_int = hangman_int+1
    
def welcome_screen():
    print(game_start_graphic)
    rules()
    y = input(" Press 'return' start ")
    print("\n")
    print(" Ok, so you've read the rules...")
    print(" Now which type of word do you want to try and guess?")
    print("\n")
    choose_game()

def choose_game():
    enter = input(" Type 'A' for Animals or 'C' for Colours: ")
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
        print(" Try again my friend!\n")
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

    ##USER SCREEN

    line_break = "\n"
    print(first_guess_graphic)
    print(type_for_game_header())
    print(line_break)
    print(" WORD TO GUESS: " + list_to_string(game_word_display))
    print(line_break)
    print(" Let's go!... Nervous? It's time to choose the first letter.")
    enter_next_letter()

#prints type of word to guess
def type_for_game_header():
    if animal_game == True:
        return(" TYPE OF WORD: A N I M A L")
    else:
        return(" TYPE OF WORD: C O L O U R")

#Turns a list into a string
def list_to_string(list):
    list_to_print = ""
    for x in list:
        list_to_print += " " + x
    return list_to_print

"""
This functions starts the game
"""
welcome_screen()




