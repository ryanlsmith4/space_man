import random

turns = 0
letters_guessed = []
correct_guesses = []

guess = ''
def dictionary_list():
    '''
    This function reads the entire content of a file and puts them into a list
    Then splits the dictionary with commas by the /n chars
    '''
    f = open('dictionary.txt', 'r')
    dict_list = f.readlines()
    f.close()
    dict_list = dict_list[0].split(' ')
    return dict_list
# END dictionary_list


def gen_secret_word(list):
    '''
    This function takes in a sequence || (list) and return one element in it
    Using random.choice which becomes the secret_word
    '''
    secret_word = random.choice(list)
    # print(secret_word)
    return secret_word
# END gen_secret_word
secret_word = gen_secret_word(dictionary_list())

def letter_guess():
    letter = input("Guess a Letter: ")
    # print(letter)
    guess = letter
    return letter

guess = letter_guess()


def is_word_guessed(secret_word, correct_guesses):
    secret_word = secret_word
    correct_guesses = correct_guesses
    if correct_guesses == secret_word:
        print('congrats you won!')

def check_matching(secret_word, guess):
    if guess in secret_word:
        correct_guesses.append(guess)
        return correct_guesses




#TEST function
def test():
    # dictionary_list()
    gen_secret_word(dictionary_list())
    print(guess)
    letter_guess()
    check_matching(secret_word, guess)
    is_word_guessed(secret_word, correct_guesses)
    print(correct_guesses)
    print(''.join(letters_guessed))
    print(turns)

#END TEST functional
while True:
    test()
