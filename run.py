# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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

for x in range(len(HANGMAN)):
    print(HANGMAN[x])

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
MMM      MMM  AAA    AAA   NNN.     NNNN    |     -   -  
                                            |
#==#==#==#==  CREATED BY ANDREW CARGILL  #==#==#==#==#

\n'''
    print(game_start_graphic)


def enter_name():
    print("THE RULES ARE SIMPLE... YOU JUST NEED TO GUESS THE WORD!")
    print("BUT, IF YOU MAKE 5 WRONG GUESSES THEN POOR HARRY HANGS :")
    print("GOOD LUCK.\n")

    
def game_start_input():
    while True:
        game_start = input("Enter 'E' for easy or 'H' for hard: ")
        if game_start == "h":
            print("lets go!")
            begin_game = load_game(x)
            return True
        elif game_start =="e":
            print("you choose easy game!")
        else:
            print("Try again idiot!")


def load_game(x):
    begin_game = ".......The hard Game will now load!"
    print(begin_game)


game_start()
enter_name()
game_start_input()




