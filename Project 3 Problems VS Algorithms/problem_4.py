"""
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:

"""


print("Please see my comments in the explanation!")



## my own solution
def my_own_sort_012(input_list):
    if input_list == []:
        print("You inputted and empty list")
        return
    zeros = 0
    ones = 0
    twos = 0
    for number in input_list:
        if number == 0:
            zeros +=1
        elif number == 1:
            ones +=1
        elif number == 2:
            twos +=1
        else:
            print("Error: You have inserted numbers outside [0,1,2]")
            return
    result = zeros*[0]
    result.extend(ones*[1])
    result.extend(twos*[2])
    return result


def test_function(test_case):
    sorted_array = my_own_sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


## test case 1: From the problem set
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

## test case 2:  Wrong input
my_own_sort_012([1,0,2,"a"])
my_own_sort_012([1,1.2,0,2,0])
#Error: You have inserted numbers outside [0,1,2]


## test case 3:  no input
my_own_sort_012([])
#You inputted and empty list



