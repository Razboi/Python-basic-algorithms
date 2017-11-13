"""
Using the Python language, have the function SimpleAdding(num)
add up all the numbers from 1 to num.
"""


def simple_adding(num):
    for i in range(1, num):
        num += i
    return num


print(simple_adding(4))
