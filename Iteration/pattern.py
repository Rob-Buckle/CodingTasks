# Creating an inverted triangle shape using a for loop
# By defining the peak or widest part of the triange
# This makes it easier to create and if and else condition

peak = 5
height = 9

for across in range(1, height + 1):
    if across <= peak:
        print("*" * across)
    else:
        print("*" * (height - across + 1))

