"""
Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""


def get_min_max(ints):
    if len(ints) == 0:
        print("Error: The input is empty")
        return
    tmp = ints

    min = ints[0]
    max =ints[0]
    for number in ints:
        if not str(number).isdigit():
            print("Error: The input must only contain numbers")
            return
        if number < min:
            min = number
        elif number > max:
            max = number
        else:
            pass
    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# Test Case 1: From the problem set
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Test Case 2:
l = []
get_min_max(l)
# Error: The input is empty



# Test Case 3:
l = [1,2,"a"]
get_min_max(l)
# Error: The input must only contain numbers


# Test Case 4:
l = [2,2,2]
print(get_min_max(l))
# (2, 2)




