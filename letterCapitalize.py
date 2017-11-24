"""
Using the Python language, have the function LetterCapitalize(str) take the str
parameter being passed and capitalize the first letter of each word. Words will be
separated by only one space.
"""


def letter_capitalize(sen):
    word_list = sen.split(" ")
    new_words = ""
    # for each word form a new word with the first letter capitalized and the rest the same
    for i in word_list:
        i = i[0].capitalize() + i[1::]
        # add the new word to the new sentence
        new_words += i + " "
    return new_words


print(letter_capitalize("this is a test"))
