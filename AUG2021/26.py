#attempt6: TOOK HELP(Copied)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        k=preorder.split(",")
        curcount=1
        for i in k:
            if curcount==0:
                return False
            curcount+=1 if i!="#" else -1
            
        return curcount==0        

#attempt4 and 5: WA TOOK HELP, the difference should be checked at each index
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        k=preorder.split(",")
        curcount=1
        for i in k:
            curcount+=1 if i!="#" else -1
        return curcount==0
'''


#attempt1,2 and 3: WA Wrong implementation : Was just trying to count number of leaves and non
#leaves. Overall idea is right but should be done at every index of the string and 
# not just at the end
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        k=preorder.split(",")
        hashcount,n=k.count("#"),len(k)
        if n>1 and k[0]=='#':
            return False
        if n>1 and (k[-1]!='#' or k[-2]!='#'):
            return False
        return hashcount-1==n-hashcount        
''' 