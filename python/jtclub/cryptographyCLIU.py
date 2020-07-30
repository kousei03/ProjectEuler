# Corbin Frisvold
# Weekly Challenge 4 Problem 2
# 10/22/19

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZA'
lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza'
phrase = str(raw_input("Input: "))
crypt = ''
n = ''
if len(phrase) > 10:
    print("Please stay equal to or under 10 characters.")
else:
    for i in range(len(phrase)):
        if phrase[i].isupper():
            crypt += str(upper[upper.index(phrase[i])+int(n)])
        elif phrase[i].islower():
            crypt += str(lower[lower.index(phrase[i])+int(n)])
        else:
            n += phrase[i]
            
print(crypt)