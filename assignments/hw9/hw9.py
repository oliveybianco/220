"""
Name: <Olivia Bianco>
<HW9>.py

Problem: <Creating a hangman game.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work. Using graphics.>
"""

import random
from graphics import GraphWin, Text, Line, Point, Entry, Circle


def get_words(file_name):
    my_file = open(file_name, "r")
    words = []
    lines = my_file.readlines()
    for line in lines:
        words.append(line)
    return words


def get_random_word(words):
    index = random.randint(0, len(words)-1)
    gotten_word = words[index]
    secret_word = gotten_word.rstrip()
    return secret_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True

    return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True

    return False


def make_hidden_secret(secret_word, guesses):
    empty = [] * len(secret_word)
    for _ in range(len(secret_word)):
        empty.append('_')
    my_list = []
    my_list[:] = secret_word
    for letter in range(len(secret_word)):
        for j in range(len(guesses)):
            if guesses[j] == my_list[letter]:
                empty[letter] = guesses[j] + ''
    return ' '.join(empty)


def won(guessed):
    for guess in guessed:
        if guess == "_":
            return False
    return True


def play_graphics(secret_word):
    win = GraphWin("HangMan", 700, 700)
    win.setBackground("white")
    base = Line(Point(200, 500), Point(500, 500))  # gallows
    pole = Line(Point(350, 200), Point(350, 500))
    top_line = Line(Point(275, 200), Point(350, 200))
    hanging = Line(Point(275, 200), Point(275, 300))
    base.draw(win)
    pole.draw(win)
    top_line.draw(win)
    hanging.draw(win)
    user_input = Entry(Point(350, 600), 10)
    user_input.draw(win)
    input_text = Text(Point(270, 600), "Enter a letter: ")
    input_text.draw(win)
    blanks_display = Text(Point(350, 550), " _ " * len(secret_word))
    blanks_display.draw(win)

    head = Circle(Point(275, 325), 25)  # body parts to be used later
    body = Line(Point(275, 350), Point(275, 400))
    left_arm = Line(Point(275, 375), Point(200, 350))
    right_arm = Line(Point(275, 375), Point(350, 350))
    left_leg = Line(Point(275, 400), Point(250, 450))
    right_leg = Line(Point(275, 400), Point(300, 450))

    guesses_left = 6
    guessed_already = []

    while guesses_left >= 0 and not guessed_already == secret_word:  # loop until won
        win.getKey()
        letter = user_input.getText()
        guessed_already.append(letter)
        guessed_letters = Text(Point(400, 325), guessed_already)
        guessed_letters.setSize(25)
        guessed_letters.draw(win)  # display the list of guessed letters to user
        input_text.setText("")
        if letter_in_secret_word(letter, secret_word):
            guessed_correct = make_hidden_secret(secret_word, letter)
            blanks_display.undraw()
        else:
            guesses_left -= 1
        if guesses_left == 5:
            head.draw(win)
        elif guesses_left == 4:
            body.draw(win)
        elif guesses_left == 3:
            left_arm.draw(win)
        elif guesses_left == 2:
            right_arm.draw(win)
        elif guesses_left == 1:
            left_leg.draw(win)
        elif guesses_left == 0:
            right_leg.draw(win)

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guessed_already = []
    guesses_left = 6
    guessed_correct = make_hidden_secret(secret_word, guessed_already)
    while guesses_left >= 0 and not guessed_correct == secret_word:
        print("already guessed:", guessed_already)
        print("guesses remaining:", guesses_left)
        print(guessed_correct)
        user_guess = input("guess a letter: ")
        guessed_already.append(user_guess)
        if letter_in_secret_word(user_guess, secret_word):
            guessed_correct = make_hidden_secret(secret_word, guessed_already)
        else:
            guesses_left -= 1
        if guessed_correct.split(" ") == list(secret_word):
            print("winner!\n" + guessed_correct)
            break
        elif guesses_left == 0:
            print("sorry, you did not guess the word.")
            print("the secret word was " + secret_word)
        else:
            print()


if __name__ == '__main__':
    pass
