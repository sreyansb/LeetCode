#attempt1: MAde a formula but wrong assumptions
#took help from channa sir
class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        a=minutesToTest//minutesToDie+1
        b=a
        index=0
        while(a<buckets):
            index+=1
            a*=b
            print(a)
        return index
obj=Solution()
obj.poorPigs(1000,15,15)
        
        
