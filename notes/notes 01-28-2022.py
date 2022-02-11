#find the roots of a quadratic function given a quadratic equation. in other words find values when x - 0
#inputs will be a, b, and c and will be used to solve for x
#outputs will be root1 and root2
#step1 = get the inputs
#step2 = calculate one of the roots, so find the positive one (root1) first then the negative (root2) one after

import math
def quadratic():
    a, b, c = eval(input("Enter coefficients a, b, and c: "))
    sqrt_d = math.sqrt(b * b - 4 * a * c)
    divide = 2 * a
    root_1 = -b + sqrt_d / divide
    root_2 = -b - sqrt_d / divide
    print("root 1 is: ", root_1)
    print("root 2 is: ", root_2)

quadratic()

