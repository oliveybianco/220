"""
Name: <Olivia Bianco>
<Lab10>.py

Problem: <Creating a button class.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work. Using graphics.>
"""
from graphics import Text, Point


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        center_point = self.shape.getCenter()
        cen_x, cen_y = center_point.getX(), center_point.getY()
        self.text = Text(Point(cen_x, cen_y), label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x_val = point.getX()
        y_val = point.getY()
        rec_p1 = self.shape.getP1()
        rec_p2 = self.shape.getP2()
        x1, y1 = rec_p1.getX(), rec_p1.getY()
        x2, y2 = rec_p2.getX(), rec_p2.getY()
        require_1 = y1 <= y_val <= y2
        require_2 = x1 <= x_val <= x2
        if require_1 and require_2:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)





