"""
Name: <Olivia Bianco>
<Hw7>.py

Problem: <Reading and writing to text files and working with functions.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def number_words(in_file_name, out_file_name):
    pass


def hourly_wages(in_file_name, out_file_name):
    pass


def calc_check_sum(isbn):
    new_isbn = isbn.replace("-", "").replace(" ", "")
    result = 0
    for i in range(len(new_isbn)):
        result = result + int(new_isbn[i]) + (10 - i)
        if result % 11 == 0:
            print(result)
        else:
            print("please enter the correct digits")
    return result


my_isbn = "0-072-94652-0"
calc_check_sum(my_isbn)
print(my_isbn)


def send_message(file_name, friend_name):
    pass


def encode():
    pass


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
