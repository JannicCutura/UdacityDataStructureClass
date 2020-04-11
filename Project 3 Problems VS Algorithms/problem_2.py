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
    ## this takes O(lon(n)) time and will be helpful
    def recursive_binary_search(target, source, left=0):
        if len(source) == 0:
            return None
        center = (len(source) - 1) // 2
        #print(center)
        if source[center] == target:
            return center + left
        elif source[center] < target:
            return recursive_binary_search(target, source[center + 1:], left + center + 1)
        else:
            return recursive_binary_search(target, source[:center], left)
    #print("")
    if len(input_list) == 0:
        print("The input list is empty")
        return

    if not isinstance(number, int):
        print("Number to look for is not an integer")
        return

    try:
        center = (len(input_list) - 1) // 2
        #print("The center index is {} and its value is {}".format(center, input_list[center]))
        if input_list[center] == number:
            return center

        ## the reappended part is left of the middle
        # [7, 8, 1, 2, 3, 4, 5, 6]
        #print(input_list)
        if input_list[0] > input_list[center] and input_list[center + 1] < input_list[len(input_list )-1]:
            #print("appended part is left of middle")
            #print(" - check if target number in regular part")
            if number > input_list[center] and number <= input_list[-1]: ## the target number is in the right non-weird properly sorted part
                #print("Target number {} is in the right part (regular part), start recursive binary search".format(number))
                #print( input_list[center+1:])
                return center +1 +recursive_binary_search(number, input_list[center+1:], left=0)
            else:
                #print("Target number {} is in the left part, re-start new search".format(number))
                #print(input_list[0:center])
                return rotated_array_search(input_list[0:center], number)

        else: ## the reappended part is right of middle, i.e.
            # [3, 4, 5, 6, 7, 8, 1, 2]
            #print("appended part is right of middle")
            if number < input_list[center] and number >= input_list[0]: ## the target number is in the right non-weird properly sorted part
                #print("Target number {} is in the left part,start recursive binary search on:".format(number))
                #print(input_list[:center])
                return  recursive_binary_search(number, input_list[:center], left=0)
            else:
                #print("Target number {} is in the right part, re-start new search on:".format(number))
                #print(input_list[center+1:])
                #print(input_list[center+1:] == [])
                return center + 1 + rotated_array_search(input_list[center+1:], number)
    except TypeError:
        #print("Number not found")
        return -3



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


## Test Case 3: Empty input
rotated_array_search([2, 3, 4, 5, 6, 7, 8, 9, 1], "a")
# Number to look for is not an integer

