def longestWord(sen):
    words = sen.split(" ")
    finalword = ""
    for i in words:
        if len(i) > len(finalword):
            finalword = i
    return finalword


print(longestWord("i love python"))
