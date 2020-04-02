import hashlib
import time
from time import gmtime, strftime
      
      
class Block:

    def __init__(self, data, previous_hash, timestamp ):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self,timestamp, data, previous_hash):
        sha = hashlib.sha256()
        hash_str = str(timestamp)+str(data)+str(previous_hash)
        hash_str = hash_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add2chain(self, data, previous_hash):
        current_gmt = gmtime()
        if self.head is None:
            self.head = Block(data, previous_hash, timestamp=current_gmt)
            self.tail = Block(data, previous_hash, timestamp=current_gmt)
        else:
            newblock =  Block(data, previous_hash, timestamp=current_gmt)
            oldhead = self.head
            self.head = newblock
            newblock.next = oldhead


mychain = BlockChain()

print(mychain.head)
mychain.add2chain(1,2)
data = 1
previous_hash = 2

Block(data, previous_hash, timestamp=current_gmt)


print()