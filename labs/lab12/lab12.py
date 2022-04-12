"""
Name: <Olivia Bianco>
<Lab12>.py

Problem: <Working with lists and decision structures>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

from random import randint


def find_and_remove_first(my_list, val):
    i = 0
    while i < len(my_list):
        if my_list[i] == val:
            my_list.insert(i, 'Olivia')
            my_list.pop(i + 1)

    i += 1


def good_input():
    user = 0
    while user < 1 or user > 10:
        user = eval(input("Guess a number: "))
        if user > 10:
            print("Too high.")
        elif user < 1:
            print("Too low.")


def num_digits():
    user_input = eval(input("enter a positive integer, or enter a negative integer or zero to quit: "))
    while user_input > 1:
        count = 0
        each_place = user_input
        while each_place != 0:
            count += 1
            each_place = each_place // 10
        print(count)
        user_input = eval(input("enter a positive integer, or enter a negative integer or zero to quit: "))


def hi_lo_game():
    user_input = eval(input("Guess a number: "))
    acc = 1
    num = randint(1, 100)
    while user_input != num and acc != 7:
        acc += 1
        if user_input < num:
            print("too low.")
        else:
            print("too high.")
        user_input = eval(input("Guess a number: "))
        if user_input == num:
            print("You won in " + str(acc) + "guesses!")
        if acc == 7:
            print("You lost. The secret number was " + str(num))

