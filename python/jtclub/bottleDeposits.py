# Corbin Frisvold Challenge Problem 1
smallContainers = int(raw_input("How many small containers? "))
largeContainers = int(raw_input("How many large containers? "))
cash = (smallContainers*0.10)  + (largeContainers*0.25)
cash = "%0.2f" % cash
print("You will get ", cash, "$")