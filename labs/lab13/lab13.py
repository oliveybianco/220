"""
Name: <Olivia Bianco>
<Lab13>.py

Problem: <Capstone, working with lists and sorting them.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def trade_alert(file_name):
    my_file = open(file_name, "r")
    line = my_file.read()
    nums = line.split()
    for num in range(len(nums)):
        if eval(nums[num]) > 830:
            spot = num + 1
            print("warning! the volume exceeds 830 at " + str(spot) + " seconds!")
        elif eval(nums[num]) == 500:
            spot = num + 1
            print("pay attention! the volume is equal to 500 at " + str(spot) + " seconds!")

    my_file.close()

