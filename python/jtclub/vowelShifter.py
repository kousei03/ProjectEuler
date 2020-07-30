# Corbin Frisvold
# Weekly Challenge 4 Problem 1 Vowel Shifter
# 10/22/19

vowelslower = ["a", "e", "i", "o", "u", "a"]
vowelsupper = ["A", "E", "I", "O", "U", "A"]
shift = ""
phrase = str(raw_input("Enter a sentence.\n"))
for i in range(len(phrase)):
    if phrase[i] in vowelslower or phrase[i] in vowelsupper:
        if phrase[i].islower():
            shift += vowelslower[vowelslower.index(phrase[i])+1]
        else:
            shift += vowelsupper[vowelsupper.index(phrase[i])+1]
    else:
        shift += phrase[i]
print(shift)