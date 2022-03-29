"""
Name: <Olivia Bianco>
<Lab10>.py

Problem: <Creating a door class.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work. Using graphics.>
"""

from graphics import Point, Text


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        center = self.shape.getCenter()
        self.text = Text(center, label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x_val, y_val = point.getX(), point.getY()
        door_p1 = self.shape.getP1()
        door_p2 = self.shape.getP2()
        x1, y1 = door_p1.getX(), door_p1.getY()
        x2, y2 = door_p2.getX(), door_p2.getY()
        require_1 = x1 <= x_val <= x2
        require_2 = y1 <= y_val <= y2
        if require_1 and require_2:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False

    def set_secret(self, secret):
        self.secret = secret
