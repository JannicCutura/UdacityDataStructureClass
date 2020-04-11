

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        self.to_return = set()

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):

        if self.children:

            for char, node in self.children.items():

                if node.is_word:
                    self.to_return.add(suffix + char)

                node.suffixes(suffix + char)

        return list(self.to_return)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

Mynode= TrieNode()
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



#%%
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');







