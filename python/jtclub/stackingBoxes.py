# Corbin Frisvold
# Bloomsburg 2018 Problem 4: Stacking Boxes
boxes = int(input("How many boxes? "))
stack1 = 0
stack2 = 0
stack3 = 0
stack4 = 0
for i in range(0,boxes):
    if (2*i)+1 <= boxes:
        stack1 += 1
        boxes -= (2*i)+1
for i in range(0,boxes):
    if (2*i)+1 <= boxes:
        stack2 += 1
        boxes -= (2*i)+1
for i in range(0,boxes):
    if (2*i)+1 <= boxes:
        stack3 += 1
        boxes -= (2*i)+1
for i in range(0,boxes):
    if (2*i)+1 <= boxes:
        stack4 += 1
        boxes -= (2*i)+1
        
if stack1>0:
    print("Height of 1st stack: ", stack1)
if stack2>0:
    print("Height of 2nd stack: ", stack2)
if stack3>0:
    print("Height of 3rd stack: ", stack3)
if stack4>0:
    print("Height of 4th stack: ", stack4)
