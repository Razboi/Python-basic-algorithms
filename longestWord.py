"""
Using the Python language, have the function LongestWord(sen) take the sen
parameter being passed and return the largest word in the string.
If there are two or more words that are the same length, return the first word
from the string with that length. Ignore punctuation and assume sen will not be empty.
"""


def longest_word(sen):
    words = sen.split(" ")
    final_word = ""
    for i in words:
        if len(i) > len(final_word):
            final_word = i
    return final_word


print(longest_word("i love python"))
