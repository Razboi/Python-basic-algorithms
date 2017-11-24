"""
Using the Python language, have the function LetterChanges(str) take the str
parameter being passed and modify it using the following algorithm. Replace every
letter in the string with the letter following it in the alphabet.
Then capitalize every vowel in this new string (a, e, i, o, u) and finally
return this modified string.
"""


def letter_changes(sen):
    new_sen = ""
    for i in sen:
        # if the word is z add A to the new str
        if i == "z":
            new_sen += "A"
        # set the letter to the next letter in the alphabet. If its a vowel capitalize it
        else:
            letter = chr(ord(i) + 1)
            if letter in ["a", "e", "i", "o", "u"]:
                letter = letter.upper()
            new_sen += letter
    return new_sen


print(letter_changes("abcdez"))
