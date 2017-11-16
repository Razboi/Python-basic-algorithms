"""
Using the Python language, have the function QuestionsMarks(str) take the str string parameter, which will contain
single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of
two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the
string false.  If there aren't any two numbers that add up to 10 in the string, then your program should return false as
well.
For example: if str is "arrb6??ee?4xxbl5???eee5" then your program should return true because there are exactly 3 question
marks between 6 and 4.
"""


def question_marks(sen):
    counter = 0
    x, y = 0, 0
    # check every character
    for i in range(0, len(sen)):
        # if its a question mark and the counter for question marks is 0 (first question mark)
        if sen[i] == "?" and counter == 0:
            # check if the character before the question mark is an integer, if it is save it as x and add 1 to counter
            try:
                x = int(sen[i - 1])
                counter += 1
            except ValueError:
                pass
        elif sen[i] == "?" and counter != 0:
            # if its a question mark and the counter for question marks is 2 (third question mark)
            if counter == 2:
                # check if the character after the question mark is an integer, if it is save it as y
                try:
                    y = int(sen[i + 1])
                    # check if the int before the first question mark and the int after the third one adds to 10
                    if x + y == 10:
                        return True
                    # reset the counter (the sum was not 10)
                    counter = 0
                except ValueError:
                    # reset the counter (the character after the third question mark was not an int)
                    counter = 0
            # if counter == 1 (second question mark) add 1 to the counter
            else:
                counter += 1
    # if there aren't any matches return false
    return False


print(question_marks("arrb6??sss?4xxbl5???ee5???e"))
