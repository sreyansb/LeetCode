class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res=[]
        self.string=characters
        length=len(characters)
        for i in range(1,2**length):
            j=bin(i)[2:]
            if j.count("1")==combinationLength:
                if len(j)<length:
                    self.res.append("0"*(length-len(j))+j)
                else:
                    self.res.append(j)
        self.res.reverse()
        self.index=0
            

    def next(self) -> str:
        s=""
        for i in range(len(self.string)):
            s+=self.string[i] if self.res[self.index][i]=="1" else ""
        self.index+=1
        return s

    def hasNext(self) -> bool:
        return self.index!=len(self.res)
        
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
