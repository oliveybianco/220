"""
Name: <Olivia Bianco>
<Lab12>.py

Problem: <Working with lists and files>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def read_data(file_name):
    i = 0
    my_list = []
    my_file = open(file_name, "r")
    line = my_file.read()
    words = line.split()
    while i < len(words):
        nums = eval(words[i])
        my_list.append(nums)
        i += 1
    my_file.close()
    return my_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val in values:
            return True
        else:
            return False

    i += 1

