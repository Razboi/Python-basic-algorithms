"""
Using the Python language, have the function CorrectPath(str) read the str
parameter being passed, which will represent the movements made in a 5x5 grid of
cells starting from the top left position. The characters in the input string will
be entirely composed of: r, l, u, d, ?. Each of the characters stand for the
direction to take within the grid, for example: r = right, l = left, u = up, d = down.
Your goal is to determine what characters the question marks should be in order
for a path to be created to go from the top left of the grid all the way to the
bottom right.
"""


def correct_path(sen):
    # xy coordinates
    position = [0, 0]
    """according to the instructions add or subtract to the xy coordinates of
  position."""
    for i in sen:
        if i == "r":
            position[0] += 1
        if i == "d":
            position[1] += 1
        if i == "l":
            position[0] -= 1
        if i == "u":
            position[1] -= 1
    new_path = ""
    # substitute ? with the according instruction depending on the values of the xy coordinates
    for i in sen:
        if i == "?":
            if position[0] < 4:
                new_path += "r"
                position[0] += 1
            elif position[1] < 4:
                new_path += "d"
                position[1] += 1
            elif position[0] > 4:
                new_path += "l"
                position[0] -= 1
            elif position[1] > 4:
                new_path += "u"
                position[1] -= 1
            else:
                new_path += "u"
                position[1] -= 1
        # if its a normal instruction add it
        else:
            new_path += i
    return new_path


print(correct_path("drdr??rrddd?"))
