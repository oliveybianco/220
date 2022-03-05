"""
Name: <Olivia Bianco>
<HW6>.py

Problem: <Working with strings.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

import math


def cash_converter():
    num = eval(input("Enter an integer: "))
    print("That is: ${:.2f}".format(num))


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    cipher = ""
    for word in range(len(message)):
        character = message[word]
        cipher += chr(ord(character) + key)

    print(cipher)


def sphere_area(radius):
    surface_area = 4 * (math.pi * radius ** 2)
    return surface_area


def sphere_volume(radius):
    volume = 4/3 * (math.pi * radius ** 3)
    return volume


def sum_n(number):
    summed = (number * (number+1)) / 2
    return summed


def sum_n_cubes(number):
    cube_sum = ((number * (number+1)) / 2) ** 2
    return cube_sum


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    cipher = ""

    for i in range(len(message)):
        character = ord(message[i]) - 65
        shift = ord(key[i % len(key)]) - 65
        add = character + shift
        check = add % 58
        convert = check + 65
        revert = chr(convert)
        cipher += revert
    print(cipher)




if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
