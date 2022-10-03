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
 ——————  W E L C O M E   T O   H A R R Y ' S  —————————

 HHH      HHH      AAA      NNN       NNN      GGGGG
 HHH      HHH    AAA AAA    NNN N     NNN    GGG    GGG
 HHH      HHH   AAA   AAA   NNN  N    NNN  GGG
 HHHHHHHHHHHH  AAAAAAAAAAA  NNN   N   NNN  GGG    
 HHH      HHH  AAA     AAA  NNN    N  NNN  GGG    GGGGG
 HHH      HHH  AAA     AAA  NNN     N NNN   GGG     GGG
 HHH      HHH  AAA     AAA  NNN      NNNN    GGGGGGG
                                              _ _ _ _
 MMM      MMM      AAA      NNN       NNN    |       |
 MMMM    MMMM    AAA AAA    NNN N     NNN    |       0
 MMM M  M MMM   AAA   AAA   NNN  N    NNN    |      /|\ 
 MMM  MM  MMM  AAAAAAAAAA   NNN   N   NNN    |       |  
 MMM      MMM  AAA    AAA   NNN    N  NNN    |      / \ 
 MMM      MMM  AAA    AAA   NNN     N NNN    |     -   -
 MMM      MMM  AAA    AAA   NNN      NNNN    | 
--------------  CODED BY ANDREW CARGILL  --------------                                             
'''


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

win_graphic ='''
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#=
                                                                     \ | /   
    @@                                 _ _ _ _            $         -  @  - 
   @@@@                               |                  €€€         / | \ 
  @@@@@@                              |    T H A N K S! |###|        
    ||         =========              |         0       | x |
    ||        ===========             |        \|/      |   |__________
    ||        | x  _  x |             |         |       | _  ##########|
    ||        |   | |   |             |        / \      || |           |
                                   #==#==#    -   -        
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#=    
    '''
lost_graphic = '''
                          _________________              $                    
                        //                 \            €€€        
                       //        | |        \          |###|        
                      //      ___| |___      \         | x |    
                     ||       ___   ___       ||       |   |__________     
                     ||          | |          ||       | _  ##########|     
       #######       ||          | |          ||       || |           |      
      ###########    ||          | |          ||
      #############  ||                       ||     
        #############||       R . I . P       || 
      ### ###########||       H A R R Y       ||        
    ############################___###_###_#############
'''
## Rules of the game
def rules():
    print(" THE RULES ARE SIMPLE... YOU JUST NEED TO GUESS THE WORD")
    print(" BUT, IF YOU MAKE 6 WRONG GUESSES THEN IT'S THE END FOR POOR HARRY!\n")



# this is where all words are stored  
animal_words = ["bull", "cow", "duck", "mouse", "cat", "dog", "horse", "goat", "tiger"]

color_words = ["blue", "red", "purple", "grey", "pink", "orange", "black", "white"]

#Used to select game questions
animal_game = True

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

#all used letters
used_letters =[]

#used in development of game
def code_checker():
    print("Game word display = " + list_to_string(game_word_display))
    print("Answer word list  " + list_to_string(answer_word_list))
    print("letter guess" + letter_guess)
    print("used letters" + list_to_string(used_letters))

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

#Selects words based on players choice
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
#if true: updates game word display with letter
#if false: updates hangman index & adds to bad guesses
def check_true():
    if letter_guess in answer_word_list:
        update_game_word_display()
        game_loop_display()
        print(" Well done! '" + letter_guess + "' was in the word.")
        enter_next_letter() 
    else:
        hangman_stepper() 
        add_to_bad_guesses()
        game_loop_display()
        print(" Unlucky... '" + letter_guess + "' wasn't in the word.")
        enter_next_letter() 

# Prints updated display after each guess
def game_loop_display():
    print(type_for_game_header())
    print(HANGMAN[hangman_int]) 
    print("\n")
    print(" WORD TO GUESS:  " + list_to_string(game_word_display))
    print("\n")
    print(" WRONG GUESSES: " + list_to_string(bad_guesses))
    print("\n") 

#Adds letter guessed to a list
def add_to_used_letters():
    global used_letters
    used_letters.append(letter_guess.upper())


#adds wrong guesses to a list
def add_to_bad_guesses():
    global bad_guesses
    bad_guesses.append(letter_guess.upper())

#checks for end of game
#asks user for next guess
def enter_next_letter():
    check = [x.upper() for x in answer_word_list]
    if check == game_word_display:
        print(win_graphic)
        print(" YOU SAVED HARRY! The answer was " + answer + "!!!")
        print(" Would you like to play again?")
        play_again()
    elif hangman_int == 6:
        print(lost_graphic)
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
        print(" Ooops... You've already used that letter!")
        enter_next_letter()
    elif len(y) > 1:
        print(" Slow down my friend... guess one letter at a time!")
        enter_next_letter()
    elif y.isnumeric() == True:
        print(" Hint: There's no numbers in the word!")
        enter_next_letter()
    else:
        letter_guess = y.upper()
        add_to_used_letters()
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
    print(" It's time to choose a type of word. Good Luck!! ")
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




