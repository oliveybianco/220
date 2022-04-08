"""
Name: <Olivia Bianco>
<HW10>.py

Problem: <Using decision structures, creating classes and objects.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

from graphics import GraphWin, Point
from face import Face


def fibonacci(num):
    num1, num2 = 1, 1
    sequence = []
    count = 0
    while count < num and num > 1:
        sequence.append(num1)
        result = num1 + num2
        num1 = num2
        num2 = result
        count += 1
    return sequence[num - 1]


def double_investment(principle, rate):  # numbers are too large
    years = 0
    total = principle
    while total <= principle * 2:
        total = total + total * rate + 1
        years += 1
    return years


def syracuse(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def goldbach(n):
    primes = []
    val = 1
    while val <= n:
        count = 0
        i = 2
        while i <= val // 2:
            if val % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and val != 1:
            primes.append(val)
        val = val + 1

    if n % 2 != 0:
        return None

    idx_a = 0
    idx_b = 0

    prime_a = primes[idx_a]
    prime_b = primes[idx_b]

    while prime_a + prime_b != n:
        if prime_b == primes[-1]:
            idx_a = idx_a + 1
            idx_b = idx_a + 1
            prime_a = primes[idx_a]
            prime_b = primes[idx_b]
        else:
            idx_b = idx_b + 1
            prime_b = primes[idx_b]
    return [prime_a, prime_b]


# def main():
#     win = GraphWin("Face", 700, 700)
#     center = Point(350,350)
#     size = 300
#     my_face = Face(win, center, size)
#     my_face.wink()
#     win.getMouse()
#     win.close()
