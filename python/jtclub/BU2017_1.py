# Corbin Frisvold Weekly Challenge 1 Solution
# 2017 BU Problem #1 Speeding Ticket
# 10.1.19

def ticket():
    fee = 0
    new_mph = 0
    mph = int(input("\nSpeed in MPH over the limit: "))
    base = int(input("\nBase fee: "))
    quadruple = base*4
    double = base*2
    if mph > 15:
        fee += (mph-15)*quadruple
        mph = 15
    if mph > 6 and mph <= 15:
        fee += (mph-5)*double
        mph = 5
    if mph <= 5:
        fee += mph*base
    return("\nCost of ticket: $", fee)