# Corbin Frisvold
# Project Euler Problem 1
# 11/4/19
sum = 0
for i in range(1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i
print(sum)