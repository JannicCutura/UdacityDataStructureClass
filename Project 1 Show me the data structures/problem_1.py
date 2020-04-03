"""
I went in detail over this solution  https://knowledge.udacity.com/questions/93168 but then built my own code from scratch
I remember the basic structure was:
 - DoubleNode class to build a doubleLinkedList
 - Use a dictionary to track where a given key in the list is, so you can remove it in O(1) and do not have to loop
"""


class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# lets first test the doublenode class a bit
node1 = DoubleNode(1,1)
node2 = DoubleNode(2,3)
node1.key
node2.value
#ok works as expected



class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def preprend(self, node):

        # if llist is empty
        if self.head is None:
            self.head = node
            self.tail = node

        # if head is the node element, just ignore it
        elif self.head == node:
            return

        # if the list has one element, then move the tail forward
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail



        # if the list has multiple elements
        else:
            if self.tail == node:
                self.remove_tail()
            # "take one out in the middle"
            if node.prev is not None:
                node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev

            # "and add it in the front"
            node.next = self.head
            self.head.prev = node
            self.head = node


    def remove_tail(self):
        if self.tail is None:
            return

        if self.tail == self.head:
            self.head = None
            self.tail = None
            return

        else:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail

    def __str__(self):
        if self.head is None:
            return "List is empty"
        else:
            cur_node = self.head
            to_display = "Last added  -->  "
            to_display = to_display + str(cur_node.value)
            while cur_node.next:
                to_display = to_display+  " | " + str(cur_node.next.value)
                cur_node = cur_node.next
            to_display = to_display  + " <-- next to drop "

        return to_display


llist = DoubleLinkedList()
llist.preprend(node1)
llist.preprend(node2)
print(llist)
#ok works as expected
del node1, node2, llist


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.num_elements = 0
        self.capacity = capacity
        self.hash = dict()
        self.llist = DoubleLinkedList()

    def get(self, key):
        if key not in self.hash:
            return -1

        self.llist.preprend(self.hash[key])
        return self.hash[key].value


    def set(self, key, value):
        if key in self.hash:
            self.llist.preprend(self.hash[key])
            self.hash[key] = value ## in case a different value is associated with the key

        else:
            if self.num_elements == self.capacity:
                ## here we need to remove the tail
                del self.hash[self.llist.tail.key]
                self.llist.remove_tail()
            else:
                ## here we can just add
                self.num_elements +=1

            self.hash.update({key:DoubleNode(key, value)})

            self.llist.preprend(self.hash[key])

    def __repr__(self):
        return str(self.llist)

    def get_hash(self):
        return {k: str(v) for k, v in self.hash.items()}

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry



## okay these all work as expected, here are some more for me:

print("This is the cache:")
print(our_cache)
print("and here we see the cash with the pointers to where the Nodes are in memory (0x000121245... notation)")
print(our_cache.hash)
print("lets dig a bit. Get the first Node")
node1 = our_cache.hash[1]
print("Print, key, value and the prev attribute:")
node1.key
node1.value
print(node1.prev)
print("if the implemntation is correct, our_cache.hash[2]  should be  our_cache.hash[1].prev. Is it?")
node1.prev == our_cache.hash[2]
print("and vice verse, our_cache.hash[2].next  should be  our_cache.hash[1]. Is it?")
node1 == our_cache.hash[2].next






