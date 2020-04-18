


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





class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        results =[]

        for values in self.children:
            if self.children[values].children:
                results.extend(self.children[values].suffixes(suffix + values))
            elif values == '\x00':
                results .append(suffix)
        return  results



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word+"\0")


MyTrie2 = Trie()
for word in wordList:
    MyTrie2.insert(word)





def f(prefix):
    print(prefix)
    if prefix != '':
        print("prefix not empty")
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f("a")










