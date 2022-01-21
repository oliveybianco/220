"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    upper = eval(input("What is the upper bound? "))



def multiplication_table():
    pass


def triangle_area():
    side_a = eval(input("Enter the length of side a: "))
    side_b = eval(input("Enter the length of side b: "))
    side_c = eval(input("Enter the length of side c: "))
    add = side_a + side_b + side_c
    s = add / 2
    step_one = (s-side_a) * (s-side_b) *(s-side_c)
    step_two = s * step_one
    area = math.sqrt(step_two)
    print("Area is: ", area)

def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    nums = list(range(lower, upper))
    for i in range(len(nums)):
        add = sum(i ** 2)




def power():
    base = eval(input("Enter the base: "))
    power = eval(input("Enter the power: "))


if __name__ == '__main__':
    pass
