#attempt1:

class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n=len(jobs)
        infi=float('inf')
        if n<d:
            return -1
        if n==d:
            return sum(jobs)
        #we need to make d incisions in the array
        dpt=[[-1 for i in range(d+1)] for i in range(n+1)]
        ans=[]
        jobs=[0]+jobs
        for i in range(1,n+1):
            dpt[i][1]=max(jobs[1:i+1])
            for j in range(2,min(i,d)+1):
                if i==j:
                    dpt[i][j]=jobs[j]+dpt[i-1][j-1]
                else:
                    dpt[i][j]=infi
                    for k in range(1,i):#we need to go from index 1 to index i-1 to find later cuts
                        if dpt[k][j-1]!=-1:
                            dpt[i][j]=min(dpt[k][j-1]+max(jobs[k+1:i+1]),dpt[i][j])
        #print(dpt)
        return dpt[n][d]
