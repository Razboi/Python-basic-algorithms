"""
Using the Python language, have the function FirstReverse(str) take the
 str parameter being passed and return the string in reversed order.
 For example: if the input string is "Hello World and Coders" then your program
 should return the string sredoC dna dlroW olleH.
 """


def first_reverse(sen):
    reverse_string = ""
    for i in reversed(sen):
        reverse_string += i
    return reverse_string


print(first_reverse("this is a test"))