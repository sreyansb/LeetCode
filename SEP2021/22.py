#attempt3:AC
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        finlist=[]
        for i in arr:
            if len(set(i))==len(i):
                finlist.append(set(i))
        maxl=[0]
        n=len(finlist)
        
        def recurse(index,curwindow):
            #print(curwindow)
            
            maxl[0]=max(maxl[0],len(curwindow))
            leng=len(curwindow)
            for i in range(index+1,n):
                if len(finlist[i]|curwindow)==len(finlist[i])+leng:
                    recurse(i,curwindow|finlist[i])
        maxlen=0
        for i in range(n):          
            recurse(i,finlist[i])
            maxlen=max(maxlen,len(finlist[i]))
        return max(maxl[0],maxlen)

#attempt2: RunTime Error because finlist can be empty and hence the last max
#condition on the set throws an error
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        finlist=[]
        for i in arr:
            if len(set(i))==len(i):
                finlist.append(set(i))
        maxl=[0]
        n=len(finlist)
        
        def recurse(index,curwindow):
            #print(curwindow)
            
            maxl[0]=max(maxl[0],len(curwindow))
            leng=len(curwindow)
            for i in range(index+1,n):
                if len(finlist[i]|curwindow)==len(finlist[i])+leng:
                    recurse(i,curwindow|finlist[i])
        for i in range(n):          
            recurse(i,finlist[i])
        return max(maxl[0],max([len(i) for i in finlist]))
''' 

#attempt1: WA because didn't take care of a corner case in the recursion condition
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        finlist=[]
        for i in arr:
            if len(set(i))==len(i):
                finlist.append(set(i))
        maxl=[0]
        n=len(finlist)
        
        def recurse(index,curwindow):
            if index>=n:
                maxl[0]=max(maxl[0],len(curwindow))
                return
            leng=len(curwindow)
            for i in range(index+1,n):
                if len(finlist[i]|curwindow)==len(finlist[i])+leng:
                    recurse(i+1,curwindow|finlist[i])
                    #should've called with i
        for i in range(n):          
            recurse(i,finlist[i])
        return max(maxl[0],max([len(i) for i in finlist]))
'''