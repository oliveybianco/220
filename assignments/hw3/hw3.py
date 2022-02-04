"""
Name: <Olivia Bianco>
<hw3>.py

Problem: <Variety of for loops using accumulators.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def average():
    avg_amt = eval(input("How many grades will you enter? "))
    accumulator = 0
    grade_avg = 0
    for _ in range(avg_amt):
        accumulator += eval(input("Enter grade: "))
        grade_avg = accumulator / avg_amt
    print("Average is: ", grade_avg)


def tip_jar():
    total = 0
    for _ in range(5):
        total += eval(input("How much would you like to donate? "))
    print("total tips: ", total)


def newton():
    num = eval(input("What number do you want to square root? "))
    refine = eval(input("How many times should we improve the approximation? "))
    approx = num
    for _ in range(refine):
        approx = (approx + (num/approx)) / 2
    print("The square root is approximately: ", approx)


def sequence():
    nums = eval(input("Enter the number of terms: "))
    for i in range(0, nums):
        print(1 + (i // 2 * 2), end=' ')


def pi():
    terms = eval(input("Enter the number of terms in the series: "))
    product = 2
    for i in range(terms):
        numerator = 2 + (i // 2 * 2)
        denominator = 1 + ((i + 1) // 2 * 2)
        product = product * (numerator / denominator)
    print("pi is approximately: ", product)


if __name__ == '__main__':
    pass
