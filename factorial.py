"""
Using the Python language, have the function FirstFactorial(num) take the num parameter
being passed and return the factorial of it (e.g. if num = 4, return (4 * 3 * 2 * 1)).
For the test cases, the range will be between 1 and 18 and the input will always be an integer.
"""


def first_factorial(num):
    final_number = 1
    for i in range(1, num + 1):
        final_number *= i
        print(final_number)
    return final_number


print(first_factorial(4))
