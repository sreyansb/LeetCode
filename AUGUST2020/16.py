from math import inf
#took help from a video
#we are trying to maximise the first buy and sell because that is what
#will give the biggest value.
#then we will go for the second buying and selling
#fb will represent -> first buy similarily sb
#fs -> first sell
#Assume we have 0 cash.
#We buy first => -arr[i] will be the value of fb
#we can sell only after buying -> fs=fb+arr[i]
#similarily other stuff
class Solution:
    def maxProfit(self, a: List[int]) -> int:
        if not(a):
            return 0
        fb=-inf#maximise first buy
        fs=-inf#maximise first sell
        sb=-inf#maximise second buy
        ss=-inf#maximise second sell
        for i in a:
            fb=max(fb,-i)
            fs=max(fs,fb+i)
            sb=max(sb,fs-i)
            ss=max(ss,sb+i)
        return ss
