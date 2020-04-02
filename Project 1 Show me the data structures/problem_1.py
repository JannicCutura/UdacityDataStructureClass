# solution partially adapted from: https://knowledge.udacity.com/questions/93168
## from the forum
class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeLinks(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, node):
        # if the most recent element is used again, don't do anything
        if self.head == node:
            return

        # if the list is empty, add new tail and head
        elif self.head is None:
            self.head = node
            self.tail = node

        # if the list has only one element, (head == tail)
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail

        # any other case, i.e. at least two elements
        else:
            # if the tail is the same node, remove it
            if self.tail == node:
                self.removeTail()

            node.removeLinks()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def __str__(self):
        to_return = 'Most Recent '
        curr = self.head
        while curr != None:
            to_return += str(curr)
            if curr.next != None:
                to_return += ' <--> '
            curr = curr.next
        return to_return + ' Least Recent'


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hash = {}
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.hash:
            return -1
        # Update the most recent item
        self.updateMostRecent(self.hash[key])
        return self.hash[key].value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.hash:
            if self.currentSize == self.capacity:
                self.removeLeastRecent()
            else:
                self.currentSize += 1
            self.hash[key] = DoubleNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.hash[key])

    def removeLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.hash[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.prepend(node)

    def replaceKey(self, key, value):
        if key not in self.hash:
            raise Exception('The key to be replaced is not in the cache - the action cannot be completed.')
        self.hash[key].value = value

    def __repr__(self):
        return str(self.listOfMostRecent)

    def get_hash(self):
        return {k: str(v) for k, v in self.hash.items()}


our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print()
print('Cache after adding 1, 2, 3 and 4 in that order: ')
print(our_cache)
print('Hash status:', our_cache.get_hash())
print()
print('our_cache.get(1) returns: ', our_cache.get(1))
print('Cache after getting 1.')
print(our_cache)
print('Hash status:', our_cache.get_hash())
print()
print('our_cache.get(2) returns: ', our_cache.get(2))
print('Cache after getting 2.')
print(our_cache)
print('Hash status:', our_cache.get_hash())
print()
print('our_cache.get(9) returns: ', our_cache.get(9))
print('Cache after getting 9.')
print(our_cache)
print('Hash status:', our_cache.get_hash())

# Let's add some more items to see if this works right
our_cache.set(5, 5)
print('Cache after adding 5:\n', our_cache)
print('Hash status:', our_cache.get_hash())
print(our_cache)
print()
our_cache.set(6, 6)
print('Cache after adding 6:\n', our_cache)
print('Hash status:', our_cache.get_hash())
print()
our_cache.set(7, 7)
print('Cache after adding 7:\n', our_cache)
print('Hash status:', our_cache.get_hash())

print('our_cache.get(3) returns: ', our_cache.get(3))
print('Cache after adding get(3):\n', our_cache)
print('Hash status:', our_cache.get_hash())
{k: str(v) for k, v in our_cache.hash.items()}

