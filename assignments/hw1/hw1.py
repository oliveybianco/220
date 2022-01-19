"""
Name: <Olivia Bianco>
<hw1>.py

Problem: <Basic arithmetic programs.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
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
    ratio = shots_made / total_shots
    percentage = ratio * 100
    print("Shooting Percentage = ", percentage, "%")


def coffee():
    c_pounds = eval(input("How many pounds of coffee would you like?"))
    overhead = 1.50
    coffee_cost = c_pounds * 10.5
    shipping_cost = c_pounds * .86
    total_pounds_cost = coffee_cost + shipping_cost + overhead
    print("Your total is: ", total_pounds_cost)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    conversion = kilometers / 1.61
    print("That's", conversion, "miles!")


if __name__ == '__main__':
    pass
