def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_point_two = win.getMouse()
    radius_two = math.sqrt(
        (center_two.getX() - circumference_point_two.getX()) ** 2 +
        (center_two.getY() - circumference_point_two.getY()) ** 2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("light green")
    circle_two.draw(win)

    overlap_message = Text(Point(5, 4), "The circles overlap.")
    not_overlap_message = Text(Point(5, 4), "The circles do not overlap.")
    closing_message = Text(Point(5, 3), "Click again to close.")

    if did_overlap(circle_one, circle_two):
        overlap_message.draw(win)
        closing_message.draw(win)
    else:
        not_overlap_message.draw(win)
        closing_message.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    center_one = circle_one.getCenter()
    p1x = center_one.getX()
    p1y = center_one.getY()

    center_two = circle_two.getCenter()
    p2x = center_two.getX()
    p2y = center_two.getY()

    rad1 = circle_one.getRadius()
    rad2 = circle_two.getRadius()

    distance = ((p2x - p1x) ** 2 + (p2y - p1y) ** 2) ** (1 / 2)
    if distance <= rad1 + rad2:
        print("The circles overlap.")
        return True
    else:
        print("The circles do not overlap.")
        return False

