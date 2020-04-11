import hashlib
import time
from time import gmtime, strftime
      
      
class Block:

    def __init__(self, data, timestamp):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp)+str(self.data)+str(self.previous_hash)
        hash_str = hash_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add2chain(self, data):
        current_gmt = gmtime()
        if self.head is None:
            previous_hash = None  # first block has no previous hash
            self.head = Block(data,  timestamp = current_gmt)
            self.tail = self.head

        elif self.head is self.tail:
            newblock = Block(data, timestamp=current_gmt)
            newblock.previous_hash = self.head.hash
            self.head.next = newblock
            self.tail= newblock


        else:
            newblock = Block(data,  timestamp=current_gmt)
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            newblock.previous_hash =cur_node.hash
            cur_node.next = newblock
            self.tail= newblock

        self.size +=1


    def __str__(self):
        if self.head is None:
            return "This blockchain is empty"
        else:
            cur_node = self.head
            to_print = "Head is "
            while cur_node:
                to_print = to_print + str(cur_node.data) + " --> "
                cur_node = cur_node.next
            to_print = to_print[:-5]
            to_print = to_print+" is Tail"
            return to_print





## Test Case 1: Regular case
# initialize blockchain
mychain = BlockChain()

print(mychain)
#This blockchain is empty

mychain.add2chain(1)
print(mychain)
#Head is 1 is Tail

mychain.add2chain(3)
print(mychain)
# Head is 1 --> 3 is Tail
mychain.add2chain(5)
print(mychain)
# Head is 1 --> 3 --> 5 is Tail


## Test case 2: Suggested by my previous reviewer to check order
mychain = BlockChain()
mychain.add2chain(1)
mychain.add2chain(3)
mychain.add2chain(5)

a = mychain.head
while a:
    print(a.data)
    a=a.next
#1
#3
#5
# Note: this is what they wanted.


## Test case 3: Add a non-sense element
mychain = BlockChain()
mychain.add2chain(1)
mychain.add2chain(3)
mychain.add2chain(5)
mychain.add2chain(None)
# expect no errors even though we added None

## Test case 4: Forgot the input
try:
    mychain.add2chain()
except:
    print("No input provided")
#"No input provided"


#  Test case 5: Check the hash references
print(mychain)
print("Previous Hash of head is equal current has of previous block?")
a = mychain.head
runner = 1
while a.next:
    print("At node number {}, is hash equal to next.previous hash?".format(runner))
    print(a.hash == a.next.previous_hash)
    a=a.next
    runner +=1


