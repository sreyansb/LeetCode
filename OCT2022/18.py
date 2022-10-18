#attempt1:
class Solution:
    def countAndSay(self, n: int) -> str:
        curStack = [("1",1)]
        di = {"one":1,"two":2,"three":3, "four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}
        dinumber = {di[key]:key for key in di}
        while(n > 1):
            nextStack = []
            newString = "".join([str(i[1])+i[0] for i in curStack])
            pastChar = newString[0]
            count = 1
            for nextChar in newString[1:]:
                if nextChar != pastChar:
                    nextStack.append((pastChar,count))
                    count = 0
                pastChar = nextChar
                count += 1
            nextStack.append((pastChar,count))
            curStack = nextStack
            n -= 1
        return "".join([i[1]*i[0] for i in curStack])
