from graphics import GraphWin, Rectangle, Point, Text, Line



def greeting_card():
    width = 400
    height = 400
    win = GraphWin("Valentine's Day", width, height)
    win.setBackground("white")
    aline = Line(Point(1, 3), Point(4, 7))
    aline.draw(win)
    input("hit enter to close")