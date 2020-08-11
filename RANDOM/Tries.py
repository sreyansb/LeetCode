#fast and less memory consumptions
class Trie:
    def __init__(self):
        self.root={}

    def insert(self, word):
        root=self.root
        for index in word:
            if index not in root:
                root[index]={}
            root=root[index]
        root['$']=1
        print(self.root)

    def search(self, word):
        root=self.root
        for index in word:
            if index in root:
                root=root[index]
            else:
                return False
        return root and '$' in root
        

    def startsWith(self, word):
        root=self.root
        for index in word:
            if index in root:
                root=root[index]
            else:
                return False
        return True if root else False
#Attempt 1
"""
class Node:
        def __init__(self):
            self.children={}
            self.terminateshere=False
class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word):
        root=self.root
        for index in word:
            if index not in root.children:
                root.children[index]=Node()
            root=root.children[index]
        root.terminateshere=True

    def search(self, word):
        root=self.root
        for index in word:
            if index in root.children:
                root=root.children[index]
            else:
                return False
        return root and root.terminateshere
        

    def startsWith(self, word):
        root=self.root
        for index in word:
            if index in root.children:
                root=root.children[index]
            else:
                return False
        return True if root else False
"""

# Your Trie object will be instantiated and called as such:
obj = Trie()
word="here"
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
prefix="he"
param_3 = obj.startsWith(prefix)
print(param_3)

