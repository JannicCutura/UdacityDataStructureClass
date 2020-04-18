"""
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:

"""


def binary_search_for_the_square(target):
    start_index = 0
    end_index = target
    while start_index < end_index:
        mid_index = (start_index + end_index) // 2

        if mid_index**2 <= target and (mid_index+1)**2 > target:
            return mid_index
        if mid_index**2 > target:
            end_index = mid_index
        else:
            start_index = mid_index
    return -1


def sqrt(number):
    if not isinstance(number, int):
        print("You have not entered an integer")
        return
    if number < 0 :
        print("negative Numbers don't have (real) roots")
        return
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number > 1:
        result =  binary_search_for_the_square(number)
        return result




## test Case 1: From the problem set
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


## test case 2: Enter a non-integer
sqrt("a")
# You have not entered an integer
sqrt(1.4)
# You have not entered an integer

## test case 3: Enter a really huge number:
sqrt(100000000)
# 10000
# slows down quite a bit. This is a memory issue, I can see my RAM spike.

## test case 4: negative integer
sqrt(-9)






