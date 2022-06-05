import random

MENU_TEXT = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'

GUESS_TEXT = 'Guess the word '
WIN_FAIL_TEXT = {True: 'You guessed the word {}!\nYou survived!',
                 False: 'You lost!'
                 }

SCOREBOARD_TEXT = 'You won: {:d} times.\nYou lost: {:d} times.'

GREET_TEXT = 'H A N G M A N'
END_TEXT = 'Thanks for playing!'
WRONG_LETTER_TEXT = "That letter doesn't appear in the word."
NON_LETTER_TEXT = 'Please, enter a lowercase letter from the English alphabet.'
WRONG_NUM_LETTERS = 'Please, input a single letter.'
NO_IMPROVEMENTS_TEXT = 'No improvements.'
ALREADY_TRIED_TEXT = "You've already guessed this letter"

POSSIBLE_GOAL_WORDS = ('python', 'java', 'swift', 'javascript')

NUM_ATTEMPTS = 8


def init_goal_word():
    return random.choice(POSSIBLE_GOAL_WORDS)


def test_guess(word, goal_word):
    result = word == goal_word
    return result


def ask_guess(guess_text, goal_word):
    masked_word = goal_word[:3] + '-' * (len(goal_word) - 3) + ':'
    print(guess_text + masked_word)
    return input()


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += 1


def test_input_len(string):
    if not len(string) == 1:
        print(WRONG_NUM_LETTERS)
        return False
    else:
        return True


def test_input_correct_letter(string):
    if string < 'a' or string > 'z':
        print(NON_LETTER_TEXT)
        return False
    else:
        return True


def test_input_unique(string, guess_history):
    if string in guess_history:
        print(ALREADY_TRIED_TEXT)
        return False
    else:
        return True


def validate_input(string, guess_history):
    if not test_input_len(string):
        return False
    elif not test_input_correct_letter(string):
        return False
    elif not test_input_unique(string, guess_history=guess_history):
        return False
    else:
        return True


def ask_letter(guess_word, guess_history, goal_word):
    print('Input a letter:')
    inp = input()
    if not validate_input(inp, guess_history=guess_history):
        success = 0
    else:
        guess_history += inp

        if inp in goal_word:
            guess_word = list(guess_word)
            indxs = list(find_all(goal_word, inp))
            for indx in indxs:
                guess_word[indx] = inp
            guess_word = ''.join(guess_word)
            success = 1
        else:
            print(WRONG_LETTER_TEXT)
            success = -1
    return success, guess_word, guess_history


def play():
    num_attempts = NUM_ATTEMPTS
    goal_word = init_goal_word()
    guess_word = '-' * len(goal_word)
    guess_history = ''
    win = False

    while num_attempts > 0:
        print(guess_word)
        result, guess_word, guess_history = ask_letter(guess_word=guess_word,
                                                       guess_history=guess_history,
                                                       goal_word=goal_word)
        if result < 0:
            num_attempts -= 1
        if test_guess(word=guess_word, goal_word=goal_word):
            win = True
            break

    print(WIN_FAIL_TEXT[win].format(goal_word))
    return win


if __name__ == '__main__':
    num_wins = 0
    num_losts = 0

    print(GREET_TEXT)

    while True:
        print(MENU_TEXT)
        print()

        req = input()
        if req == 'play':
            if play():
                num_wins += 1
            else:
                num_losts += 1
        elif req == 'results':
            print(SCOREBOARD_TEXT.format(num_wins,num_losts))
        elif req == 'exit':
            break
