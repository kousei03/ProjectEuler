# Corbin Frisvold
# Bloomsburg 2019 Problem 2: Euclidean Cake

c = 1
dim = raw_input("Enter dimensions of cake: ")
dim = dim.split(" ")
dim[0], dim[1] = int(dim[0]), int(dim[1])
dim.sort()
while dim[0] > 0:
    print("Cake on day ", c, ":", dim[0], "X", dim[1])
    c += 1
    dim[1] = dim[1] - dim[0]
    dim.sort()
print("Cake on day ", c, ": gone")