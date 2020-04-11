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

def unique_of_lllist(llist):
    if llist.head is None:
        return None

    # store all unique values to check whether we had them in O(1) time
    hash = dict()

    cur_node = llist.head
    unique_llist = LinkedList()
    while cur_node:
        #print("The llist is:")
        #print(llist)
        #print("and we are at:")
        #print(cur_node.value)
        #print(hash)
        if cur_node.value not in hash:
            #print("Not in hash yet, add {} it to hash".format(cur_node.value))
            hash[cur_node.value] = cur_node.value
            #print("Not in newlist yet, add {} it to newlist".format(cur_node.value))
            unique_llist.append(cur_node.value)
        else:
            #print("Already in hash, next node")
            pass
        cur_node = cur_node.next
        #print(cur_node is None)
        #print("")
    return  hash, unique_llist


def union(llist_1, llist_2):
    union_as_set = set()

    # if either list is empty, return the other one
    if llist_1.head == None:
        return unique_of_lllist(llist_2)[1]
    elif llist_2.head == None:
        return  unique_of_lllist(llist_1)[1]

    else: # both lists have elements
    # lets first get unique values for each list
        hash1, llist_1 = unique_of_lllist(llist_1)
        hash2, llist_2 = unique_of_lllist(llist_2)
        for key in hash2:
            if key in hash1:
                #print("Already in list")
                pass
            else:
                hash1[key] = key
                llist_1.append(key)

    return llist_1



def intersection(llist_1, llist_2):
    # if either list is empty, return an empty LinkedList()
    if llist_1.head == None:
        return LinkedList()
    elif llist_2.head == None:
        return LinkedList()
    else:  # both lists have elements
        # lets first get unique values for each list
        hash1, llist_1 = unique_of_lllist(llist_1)
        hash2, llist_2 = unique_of_lllist(llist_2)
        intersection_list = LinkedList()
        for key in hash2:
            if key in hash1:
                intersection_list.append(key)
            else:
                #print("Not in the other list")
                pass

    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]



for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(linked_list_1)
print(linked_list_2)

# test my unique function first
print(unique_of_lllist(linked_list_1)[1])
#3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 ->
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
#3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_3,linked_list_4))
#



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
#




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
# A -> 1 -> 3 -> 9 -> 1 -> 7 -> 8 -> 11 -> 21 ->
print (intersection(linked_list_7,linked_list_8))
# 9
