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

        else:
            newblock = Block(data,  timestamp=current_gmt)
            previous_hash = self.head.hash
            oldhead = self.head
            self.head = newblock
            self.head.previous_hash = previous_hash
            newblock.next = oldhead

    def __str__(self):
        if self.head is None:
            return "This blockchain is empty"
        else:
            return "The head of the chain is {}".format(self.head.data)





## test cases
# initialize blockchain
mychain = BlockChain()

print(mychain)
#This blockchain is empty

mychain.add2chain(1)
print(mychain)
#The head of the chain is 1

mychain.add2chain(3)
mychain.add2chain(5)

# test whether hash codes work and link corretly
print("Previous Hash of head is equal current has of previous block? {}".format(mychain.head.previous_hash ==mychain.head.next.hash))
