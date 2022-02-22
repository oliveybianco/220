"""
Name: <Olivia Bianco>
<HW5>.py

Problem: <Using strings and lists. Slicing and indexing.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def name_reverse():
    name = input("enter a name (first last): ")
    first, last = name.split(" ")
    ", ".join([last, first])
    swap = last + ", " + first
    print(swap)


def company_name():
    domain = input("enter a domain: ")
    print(domain[4:-4])


def initials():
    students = eval(input("How many students are in the class? "))
    for i in range(students):
        stu_name = input("What is the name of student " + str(i + 1) + "?")
        first, last = stu_name.split(" ")
        f_letter = first[0]
        l_letter = last[0]
        both_letters = f_letter + l_letter
        print(both_letters)


def names():
    name_lst = (input("Enter a list of names: "))
    new_lst = list(name_lst.split(","))
    for name in new_lst:
        first, last = name.split()
        f_initial = first[0]
        l_initial = last[0]
        letters_together = f_initial + l_initial
        print(letters_together, end=" ")


def thirds():
    sentences = eval(input("Enter the number of sentences: "))
    new_list = []
    for i in range(sentences):
        sentence = input("Enter sentence " + str(i + 1) + ": ")
        new_list.append(sentence)
    for j in range(0, len(new_list)):
        letters = new_list[j][0::3]
        print(letters)

def word_average():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)


def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin: ")
    words = sentence.split()
    answer = " "
    middle = " "
    for word in words:
        first = word[0]
        mid = middle+word[1::]
        answer = answer + (mid.lower() + first.lower() + "ay")
        answer = answer.lstrip()
    print(answer)


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
