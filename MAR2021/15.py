#attempt1:added an init function
#map each url to a number
'''
class Codec:
    def __init__(self):
        self.count=0
        self.di={}
        
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.di:
            self.di[str(self.count)]=longUrl
            self.count+=1
        return str(self.count-1)
        
    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.di:
            return self.di[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
'''
