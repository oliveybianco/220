"""
Name: <Olivia Bianco>
<lab2>.py

Problem: <For loop to calculate means.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def means():
    values = eval(input("Enter the values to be entered: "))
    rms_result = 0
    harmonic_result = 0
    geometric_result = 1
    for i in range(values):
        value_x = eval(input("Enter value: " + str(i + 1)))
        rms_result = value_x**2 + rms_result
        rms_avg = (rms_result / values) ** (1/2)
        harmonic_result = (1/value_x) + harmonic_result
        harmonic_mean = values / harmonic_result
        geometric_result = value_x * geometric_result
        geometric_mean = geometric_result ** (1 / values)
    print(round(rms_avg, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


means()
