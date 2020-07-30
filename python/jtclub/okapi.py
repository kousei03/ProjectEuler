def okapi():
    rolls = str(raw_input("Enter dice rolls: "))
    x, y, z = int(rolls[0]), int(rolls[1]), int(rolls[2])
    if x == y and y == z:
        print("The payout is $", x+y+z, ".")
    elif x == y:
        print("The payout is $", x+y, ".")
    elif y == z:
        print("The payout is $", y+z, ".")
    elif x == z:
        print("The payout is $", x+z, ".")
    else:
        print("The payout is $0.")