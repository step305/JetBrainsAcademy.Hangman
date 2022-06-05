import random

GUESS_TEXT = 'Guess the word '
WIN_FAIL_TEXT = {True: 'You guessed the word!\nYou survived!',
                 False: 'You lost!'
                 }

GREET_TEXT = 'H A N G M A N'
END_TEXT = 'Thanks for playing!'
WRONG_LETTER_TEXT = "That letter doesn't appear in the word."
NO_IMPROVEMENTS_TEXT = 'No improvements.'

POSSIBLE_GOAL_WORDS = ('python', 'java', 'swift', 'javascript')

GOAL_WORD = 'python'
GUESS_WORD = ''
GUESS_HISTORY = ''

NUM_ATTEMPTS = 8


def init_goal_word():
    return random.choice(POSSIBLE_GOAL_WORDS)


def test_guess(word):
    result = word == GOAL_WORD
    return result


def ask_guess():
    masked_word = GOAL_WORD[:3] + '-' * (len(GOAL_WORD) - 3) + ':'
    print(GUESS_TEXT + masked_word)
    return input()


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1


def ask_letter():
    guess_word = GUESS_WORD
    guess_history = GUESS_HISTORY
    success = False
    print('Input a letter:')
    inp = input()[0]
    if inp in GOAL_WORD:
        if inp in guess_history:
            print(NO_IMPROVEMENTS_TEXT)
        else:
            guess_word = list(guess_word)
            guess_history += inp
            indxs = list(find_all(GOAL_WORD, inp))
            for indx in indxs:
                guess_word[indx] = inp
            guess_word = ''.join(guess_word)
            success = True
    else:
        print(WRONG_LETTER_TEXT)
    return success, guess_word, guess_history


if __name__ == '__main__':
    win = False
    GOAL_WORD = init_goal_word()
    GUESS_WORD = '-' * len(GOAL_WORD)

    print(GREET_TEXT)
    print()

    # guess = ask_guess()
    # test_guess(guess)
    while NUM_ATTEMPTS > 0:
        print(GUESS_WORD)
        result, GUESS_WORD, GUESS_HISTORY = ask_letter()
        if not result:
            NUM_ATTEMPTS -= 1
        if test_guess(GUESS_WORD):
            win = True
            break

    print(WIN_FAIL_TEXT[win])
