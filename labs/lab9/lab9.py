"""
Name: <Olivia Bianco>
<Lab9>.py

Problem: <Creating a Tic-Tac-Toe game.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position - 1]).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, shape):  # fills the spot with an x or o
    new_shape = shape.lower().strip()
    board[position-1] = new_shape


def winning_game(board):  # each possibility
    possibilities = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 6], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
    for possibility in possibilities:
        acc = 0
        for position in possibility:
            if board[position - 1] == "x":
                acc += 1
            if acc == 3:
                return True
    for possibility in possibilities:
        acc = 0
        for position in possibility:
            if board[position - 1] == "o":
                acc += 1
            if acc == 3:
                return True
    return False


def game_over(board):
    if winning_game(board):
        return True
    for i in range(len(board)):
        if str(i).isnumeric():
            return False
    return True


def get_winner(board):
    possibilities = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 6], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
    for possibility in possibilities:
        acc = 0
        for position in possibility:
            if board[position - 1] == "x":
                acc += 1
            if acc == 3:
                return "x"
    for possibility in possibilities:
        acc = 0
        for position in possibility:
            if board[position - 1] == "o":
                acc += 1
            if acc == 3:
                return "o"
    return None


def play(board):
    print("Let's play Tic-Tac-Toe!")
    print("Enter a number betwwen 1 and 9 to choose a square on the board.")
    print("The player with three in a row wins")
    print("Type yes if you want to continue and no if you do not.")
    print_board(board)
    start = input("Do you want to play? ")
    while start == "yes":
        i = 0
        while i <= 9 and not game_over(board):
            shape = ""
            if (i % 2) == 0:
                shape += "x"
            elif (i % 2) == 1:
                shape += "o"
            new_input = input("{}'s choose a position:".format(shape))
            while not is_legal(board, new_input):
                start = input("That position is filled. Please choose a new position.")
            fill_spot(board, start, shape)
            print_board(board)
            i += 1
            if game_over(board):
                if get_winner(board) == "x":
                    print("x wins!")
                elif get_winner(board) == "o":
                    print("o wins!")
                else:
                    print("Tie.")
    user = input("Do you want to play again? ")
    board = build_board()


def main():
    play(build_board())


if __name__ == '__main__':
    main()
