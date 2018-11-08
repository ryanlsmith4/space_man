import random

letters_guessed = []
correct_guesses = []
my_list = []
low_dash = []


def dictionary_list():
    '''
    This function reads the entire content of a file and puts
    them into a list then splits the dictionary with commas by the /n chars
    '''
    f = open('dictionary.txt', 'r')
    dict_list = f.readlines()
    f.close()
    dict_list = dict_list[0].split(' ')
    return dict_list
# END dictionary_list

def gen_secret_word(list):
    '''
    This function takes in a sequence || (list) and return one element
    in it Using random.choice which becomes the secret_word
    '''
    secret_word = random.choice(list)
    return secret_word
# END gen_secret_word




def guess_letter():
    '''
    Function to take in user input and verify its valid to be
    returned in lowercase form
    '''
    letter = input("Guess a Letter: ")
    if letter == None:
        print("can't be null")

    elif len(letter) > 1:
        print("only one letter please")

    letter = letter.lower()
    return letter
#END guess letter()



def check_matching(secret_word, guess):
    '''
    function takes in the user guess and the
    secret word and returns true or
    false whether the guess matched
    '''
    match = True
    if guess in secret_word:
        correct_guesses.append(guess)
    else:
        match = False
        letters_guessed.append(guess)
        print("not in secret word")
    return match
#END check_matching


def print_game():
    '''
    Function that draws the game board the length of the secret_word
    '''
    load_word = "Secret Word: "
    for i in low_dash:
        load_word = load_word + i + " "
    print(load_word)
#END print_game()



def replace_dash(guess, secret_word):
    '''Function that replaces the dashes with the corresponding
        letters'''
    secret_word = list(secret_word)
    for i in range(len(secret_word)) :
        if guess == secret_word[i]:
            low_dash[i] = guess

#END replace_dash

def gen_dash_word() :
    '''
    Function that turns secret_word into dashes
    '''
    for i in secret_word:
        low_dash.append("_")

    # print(low_dash)

# Game loop (Work in progress)
def play_space():
    turns = 0
    print(secret_word)
    while turns < 7:
        print_game()
        guess = guess_letter()
        replace_dash(guess, secret_word)
        if check_matching(secret_word, guess) == False:
            turns += 1
        elif "".join(correct_guesses) == secret_word:
            print("You WIN")
            return
        print(turns)
#END play space

#assign secret_word using gen_secret_word()
secret_word = gen_secret_word(dictionary_list())
gen_dash_word()
# print(secret_word)

play_space()

#shout out to Alex Bogert for unblocking me on this project
