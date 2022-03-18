"""
Name: <Olivia Bianco>
<HW8>.py

Problem: <Using conditional control structures and working with functions.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

import math
from graphics import GraphWin, Circle, Text, Point


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    summed = sum(nums)
    return summed


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    summation = []
    for i in range(len(nums)):
        num_split = nums[i].split(", ")
        to_numbers(num_split)
        square_each(num_split)
        values = sum_list(num_split)
        summation.append(values)
    return summation


def starter(weight, wins):
    requirement_1 = 150 <= weight < 160 and wins >= 5
    requirement_2 = weight > 199 or wins > 20
    if requirement_1:
        return True
    elif requirement_2:
        return True
    else:
        return False


def leap_year(year):
    if year % 400 == 0 or year % 100 and year % 4 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    win.setBackground("white")

    center = win.getMouse()  # first circle
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_2 = win.getMouse()
    radius_2 = math.sqrt(
        ((center_2.getX() - circumference_2.getX()) ** 2 + (center_2.getY() - circumference_2.getY()) ** 2))
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    true_msg = Text(Point(5, 4), "The circles do overlap.")
    false_msg = Text(Point(5, 4), "The circles do not overlap.")
    close = Text(Point(5, 3), "Click again to close.")

    if did_overlap(circle_one, circle_two):
        true_msg.draw(win)
        close.draw(win)
    else:
        false_msg.draw(win)
        close.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    center_1 = circle_one.getCenter()
    center_2 = circle_two.getCenter()
    radius_1 = circle_one.getRadius()
    radius_2 = circle_two.getRadius()
    sum_radii = radius_1 + radius_2

    cen1_x = center_1.getX()
    cen1_y = center_1.getY()
    cen2_x = center_2.getX()
    cen2_y = center_2.getY()
    first_val = (cen1_x - cen2_x) ** 2
    sec_val = (cen1_y - cen2_y) ** 2
    distance = math.sqrt(first_val + sec_val)
    if distance <= sum_radii:
        return True
    else:
        return False


if __name__ == '__main__':
    pass
