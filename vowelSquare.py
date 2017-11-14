"""
Using the Python language, have the function VowelSquare(strArr) take the strArr parameter being passed which will be a
2D matrix of some arbitrary size filled with letters from the alphabet, and determine if a 2x2 square composed entirely
of vowels exists in the matrix.
If a 2x2 square of vowels is found your program should return the top-left position (row-column) of the square.
If no 2x2 square of vowels exists, then return the string not found.
"""


def vowel_square(arr):
    vowels = "aeiou"
    # for every row
    for i in range(0, len(arr)):
        # for every column in the row
        for j in range(0, len(arr[i])):
            # if the value is in the vowels list and its not the last row or column
            if arr[i][j] in vowels and i != len(arr) - 1 and j != len(arr[i]) - 1:
                # if the values in the next column, row, and row and column are also vowels
                if arr[i][j + 1] in vowels and arr[i + 1][j] in vowels and arr[i + 1][j + 1] in vowels:
                    # return the position of the top left vowel in the 2x2 square
                    return f"{i}-{j}"
    # no matches return not found
    return "not found"


print(vowel_square(["abcd", "eikr", "oufj"]))
