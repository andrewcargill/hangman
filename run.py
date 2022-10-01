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
word_bank = ["bee", "ed", "teddy", "f3efd", "gggg", "tterer", "fffff", "1", "2222222"]

#A blank list that will show any correct letters
guess_list = ["- ", "- ", "- ", "- ", "- ", "- ", "- "]

#Generates a random word and breaks down into a list of letters
def random_word():
    magic_word = random.choice(word_bank)
    magic_word_list = []
    for letter in magic_word:
        magic_word_list.append(letter)
        magic_word_length = len(magic_word_list)
        

    return magic_word,magic_word_list,magic_word_length


#Guess list references the magic word list

def word_display(x):
    n = len(guess_list)
    for i in range(0, n - x):
        guess_list.pop()
    return guess_list
 

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
    """
    1. #### A function that generates a word in 'magic_word'
    1a.#### function that generates guess display word from magic word
    2. A function that listens to the 'guess'
    3. A function that steps the index of 'graphic' if wrong
    4. A function that updates 'wrong_guesses' with wrong letters
    5. A function that updates 'magic_word'
    """
    random_word()

    magic_word,magic_word_list,magic_word_length = random_word()
    
    graphic = HANGMAN
    print(graphic[0])
    line_break = "\n"
    word_text = "Here's the word to guess:    "
    magic_word = magic_word #for testing
    print(magic_word_list) #for testing
    print(magic_word_length) #for testing
    print(word_display(magic_word_length))
    print(line_break + word_text + magic_word + line_break)
    wrong_guesses_text = "Wrong guesses: \n"
    wrong_guesses ="A B C"
    print(wrong_guesses_text + wrong_guesses + line_break)
    guess = input("Choose a letter:  ")

"""
This functions starts the game
"""
game_start()
enter_name()
game_start_input()




