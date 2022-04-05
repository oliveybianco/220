"""
Name: <Olivia Bianco>
<Lab11>.py

Problem: <Creating a three door game>

Certification of Authenticity:
<I certify that this assignment is entirely my own work. Using graphics.>
"""

from lab10.button import Button
from lab10.door import Door
from random import randint
from graphics import GraphWin, Text, Rectangle, Point


def main():
    win = GraphWin("Three Door Game", 700, 700)
    win.setBackground("white")
    door_1 = Door(Rectangle(Point(150, 200), Point(250, 600)), "Door 1")  # Drawing each door
    door_1.color_door("salmon4")
    door_1.draw(win)
    door_2 = Door(Rectangle(Point(300, 200), Point(400, 600)), "Door 2")
    door_2.color_door("salmon4")
    door_2.draw(win)
    door_3 = Door(Rectangle(Point(450, 200), Point(550, 600)), "Door 3")
    door_3.color_door("salmon4")
    door_3.draw(win)
    quit_button = Button(Rectangle(Point(400, 50), Point(550, 150)), "Quit")  # Drawing the exit button
    quit_button.draw(win)
    score_wins = Rectangle(Point(50, 50), Point(150, 150))  # drawing the scoreboards
    score_wins.draw(win)
    wins_text = Text(Point(100, 40), "Wins")
    wins_text.draw(win)
    score_losses = Rectangle(Point(150, 50), Point(250, 150))
    score_losses.draw(win)
    losses_text = Text(Point(200, 40), "Losses")
    losses_text.draw(win)
    instructions = Text(Point(350, 650), "Click to guess which is the secret door!")
    instructions.draw(win)
    begin_text = Text(Point(325, 175), "I have a secret door")
    begin_text.draw(win)

    play_again = Text(Point(350, 650), "click anywhere to play again.")
    win_msg = Text(Point(325, 175), "you win!")
    loss_msg = Text(Point(325, 175), "you lost.")
    wins_acc = 0  # initializing the accumulator
    losses_acc = 0
    win_cen = score_wins.getCenter()
    w_x, w_y = win_cen.getX(), win_cen.getY()
    wins_num = Text(Point(w_x, w_y), "0")
    wins_num.draw(win)
    loss_cen = score_losses.getCenter()
    l_x, l_y = loss_cen.getX(), loss_cen.getY()
    loss_num = Text(Point(l_x, l_y), "0")
    loss_num.draw(win)

    secret_num = randint(1, 3)  # setting the secret door
    if secret_num == 1:
        door_1.set_secret(True)
    if secret_num == 2:
        door_2.set_secret(True)
    if secret_num == 3:
        door_3.set_secret(True)

    pt = win.getMouse()
    while not quit_button.is_clicked(pt):
        instructions.undraw()
        play_again.draw(win)
        begin_text.undraw()
        if door_1.is_clicked(pt) and door_1.is_secret():
            door_1.color_door("green")
            wins_acc += 1
            wins_num.undraw()
            new_wins_pt = Text(Point(w_x, w_y), wins_acc)
            new_wins_pt.draw(win)
        elif door_2.is_clicked(pt) and door_2.is_secret():
            door_2.color_door("green")
            wins_acc += 1
            wins_num.undraw()
            new_wins_pt = Text(Point(w_x, w_y), wins_acc)
            new_wins_pt.draw(win)
        elif door_3.is_clicked(pt) and door_3.is_secret():
            door_3.color_door("green")
            wins_acc += 1
            wins_num.undraw()
            new_wins_pt = Text(Point(w_x, w_y), wins_acc)
            new_wins_pt.draw(win)
        else:
            loss_msg.draw(win)
            if not door_1.is_secret() and door_1.is_clicked(pt):
                door_1.color_door("red")
                losses_acc += 1
                loss_num.undraw()
                loss_text_pt = Text(Point(l_x, l_y), losses_acc)
                loss_text_pt.draw(win)
            elif not door_2.is_secret() and door_2.is_clicked(pt):
                door_2.color_door("red")
                losses_acc += 1
                loss_num.undraw()
                loss_text_pt = Text(Point(l_x, l_y), losses_acc)
                loss_text_pt.draw(win)
            elif not door_3.is_secret() and door_3.is_clicked(pt):
                door_3.color_door("red")
                losses_acc += 1
                loss_num.undraw()
                loss_text_pt = Text(Point(l_x, l_y), losses_acc)
                loss_text_pt.draw(win)
        pt = win.getMouse()
        if quit_button.is_clicked(pt):
            win.close()
        else:
            door_1.color_door("salmon4")
            door_2.color_door("salmon4")
            door_3.color_door("salmon4")
            win_msg.undraw()
            loss_msg.undraw()
            play_again.undraw()
            instructions.draw(win)
            begin_text.draw(win)
            pt = win.getMouse()

main()
