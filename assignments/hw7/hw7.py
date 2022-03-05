"""
Name: <Olivia Bianco>
<Hw7>.py

Problem: <Reading and writing to text files and working with functions.>
2
Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    my_file = open(in_file_name, "r")
    new_file = open(out_file_name, "w")
    i = 0
    for line in my_file:
        words = line.split()
        for word in words:
            i = i + 1
            print(str(i) + " " + word, file=new_file)

    my_file.close()
    new_file.close()


def hourly_wages(in_file_name, out_file_name):
    my_file = open(in_file_name, "r")
    new_file = open(out_file_name, "w")
    for line in my_file:
        words = line.split(" ")
        wage = float(words[2])
        bonus = 1.65
        wage = wage + bonus
        hours = float(words[3])
        total = hours * wage
        print(("{}{}{}{}{:.2f}".format(words[0], " ", words[1], " ", total)), file=new_file)

    my_file.close()
    new_file.close()


def calc_check_sum(isbn):
    new_isbn = isbn.replace("-", "")
    result = 0
    for i in range(10):
        pos = new_isbn[::-1]
        index = eval(pos[i])
        result += index * (i + 1)
    return result


def send_message(file_name, friend_name):
    in_file = open(file_name, "r")
    file_read = in_file.readlines()
    out_file = open(friend_name + ".txt", "w")
    for line in file_read:
        first = line.split()
        for word in first:
            word += word
        print(line.replace("\n", ""), file=out_file)

    in_file.close()
    out_file.close()


def send_safe_message(file_name, friend_name, key):
    my_file = open(file_name, "r")
    friend_text = friend_name + ".txt"
    new_file = open(friend_text, "w")
    cipher_text = ""
    for line in my_file.readlines():
        cipher_line = encode(line.rstrip(), key)
        cipher_text += cipher_line + "\n"
    print(cipher_text.rstrip(), file=new_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    my_file = open(file_name, "r")
    my_pad = open(pad_file_name, "r")
    friend_file = friend_name + ".txt"
    new_friend_file = open(friend_file, "w")
    read_file = my_file.read()
    read_key = my_pad.read()
    uncracked = encode_better(read_file, read_key)
    print(uncracked, file=new_friend_file)


if __name__ == '__main__':
    pass
