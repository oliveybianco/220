"""
Name: <Olivia Bianco>
<HW10>.py

Problem: <Creating face methods.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        h_size = self.head.getRadius()
        h_center = self.head.getCenter()
        m_size = 0.8 * h_size
        m_off = h_size / 2.0
        point_3 = h_center.clone()
        point_3.move(0, m_off * 1.8)
        point_1 = h_center.clone()
        point_1.move(-m_size / 2, m_off)
        point_2 = h_center.clone()
        point_2.move(m_size / 2, m_off)
        left_l = Line(point_1, point_3)
        right_1 = Line(point_2, point_3)
        right_1.draw(self.window)
        left_l.draw(self.window)

    def shock(self):
        size = self.head.getRadius()
        m_size = .20 * size
        m_center = self.mouth.getCenter()
        shocked = Circle(m_center, m_size)
        self.mouth.undraw()
        self.mouth = shocked
        self.mouth.draw(self.window)

    def wink(self):
        h_center = self.head.getCenter()
        h_size = self.head.getRadius()
        eye_1 = h_size / 3.0
        point_1 = h_center.clone()
        point_1.move(-eye_1 / 1.6, -eye_1)
        point_2 = h_center.clone()
        point_2.move(eye_1 / 2, -eye_1)
        new_eye = Line(point_1, point_2)
        new_eye.move(-eye_1, 0)
        self.left_eye.undraw()
        self.left_eye = new_eye
        new_eye.draw(self.window)
        self.smile()


