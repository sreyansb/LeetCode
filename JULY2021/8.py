#attempt4: Took HINT
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        dpt=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i]==nums2[j]:
                    dpt[i][j]=dpt[i+1][j+1]+1
        return max([max(rows) for rows in dpt])
        

#attempt1-3: WA didnt frame the loop properly and used  loop vatiables for other loops 
# AND TLE
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxie=0
        di2={}
        m,n=len(nums1),len(nums2)
        for i in range(n):
            if nums2[i] not in di2:
                di2[nums2[i]]=[]
            di2[nums2[i]].append(i)
        di1={}
        for i in range(m):
            if nums1[i] not in di1:
                di1[nums1[i]]=[]
            di1[nums1[i]].append(i)
        for i in set(nums1)&set(nums2):
            for pos1 in di1[i]:
                curlen=0 # should be 0 for both pos1 an dpos2
                for pos2 in di2[i]:
                    while(pos1<m and pos2<n and nums1[pos1]==nums2[pos2]):#this loop shouldn't use pos1 and pos2
                        pos1+=1
                        pos2+=1
                        curlen+=1
                maxie=max(maxie,curlen)
        return maxie
            
        
        
'''