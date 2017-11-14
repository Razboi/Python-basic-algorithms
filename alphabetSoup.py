"""
Using the Python language, have the function AlphabetSoup(str) take the str
string parameter being passed and return the string with the letters in alphabetical
order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not
be included in the string.
"""


def alphabet_soup(sen):
    # delete the whitespaces (replace with empty) and sort
    return sorted(sen.replace(" ", ""))


print(alphabet_soup("this is a test"))
