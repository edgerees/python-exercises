# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(numbers, multiplier):
    multiples = []
    for number in numbers:
        multiples.append(number * multiplier)
    print(multiples)

# LAMBDA VERSION (FROM JENNY'S CODE) >> lamdba = Python's version of an anonymous function
# def multiply_by(arr, num):
#     return list(map(lambda x: x*num, arr))

multiply_by([1, 2, 3], 5)