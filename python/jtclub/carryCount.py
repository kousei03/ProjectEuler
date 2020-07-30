# Corbin Frisvold
# Bloomsburg 2018 Problem 3 Carry Counts
# 10/28/19

def carrycount():
    carries = 0
    extra = 0
    int1 = str(raw_input("Enter two positive integers to be added: "))
    int2 = str(raw_input())
    ints = [int1, int2]
    length = len(max(ints))
    add1 = int1.zfill(length)
    add2 = int2.zfill(length)
    for i in range(length):
        if int(add1[-(i+1)]) + int(add2[-(i+1)]) + extra >=10:
            # print(add1[-(i+1)], " and ", add2[-(i+1)], " and ", extra, " carry")
            extra = 1
            carries += 1
        elif int(add1[-(i+1)]) + int(add2[-(i+1)]) + extra <= 9:
            # print(add1[-(i+1)], " and ", add2[-(i+1)], " and ", extra, " do not carry")
            extra = 0
    if carries == 1:
        print("There will be 1 carry.")
    elif carries <= 0:
        print("There will be no carries.")
    else:
        print("There will be ", carries, " carries")