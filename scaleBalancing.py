"""
Using the Python language, have the function ScaleBalancing(strArr) read strArr which will contain two elements, the
first being the two positive integer weights on a balance scale (left and right sides) and the second element being a
list of available weights as positive integers. Your goal is to determine if you can balance the scale by using the
least amount of weights from the list, but using at most only 2 weights.
"""


def scale_balancing(arr):
    b1, b2 = arr[0]
    w = arr[1]
    # if adding any single weight to b1 or b2 balances the scale, return the weight
    for i in range(0, len(w)):
        if b1 + w[i] == b2 or b2 + w[i] == b1:
            return w[i]
    """for any two weights if adding one to b1 and one to b2 or two to b1 or two to b2
    balances the scale return the values of the weights"""
    for i in range(0, len(w)):
        # i represents one weight and j loops through all the others
        for j in range(i + 1, len(w)):
            if b1 + w[i] == b2 + w[j] or b2 + w[i] == b1 + w[j] or b1 + w[i] + w[j] == b2 or b2 + w[i] + w[j] == b1:
                return f"{w[i]},{w[j]}"
    return "not possible"


print(scale_balancing([[3, 6], [1, 2, 3, 7]]))
