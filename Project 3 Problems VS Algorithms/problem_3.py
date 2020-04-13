"""
Rearrange Array Elements so as to form two number such that their sum is maximum.
 Return these two numbers. You can assume that all array elements are in the range [0, 9].
  The number of digits in both the numbers cannot differ by more than 1.
  You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""


def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)

def quicksort(items):
    sort_all(items, 0, len(items) - 1)




def rearrange_digits(input_list):
    if len(input_list) < 2:
        print("Input at least two numbers!")
        return

    quicksort(input_list) # this takes O(n log(n)) time
    larger_number = ""
    smaller_number = ""
    length = len(input_list)-1


    for i in range(0,length+1): ## this takes O(n)
        if i % 2 == 1:
             smaller_number = smaller_number + str(input_list[length - i])
        else:
            larger_number = larger_number +str(input_list[length - i])
    return [int(larger_number), int(smaller_number)]



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# test case 1: From the problem set
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# test case 2: Empty input
rearrange_digits([])
# Input at least two numbers!


# test case 3: Trivial input
test_function([[1, 1], [1, 1]])
test_function([[0, 0], [0, 0]])