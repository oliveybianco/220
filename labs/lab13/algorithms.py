"""
Name: <Olivia Bianco>
<Lab13>.py

Problem: <Working with lists and files. Sorting lists using selection sort methods.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def read_data(file_name):
    i = 0
    my_list = []
    my_file = open(file_name, "r")
    line = my_file.read()
    words = line.split()
    while i < len(words):
        nums = eval(words[i])
        my_list.append(nums)
        i += 1
    my_file.close()
    return my_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val in values:
            return True
        else:
            return False

    i += 1


def selection_sort(values):
    for i in range(len(values)):
        pos = i
        lowest = values[i]
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def calc_area(rect):
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    p1_x = point_1.getX()
    p1_y = point_1.getY()
    p2_x = point_2.getX()
    p2_y = point_2.getY()
    width = p2_x - p1_x
    height = p2_y - p1_y
    area = width * height
    return area


def rect_sort(rectangles):
    areas_list = []
    for rectangle in rectangles:
        each_area = calc_area(rectangle)
        areas_list.append(each_area)
        for i in range(len(areas_list)):
            pos = i
            lowest = areas_list[i]
            for j in range(i + 1, len(areas_list)):
                if areas_list[j] < lowest:
                    lowest = areas_list[j]
                    pos = j
            areas_list[i], areas_list[pos] = areas_list[pos], areas_list[i]
