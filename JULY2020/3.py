class Solution:
    def prisonAfterNDays(self, cells,N):
        l=[0]*15
        for i in range(1,15):
            newcells=[0]*8
            for j in range(1,7):
                newcells[j]=int(not(cells[j-1]^cells[j+1]))
            l[i]=newcells.copy()
            cells=newcells.copy()
            print(i,l[i])
        l[0]=l[14]
        print(l)
        return(l[N%14])

if __name__ == "__main__":
    l=[0,1,0,1,1,0,0,1]
    N=7
    obj=Solution()
    print(obj.prisonAfterNDays(l,N))
