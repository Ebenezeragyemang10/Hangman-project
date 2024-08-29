import random
hangman_words_list =["sakina", "jennifer", "oforiwaa", "janet", "sarah", "donkor", "adobea"," agnes", "maxwell", "ezekiel"]

#selecting random word
random_word = random.choice(hangman_words_list)


#game global variables
end_of_game= False



#function for creating dashes
def create_dashes(word):
    ''' takes a word from user and create list of dashes with same number
     as number of letters in the word '''
    dash_list = []
    for letter in word:
        dash_list.append("_")
    return dash_list

#function to check whether player guess is in the word 
def checkGuess(f_user_guess, f_random_word):
    ''' returns true or false based on whether user guess is in the word'''
    return f_user_guess in f_random_word
        
#function to replash dashes in dash list with what user guessed
def replace_dash_with_guess(f_user_guess, f_random_word):
    ''' a function to replash dashes in dash list with what user guessed'''
    for index, word in enumerate (f_random_word):
        if word == f_user_guess:
            # print(word, f_user_guess, index)
            dashed_list[index] = word

#function to check duplicate guess
def check_repeated_guess(f_user_guess):
    ''' function to check duplicate guess, thus make sure user doesnt guess a single letter multiple times'''
    return f_user_guess in dashed_list
          
def set_player_life(f_player_life):
    ''' a function that updates player life'''
    return len(f_player_life)



 ##=================== ui design ===============================#
print(random_word)
print("Welcome to the hangman game!, ready to guess:):😎")
dashed_list = create_dashes(random_word)
print("guess the letters in the word...........🤔🤔")

#set player life
player_life=set_player_life(f_player_life=random_word)
while not end_of_game:

    #take player guess
    player_guess= input("guess here \n >>> ")
    if checkGuess(f_user_guess=player_guess, f_random_word=random_word):
        if check_repeated_guess(f_user_guess=player_guess):
         print(f"{player_guess} is already guessed")

        replace_dash_with_guess(f_user_guess=player_guess, f_random_word=random_word)

    else:
        player_life -=1
        print(f"your life remaining is {player_life}")
        print("wrong guesss.....😢, guess again buddy")

    if player_life ==0:
        print("sorry you have lost the game ....... 🤦‍♂️🤦‍♂️🤦‍♂️")
        end_of_game=True
    # print(dashed_list)
    if "_" not in dashed_list:
        print("congratulations ❤, you have won the game")
        end_of_game=True

    print(dashed_list)
    print("guess again.......")

#======================= end of ui design====================================#    


