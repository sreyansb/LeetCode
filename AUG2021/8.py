#attempt4: JUST COPIED 5 hours into the problem!
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) # dimension 
        # mapping from value to index 
        mp = {} 
        for i in range(m):
            for j in range(n): 
                mp.setdefault(matrix[i][j], []).append((i, j))
        
        def find(p):
            """Find root of p."""
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]
        
        rank = [0]*(m+n)
        ans = [[0]*n for _ in range(m)]
        
        for k in sorted(mp): # from minimum to maximum 
            parent = list(range(m+n))
            for i, j in mp[k]: 
                ii, jj = find(i), find(m+j) # find 
                parent[ii] = jj # union 
                rank[jj] = max(rank[ii], rank[jj]) # max rank 
            
            seen = set()
            for i, j in mp[k]:
                ii = find(i)
                if ii not in seen: rank[ii] += 1
                seen.add(ii)
                rank[i] = rank[m+j] = ans[i][j] = rank[ii]
        return ans 

#attempt3: WA same results
'''
from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rowdic={}
        coldic={}
        n,m=len(matrix),len(matrix[0])
        final=[[0 for i in range(m)]for j in range(n)]
        eles=SortedList()
        
        for row in range(n):
            rowdic[row]=[0,-1]
            for col in range(m):
                coldic[col]=[0,-1]
                eles.add((matrix[row][col],(row,col)))
        
        for ele,pos in eles:
            row,col=pos
            maxcolval=-float('inf')
            #print(rowdic[row],coldic[col])
            maxr=rowdic[row]
            maxc=coldic[col]
            #print(ele,maxr,maxc,row,col)
            if maxr[-1]==-1 and maxc[-1]==-1:
                rowdic[row]=[1,col]
                coldic[col]=[1,row]
                final[row][col]=1
            elif maxr[-1]==-1 and maxc[-1]!=-1:
                if ele==matrix[coldic[col][-1]][col]:
                    rowdic[row][0],rowdic[row][1]=coldic[col][0],col
                    final[row][col]=coldic[col][0]
                else:
                    rowdic[row][0]=coldic[col][0]=coldic[col][0]+1
                    rowdic[row][1],coldic[col][1]=col,row
                    final[row][col]=coldic[col][0]
            elif maxc[-1]==-1 and maxr[-1]!=-1:
                if ele==matrix[row][rowdic[row][-1]]:
                    coldic[col][0],coldic[col][1]=rowdic[row][0],row
                    final[row][col]=coldic[col][0]
                else:
                    rowdic[row][0]=coldic[col][0]=rowdic[row][0]+1
                    rowdic[row][1],coldic[col][1]=col,row
                    final[row][col]=coldic[col][0]
            else:
                maxie=max(coldic[col][0],rowdic[row][0])
                if coldic[col][0]==rowdic[row][0]:
                    if ele!=matrix[coldic[col][1]][col]:
                        coldic[col][0]=rowdic[row][0]=coldic[col][0]+1
                    elif ele!=matrix[row][rowdic[row][1]]:
                        coldic[col][0]=rowdic[row][0]=coldic[col][0]+1
                    else:
                        pass
                else:
                    if maxie==coldic[col][0]:
                        if ele==matrix[coldic[col][1]][col]:
                            rowdic[row][0]=coldic[col][0]                        
                        else:
                            rowdic[row][0]=coldic[col][0]=coldic[col][0]+1                        
                    else:
                        if ele==matrix[row][rowdic[row][1]]:
                            coldic[col][0]=rowdic[row][0]
                        else:
                            rowdic[row][0]=coldic[col][0]=rowdic[row][0]+1
                
                rowdic[row][1]=col
                coldic[col][1]=row
                final[row][col]=coldic[col][0]
        
        grouping={}
        for row in range(n):
            for col in range(m):
                if matrix[row][col] not in grouping:
                    grouping[matrix[row][col]]=[]
                grouping[matrix[row][col]].append((row,col))
        #print(grouping)
        for i in grouping:
            grouping[i].sort(key=lambda x:final[x[0]][x[1]],reverse=True)
        
        #print(grouping)
        
        def connectedcomponents(i,curr,curc,visited):
            for r,c in grouping[i]:
                if (curr==r or curc==c) and (r,c) not in visited:
                    final[r][c]=final[curr][curc]
                    visited.add((r,c))
                    connectedcomponents(i,r,c,visited)
                    
        for i in grouping:
            visited=set()
            for j in grouping[i]:
                if j not in visited:
                    visited.add(j)
                    connectedcomponents(i,j[0],j[1],visited)        
        return final
'''

#attempt2: WA Read the question again and also the hints. Developed a solution
#which processed results based on many stuffs
'''
from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rowdic={}
        coldic={}
        n,m=len(matrix),len(matrix[0])
        final=[[0 for i in range(m)]for j in range(n)]
        eles=SortedList()
        
        for row in range(n):
            rowdic[row]=[0,-1]
            for col in range(m):
                coldic[col]=[0,-1]
                eles.add((matrix[row][col],(row,col)))
        
        for ele,pos in eles:
            row,col=pos
            maxcolval=-float('inf')
            #print(rowdic[row],coldic[col])
            maxr=rowdic[row]
            maxc=coldic[col]
            #print(maxr,maxc,row,col)
            if maxr[-1]==-1 and maxc[-1]==-1:
                rowdic[row]=[1,col]
                coldic[col]=[1,row]
                final[row][col]=1
            elif maxr[-1]==-1 and maxc[-1]!=-1:
                if ele==matrix[coldic[col][-1]][col]:
                    rowdic[row][0],rowdic[row][1]=coldic[col][0],col
                    final[row][col]=coldic[col][0]
                else:
                    rowdic[row][0]=coldic[col][0]=coldic[col][0]+1
                    rowdic[row][1],coldic[col][1]=col,row
                    final[row][col]=coldic[col][0]
            elif maxc[-1]==-1 and maxr[-1]!=-1:
                if ele==matrix[row][rowdic[row][-1]]:
                    coldic[col][0],coldic[col][1]=rowdic[row][0],row
                    final[row][col]=coldic[col][0]
                else:
                    rowdic[row][0]=coldic[col][0]=rowdic[row][0]+1
                    rowdic[row][1],coldic[col][1]=col,row
                    final[row][col]=coldic[col][0]
            else:
                if ele==matrix[coldic[col][-1]][col]:
                    rowdic[row][0],rowdic[row][1]=coldic[col][0],col
                    final[row][col]=coldic[col][0]
                elif ele==matrix[row][rowdic[row][-1]]:
                    coldic[col][0],coldic[col][1]=rowdic[row][0],row
                    final[row][col]=coldic[col][0]
                else:
                    rowdic[row][0]=coldic[col][0]=max(rowdic[row][0],coldic[col][0])+1
                    rowdic[row][1],coldic[col][1]=col,row
                    final[row][col]=coldic[col][0]
            
        return final
'''


#attempt1:WA IDEA was to find number of elements in same row and column which are
#lesser than current element
#DIDNT UNDERSTAND THE QUESTION WELL, didnt submmit the answer but realized the
#incorrectness of the approach
'''
Solution lost
'''