w#attempt1:
# need to store self.keys as: if a key is reinitialized we need to only update the difference
#if a prefix doesn't appear return a 0
class MapSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie={}
        self.keys={}
        

    def insert(self, key: str, val: int) -> None:
        k=self.trie
        if key in self.keys:
            val=val-self.keys[key]
            self.keys[key]+=val
        else:
            self.keys[key]=val
        for i in key:
            if i not in k:
                k[i]={}
                k[i]["val"]=0
            k[i]["val"]+=val
            k=k[i]        

    def sum(self, prefix: str) -> int:
        ans=0
        k=self.trie
        for i in prefix:
            if i not in k:
                return 0
            k=k[i]
        return k["val"]  
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)