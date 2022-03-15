"""
Name: <Olivia Bianco>
<Lab8>.py

Problem: <Working with file systems to compute student and class averages from a given list.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    in_read = in_file.readlines()
    total_class_avg = 0
    valid_stu = 0

    for line in in_read:
        averages = 0
        weight = 0
        class_avg = 0
        add_avg = 0
        split_file = line.split(":")
        name = split_file[0]
        stu_grades = split_file[1].strip().split()
        for num in range(0, len(stu_grades), 2):
            weight = weight + eval(stu_grades[num])
            averages = eval(stu_grades[num + 1])
            add_avg = (eval(stu_grades[num]) * averages) + add_avg
        class_avg = class_avg + (add_avg / 100)

        if weight < 100:
            averages = "Error: The weights are less than 100."
        elif weight > 100:
            averages = "Error: The weights are more than 100."
        else:
            total_class_avg = total_class_avg + class_avg
            valid_stu = valid_stu + 1
            averages = round(class_avg, 1)
        new_avg = total_class_avg / valid_stu

        out_file.write(str(name) + str("'s average: ") + str(averages) + "\n")
    out_file.write(str("Class average: ") + str(new_avg))

    in_file.close()
    out_file.close()
