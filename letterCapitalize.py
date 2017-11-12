"""
Using the Python language, have the function LetterCapitalize(str) take the str
parameter being passed and capitalize the first letter of each word. Words will be
separated by only one space.
"""


def letter_capitalize(sen):
    word_list = sen.split(" ")
    new_words = ""
    for i in word_list:
        i = i[0].capitalize() + i[1::]
        new_words += i + " "
    return new_words


print(letter_capitalize("this is a test"))
