"""
Name: <Olivia Bianco>
<Lab10>.py

Problem: <Creating a user-defined object, working with lists, working with decision structures.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work. Using graphics.>
"""

from graphics import GraphWin, Rectangle, Point
from button import Button
from door import Door


def main():
    height_px = 600
    width_px = 600
    win = GraphWin("Test", width_px, height_px)
    win.setBackground("light gray")

    my_button = Button(Rectangle(Point(200, 100), Point(400, 200)), "Exit")
    my_button.color_button("light gray")
    my_button.draw(win)

    my_door = Door(Rectangle(Point(200, 250), Point(400, 500)), "Closed")
    my_door.color_door("red")
    my_door.draw(win)

    pt = win.getMouse()
    while not my_button.is_clicked(pt):
        if my_door.is_clicked(pt) and my_door.get_label() == "Open":
            my_door.close("red", "Closed")
        else:
            my_door.open("light gray", "Open")
        pt = win.getMouse()

    win.close()


main()



