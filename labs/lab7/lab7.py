"""
Name: <Olivia Bianco>
<Lab7>.py

Problem: <Code bites. Working with different functions.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

import math
from random import randint
from graphics import color_rgb, GraphWin, Circle, Point
import time


def get_random(int_move_amount):
    ran_num = randint(-int_move_amount, int_move_amount)
    return ran_num


def did_collide(circle_1, circle_2):
    center_1 = circle_1.getCenter()
    center_2 = circle_2.getCenter()
    radius_1 = circle_1.getRadius()
    radius_2 = circle_2.getRadius()
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


def hit_vertical(circ, win):
    height = win.getHeight()
    v_cen = circ.getCenter()
    v_cen_y = v_cen.getY()
    v_radius = circ.getRadius()
    return v_cen_y <= v_radius or v_cen_y >= height - v_radius


def hit_horizontal(circ, win):
    h_cen_circ = circ.getCenter()
    h_cen_x = h_cen_circ.getX()
    h_radius = circ.getRadius()
    width = win.getWidth()
    return h_cen_x <= h_radius or h_cen_x >= width - h_radius


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    colors = color_rgb(red, green, blue)
    return colors


def bumper():
    win = GraphWin("Bumper", 400, 400)
    win.setBackground("white")
    circ_1 = Circle(Point(randint(1, 20), randint(1, 20)), 30)
    circ_1.setFill(get_random_color())
    circ_1.draw(win)
    circ_2 = Circle(Point(randint(1, 20), randint(1, 20)), 30)
    circ_2.setFill(get_random_color())
    circ_2.draw(win)

    circ1_movex = get_random(30)
    circ1_movey = get_random(30)
    circ2_movex = get_random(30)
    circ2_movey = get_random(30)

    while not win.checkMouse():
        circ_1.move(circ1_movex, circ1_movey)
        circ_2.move(circ2_movex, circ2_movey)

        if did_collide(circ_1, circ_2):
            circ1_movex = -circ1_movex
            circ1_movey = -circ1_movey
            circ2_movex = -circ2_movex
            circ2_movey = -circ2_movey

        if hit_vertical(circ_1, win):
            circ1_movex = -circ1_movex
            circ1_movey = -circ1_movey

        if hit_vertical(circ_2, win):
            circ2_movex = -circ2_movex
            circ2_movey = -circ2_movey

        if hit_horizontal(circ_1, win):
            circ1_movex = -circ1_movex
            circ1_movey = -circ1_movey

        if hit_horizontal(circ_2, win):
            circ2_movex = -circ2_movex
            circ2_movey = -circ2_movey

        time.sleep(.30)

    win.close()


bumper()
