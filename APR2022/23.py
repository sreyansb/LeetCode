#attempt1:
class Codec:
    def __init__(self):
        self.long_to_short = {}
        self.index = 1
        self.short_to_long = {}
        self.base_website = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        shorter_website = self.base_website + str(self.index)
        self.long_to_short[longUrl] = shorter_website
        self.short_to_long[shorter_website] = longUrl
        self.index += 1      
        return shorter_website
        
    def decode(self, shortUrl: str) -> str:
        return self.short_to_long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
