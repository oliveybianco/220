"""
Name: <Olivia Bianco>
<Hw4>.py

Problem: <Intro to using python graphics.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

import math
from graphics import GraphWin, Point, Rectangle, Text, Circle


def squares():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)
    win.setBackground("white")
    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    shape = Rectangle(Point(200, 150), Point(150, 200))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for _ in range(num_clicks):
        click = win.getMouse()

        change_x = click.getX()
        change_y = click.getY()
        new_shape1 = Point(change_x - 25, change_y - 25)
        new_shape2 = Point(change_x + 25, change_y + 25)
        new_shape = Rectangle(new_shape1, new_shape2)
        new_shape.setOutline("red")
        new_shape.setFill("red")
        new_shape.draw(win)
    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)
    win.setBackground("white")
    p_1 = win.getMouse()
    p_2 = win.getMouse()
    p1_x = p_1.getX()
    p1_y = p_1.getY()
    p2_x = p_2.getX()
    p2_y = p_2.getY()
    rec = Rectangle(Point(p1_x, p1_y), Point(p2_x, p2_y))
    rec.setFill("green")
    rec.setOutline("green")
    rec.draw(win)

    perimeter = 2 * (p2_x + p2_y)
    per_info = Text(Point(175, 350), "Perimeter: ")
    per_info.draw(win)
    per_value = Text(Point(220, 350), perimeter)
    per_value.draw(win)
    rec_area = (p1_x - p2_x) * (p1_y - p2_y)
    a_info = Text(Point(175, 375), "Area: ")
    a_info.draw(win)
    a_value = Text(Point(210, 375), rec_area)
    a_value.draw(win)

    instructions = Text(Point(200, 200), "Click again to close")
    instructions.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)
    win.setBackground("white")
    middle = Point(200, 200)
    close = Text(middle, "Click again to close")
    close.draw(win)
    center = win.getMouse()
    center.draw(win)
    c_point = win.getMouse()
    c_point.draw(win)
    x_val = (center.getX() - c_point.getX()) ** 2
    y_val = (center.getY() - c_point.getY()) ** 2
    distance = math.sqrt(x_val + y_val)
    circ = Circle(center, distance)
    circ.draw(win)
    circ.setOutline("black")
    circ.setFill("cyan")
    p_info = Point(130, 375)
    radius = Text(p_info, "Radius: ")
    radius.draw(win)
    num = Text(Point(210, 375), distance)
    num.draw(win)
    win.getMouse()
    win.close()


def pi2():
    terms = eval(input("How many terms are there? "))
    acc = 0
    numerator = 4
    denominator = 1
    change = 1
    for _ in range(terms):
        acc = acc + change * (numerator / denominator)
        denominator = denominator + 2
        change = change * -1
    print("pi approximation: ", acc)
    print("accuracy: ", abs(math.pi-acc))


if __name__ == '__main__':
    pass
