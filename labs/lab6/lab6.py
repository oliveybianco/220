"""
Name: <Olivia Bianco>
<Lab6>.py

Problem: <Graphics and encoding.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""
from graphics import GraphWin, Rectangle, Point, Text, Entry


def vigenere():
    width = 400
    height = 400
    win = GraphWin("Vigenere", width, height)
    win.setBackground("white")

    msg_encode = "Message to encode"
    inst = Text(Point(100, 100), msg_encode)
    inst.draw(win)
    input_1 = Entry(Point(250, 100), 25)
    input_1.draw(win)

    key = "Enter Keyword"
    inst_2 = Text(Point(100, 150), key)
    inst_2.draw(win)
    input_2 = Entry(Point(200, 150), 10)
    input_2.draw(win)

    button = Rectangle(Point(150, 225), Point(250, 175))
    button.draw(win)
    rec_center = button.getCenter()
    inst_button = Text(rec_center, "Encode")
    inst_button.draw(win)
    win.getMouse()

    msg_get = input_1.getText()
    msg_get = msg_get.upper()
    msg_get = msg_get.replace(" ", "")

    key_get = input_2.getText()
    key_get = key_get.upper()
    cipher = ""

    for i in range(len(msg_get)):
        character = ord(msg_get[i]) - 65
        shift = ord(key_get[i % len(key_get)]) - 65
        add = character + shift
        check = add % 26
        convert = chr(65 + check)
        cipher += convert

    button.undraw()
    inst_button.undraw()
    result = Text(Point(200, 300), "Resulting Message")
    result.draw(win)
    result_num = Text(Point(200, 325), cipher)
    result_num.draw(win)

    close = Text(Point(200, 390), "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()


vigenere()
