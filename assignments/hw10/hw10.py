"""
Name: <Olivia Bianco>
<HW10>.py

Problem: <Using decision structures, creating classes and objects.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def fibonacci(n):
    if n == 1:
        return None
    elif n == 2:
        return 1
    else:
        return (n-1) + (n-2)


def double_investment(principle, rate):
    pass


def syracuse(n):
    pass
    sequence = []
    new_num = 0
    while n >= 1:
        if n % 2 == 0:
            new_num = n / 2
            sequence.append(new_num)
        else:
            new_num = 3 * n + 1
            sequence.append(new_num)
    return sequence


def goldbach(n):
    pass



