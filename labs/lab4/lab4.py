"""
Name: <Olivia Bianco>
<Lab4>.py

Problem: <Greeting Card.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""
from graphics import GraphWin, Point, Text, Polygon, Line
import time


def greeting_card():
    width = 400
    height = 400
    win = GraphWin("Valentine's Day", width, height)
    win.setBackground("purple")
    greeting = Text(Point(200, 10), "Happy Valentine's Day!")
    greeting.setSize(30)
    greeting.setFace("arial")
    greeting.setStyle("bold")
    greeting.setTextColor("hot pink")
    greeting.draw(win)
    p1 = Point(200, 300)
    p1.draw(win)
    p2 = Point(125, 150)
    p2.draw(win)
    p3 = Point(275, 150)
    p3.draw(win)
    p4 = Point(175, 75)
    p4.draw(win)
    p5 = Point(200, 125)
    p5.draw(win)
    p6 = Point(225, 75)
    p6.draw(win)
    heart = Polygon(p1, p2, p4, p5, p6, p3)
    heart.setFill("hot pink")
    heart.setOutline("hot pink")
    heart.draw(win)

    a_line = Line(Point(50, 375), Point(100, 300))
    a_line.setOutline("red")
    a_line.setArrow("last")
    a_line.setWidth(12)
    a_line.draw(win)

    for i in range(5):
        a_line.move(100, -100)
        time.sleep(.50)
    inst_pt = Text(Point(200, 375), "Click again to close")
    inst_pt.setTextColor("white")
    inst_pt.draw(win)
    win.getMouse()
    win.close()


greeting_card()
