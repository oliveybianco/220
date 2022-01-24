"""
Name: <Olivia Bianco>
<hw2>.py

Problem: <For loop programs for arithmetic functions.>

Certification of Authenticity:
<I certify that this work is entirely my own.>
"""
import math


def sum_of_threes():
    upper = eval(input("What is the upper bound? "))
    result = 0
    for i in range(1, upper + 1):
        if i % 3 == 0:
            result = result + i
    print("sum of threes is: ", result)


def multiplication_table():
    for rows in range(1, 11):
        for columns in range(1, 11):
            multiply = rows * columns
            print(multiply, end="\t")
        print()


def triangle_area():
    side_a = eval(input("Enter the length of side a: "))
    side_b = eval(input("Enter the length of side b: "))
    side_c = eval(input("Enter the length of side c: "))
    add = side_a + side_b + side_c
    semi = add / 2
    step_one = (semi - side_a) * (semi - side_b) * (semi - side_c)
    step_two = semi * step_one
    area = math.sqrt(step_two)
    print("Area is: ", area)


def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    total = 0
    for i in range(lower, upper + 1):
        exp = i ** 2
        total = total + exp
    print(total)


def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    result = 1
    for _ in range(1, exponent + 1):
        result = base * result
    print(base, "^", exponent, "=", result)


if __name__ == '__main__':
    pass
