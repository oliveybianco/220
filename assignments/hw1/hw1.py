"""
Name: <Olivia Bianco>
<hw1>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area = ", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume = ", volume)

def shooting_percentage():
    total_shots = eval(input("Enter total shots: "))
    shots_made = eval(input("Enter shots made: "))
    percentage = shots_made / total_shots
    print("Shooting Percentage = ", percentage)

def coffee():
    c_pounds = eval(input("How many pounds of coffee would you like?" ))
    coffee_cost = c_pounds * 10.5
    shipping_cost = coffee_cost * .86
    total_pounds_cost = shipping_cost + 1.50
    print("Your total is: ", total_pounds_cost)

def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    conversion = kilometers / 1.61


if __name__ == '__main__':
    pass
