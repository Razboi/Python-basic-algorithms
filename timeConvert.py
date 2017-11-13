"""
Using the Python language, have the function TimeConvert(num) take the num
parameter being passed and return the number of hours and minutes the parameter
converts to (ie. if num = 63 then the output should be 1:3). Separate the number
of hours and minutes with a colon.
"""


def time_convert(num):
    # Returns hours:minutes. Minutes comes from the remainder of num and 60
    return str(round(num / 60)) + ":" + str(num % 60)


print(time_convert(145))
