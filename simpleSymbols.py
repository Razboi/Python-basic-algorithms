"""
Using the Python language, have the function SimpleSymbols(str) take the str
parameter being passed and determine if it is an acceptable sequence by either
returning the string true or false. The str parameter will be composed of + and =
symbols with several letters between them (ie. ++d+===+c++==a) and for the string
to be true each letter must be surrounded by a + symbol.
The string will not be empty and will have at least one letter.
"""


def simple_symbols(sen):
    sen_list = list(sen)
    for i in range(0, len(sen_list)):
        if sen_list[0].isalpha() or sen_list[-1].isalpha():
            return False
        if sen_list[i].isalpha():
            if sen_list[i + 1] != "+" or sen_list[i - 1] != "+":
                return False
    return True


print(simple_symbols("+a+b+==+d+c+d+"))
