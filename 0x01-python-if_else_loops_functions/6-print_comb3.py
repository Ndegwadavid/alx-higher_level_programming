#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i != j and not (i == 0 and j == 1):
            print("{:02d}, {:02d}".format(i, j), end=", ")
print("{:02d}".format(9))
