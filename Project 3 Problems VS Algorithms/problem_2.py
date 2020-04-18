"""
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
"""

def rotated_array_search(input_list, number):

    if len(input_list) == 0:
        print("The input list is empty")
        return

    if not isinstance(number, int):
        print("Number to look for is not an integer")
        return

    start_index = 0
    end_index = len(input_list) - 1

    while start_index <= end_index:
        #print("")
        #print(input_list[start_index:end_index])
        mid_index = (start_index + end_index) // 2  # integer division in Python 3

        mid_element = input_list[mid_index]

        if number == mid_element:  # we have found the element
            return mid_index

        elif input_list[start_index] <= number <= input_list[mid_index-1]:
            end_index = mid_index - 1  # we will only search in the left half

        elif input_list[mid_index+1] <= number <= input_list[end_index]:
            start_index = mid_index + 1  # we will search only in the right half

        elif input_list[start_index] > input_list[mid_index] and not input_list[mid_index+1] <= number <= input_list[end_index]:
            end_index = mid_index - 1  # we will only search in the left half

        elif input_list[mid_index] > input_list[end_index] and not input_list[start_index] <= number <= input_list[mid_index-1]:
            start_index = mid_index + 1  # we will search only in the right half
        else:
            return -1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


## Test Case 1: From the probem set
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[2, 3, 4, 5, 6, 7, 8, 9, 1], 1])



## Test Case 2: Empty input
rotated_array_search([], 1)
# The input list is empty


## Test Case 3: Looking for non-integer
rotated_array_search([2, 3, 4, 5, 6, 7, 8, 9, 1], "a")
# Number to look for is not an integer

## test case4 : More Cases from the reviewer

test_function([[10, 1, 2, 3, 4], 6])
test_function([[1, 2, 3, 4], 6])