class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def llist2list(llist):
    '''
    Takes a linkedlist and returns a python list
    '''
    pythonlist = []

    if llist.head is None:
        return []

    node  =llist.head
    while node:
        pythonlist.append(node.value)
        node = node.next

    return pythonlist


def union(llist_1, llist_2):
    return set(llist2list(llist_1)).union(set(llist2list(llist_2)))

def intersection(llist_1, llist_2):
    # Your Solution Here
    return set(llist2list(llist_1)).intersection(set(llist2list(llist_2)))


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]



for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)



print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))




# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# {1, 21, 7, 8, 9, 11}
print (intersection(linked_list_5,linked_list_6))
# set()




# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = ["A","1",3,9]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
# {1, 3, 'A', 7, 8, 9, 11, '1', 21}
print (intersection(linked_list_7,linked_list_8))
# {9}
