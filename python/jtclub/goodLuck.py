# Corbin Frisvold
# Weekly Challenge 3 Problem 1
# 10/18/19
import time

k = str(raw_input("Enter a 3-Digit Number: "))
t0 = time.time()
if len(k) < 3:
    k = k.zfill(3)
K_List = [item for item in k]
K_List.sort()
x = K_List[0]+K_List[1]+K_List[2] #Ascending K
y = K_List[-1]+K_List[-2]+K_List[-3] #Descending K
z = K_List[1]+K_List[1]+K_List[1] #Median 3 times
luck = int(x)+int(y)-int(z)
print("Good luck:", luck)
t1 = time.time()
print(t1-t0)