"""
Name: <Olivia Bianco>
<Lab5>.py

Problem: <Graphics and strings lab.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""
from graphics import GraphWin, Point, Polygon, Text, Circle, Entry, color_rgb
import math


def triangle():
    width = 400
    height = 400
    win = GraphWin("Draw a Triangle", width, height)
    win.setBackground("white")
    instructions = Text(Point(200, 200), "Click three times")
    instructions.draw(win)
    p_1 = win.getMouse()
    p_1.draw(win)
    p_2 = win.getMouse()
    p_2.draw(win)
    p_3 = win.getMouse()
    p_3.draw(win)
    tri = Polygon(p_1, p_2, p_3)
    tri.setFill("green")
    tri.setOutline("green")
    tri.draw(win)

    p1_x = p_1.getX()
    p1_y = p_1.getY()
    p2_x = p_2.getX()
    p2_y = p_2.getY()
    p3_x = p_3.getX()
    p3_y = p_3.getY()
    length1_dx = p2_x - p1_x
    length1_dy = p2_y - p1_x
    length2_dx = p3_x - p2_x
    length2_dy = p3_y - p2_y
    length3_dx = p1_x - p3_x
    length3_dy = p1_y - p3_y

    side_a = math.sqrt((length1_dx**2) + (length1_dy**2))
    side_b = math.sqrt((length2_dx**2) + (length2_dy**2))
    side_c = math.sqrt((length3_dx**2) + (length3_dy**2))
    perimeter = side_a + side_b + side_c
    p_info = "Perimeter:", perimeter
    p_info = Text(Point(200, 325), p_info)
    p_info.draw(win)

    s_value = (side_a + side_b + side_c) / 2
    step_1 = s_value * (s_value-side_a) * (s_value - side_b) * (s_value - side_c)
    area = math.sqrt(step_1)
    area_info = "Area:", area
    area_info = Text(Point(200, 350), area_info)
    area_info.draw(win)

    close = Text(Point(200, 150), "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    input_1 = Entry(Point(win_width / 2 + 25, win_height / 2 + 40), 10)
    input_1.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    input_2 = Entry(Point(win_width / 2 + 25, win_height / 2 + 70), 10)
    input_2.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    input_3 = Entry(Point(win_width / 2 + 25, win_height / 2 + 100), 10)
    input_3.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red_get = input_1.getText()
        fill_r = eval(red_get)
        blue_get = input_2.getText()
        fill_b = eval(blue_get)
        green_get = input_3.getText()
        fill_g = eval(green_get)
        shape.setFill(color_rgb(fill_r, fill_b, fill_g))

    # Wait for another click to exit
    close = Text(Point(200, 50), "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()


def process_string():
    user_input = input("Enter a string to process: ")
    first_char = user_input[0]
    print(first_char)
    last_char = user_input[-1]
    print(last_char)
    positions = user_input[1:6]
    print(positions)
    concat = user_input[0] + user_input[-1]
    print(concat)
    first_three = user_input[0:3] * 10
    print(first_three)

    for l in user_input:
        print(l)

    num_chars = len(user_input)
    print(num_chars)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[-1])]
    print(x)
    x = values[2] + values[0] + float(values[-1])
    print(x)
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Enter the number of terms in the series: "))
    acc = 0
    for i in range(terms):
        sequence = 2 + 2 * (i % 3)
        print(sequence, end=" ")
        acc = acc + sequence
    print("\n", "Sum =", acc)


def target():
    win = GraphWin("Target", 400, 400)
    center = Point(200, 200)
    w_ring = Circle(center, 200)
    w_ring.setFill("white")
    w_ring.draw(win)
    b_ring = Circle(center, 170)
    b_ring.setFill("black")
    b_ring.draw(win)
    blue_ring = Circle(center, 130)
    blue_ring.setFill("blue")
    blue_ring.draw(win)
    r_ring = Circle(center, 90)
    r_ring.setFill("red")
    r_ring.draw(win)
    y_ring = Circle(center, 40)
    y_ring.setFill("yellow")
    y_ring.draw(win)

    instructions = Text(Point(200, 380), "Click to close")
    instructions.setSize(18)
    instructions.draw(win)
    win.getMouse()
    win.close()
