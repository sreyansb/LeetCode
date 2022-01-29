#attempt3: TOOK HELP:Previous submission
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        elementstor=[]
        elementstol=[]
        stackr=[]
        stackl=[]
        for i in range(len(heights)-1,-1,-1):
            while(stackr and heights[stackr[-1]]>=heights[i]):
                stackr.pop()
            if not stackr:
                stackr.append(i)
                elementstor.append(len(heights)-i)
            else:
                elementstor.append(stackr[-1]-i)
                stackr.append(i)
        elementstor=elementstor[::-1]
        for i in range(0,len(heights)):
            while(stackl and heights[stackl[-1]]>=heights[i]):
                stackl.pop()
            if not stackl:
                stackl.append(i)
                elementstol.append(i+1)
            else:
                elementstol.append(i-stackl[-1])
                stackl.append(i)
        maxi=0
        for i in range(len(heights)):
            maxi=max(maxi,heights[i]*(elementstor[i]+elementstol[i]-1))
        return maxi
            
                
        
                    
        
'''

#attempt2: WA because of maxarea = max(maxarea,stack[-1][0]*(n-i)) as
#stack[-1][0] could be the highgest element of the elements remaining in the stack
#and hence won't apply to entire n-i elements
'''
class Solution:
    def largestRectangleArea(self, heights):
        maxarea = heights[-1]
        n = len(heights)
        stack = [(heights[-1],n-1)]
        
        for i in range(n-2,-1,-1):
            ele = heights[i]
            maxarea = max(maxarea,heights[i])
            while(stack and stack[-1][0]>=ele):
                maxarea = max(maxarea,ele*(stack[-1][-1]-i+1))
                stack.pop()
            if stack:
                maxarea = max(maxarea,stack[-1][0]*(n-i))
            if not(stack) or (stack and stack[-1][0]!=ele):
                stack.append((ele,i))
            #print(maxarea,stack)
        return maxarea
            
'''

#attempt1: Trying segtree : TLE 90/96 because of O(n*(log n)^2) and n is 10^5
#idea is to create a segment tree such that it stores the index of the min element in a given range a,b
#and query on the left of the minimum element until current index is met
"""
class Solution:
    def largestRectangleArea(self, heights):
        '''
        maxarea = heights[-1]
        n = len(heights)
        heap = [(heights[-1],n-1)]
        heapify(heap)
        for i in range(n-2,-1,-1):
            heappush(heap,(heights[i],i))
            smallele,index = heap[0]
            maxarea = max(maxarea,smallele*(n-i))
        '''
        n = len(heights)
        segtree = [0 for i in range(4*n)]
        def createsegtree(segtreeindex,lowindex,highindex):
            if lowindex>highindex:
                return
            if lowindex==highindex:
                segtree[segtreeindex] = (heights[lowindex],lowindex)
                return
            mid = (lowindex+highindex)//2
            child = 2*segtreeindex+1
            createsegtree(child,lowindex,mid)
            createsegtree(child+1,mid+1,highindex)
            if segtree[child][0]<=segtree[child+1][0]:
                segtree[segtreeindex] = segtree[child]
            else:
                segtree[segtreeindex] = segtree[child+1]
        
        createsegtree(0,0,n-1)
        
        def query(cursegindex,reqdl,reqdr,segl,segr):
            #print(cursegindex,reqdl,reqdr,segl,segr)
            if segl>reqdr or segr<reqdl:
                return (float('inf'),n)
            if reqdl<=segl<=reqdr and reqdl<=segr<=reqdr:
                return segtree[cursegindex]
            mid = (segl+segr)//2
            child = 2*cursegindex+1
            minl = query(child,reqdl,reqdr,segl,mid)
            minr = query(child+1,reqdl,reqdr,1+mid,segr)
            if minl[0]<=minr[0]:
                return minl
            elif minr[0]<minl[0]:
                return minr
        #print(query(0,0,0,0,n-1))

        
        maxarea = heights[-1]
        for i in range(n):
            prevpos = n-1
            maxarea = max(maxarea,heights[i])
            while(True):
                ansq = query(0,i,prevpos,0,n-1)
                maxarea = max(maxarea,ansq[0]*(prevpos-i+1))
                #print(i,prevpos,ansq)
                if ansq[1]==i:
                    break
                prevpos = ansq[1]-1
        return maxarea
              
a = Solution()
print(a.largestRectangleArea([2,1,5,6,2,3]))
"""
