#attemptfinal:
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n=len(A)
        if n<3:
            return 0
        diff=[0]*(n-1)
        #differences[i] holds the differences between A[i] and A[i+1]
        i=0
        while(i<n-1):
            diff[i]=A[i]-A[i+1]
            i+=1
        left=0
        count=0
        while(left<n-1):
            #print(left)
            right=left+1
            while(right<n-1 and diff[right]==diff[left]):
                right+=1
            if right-left+1>2:
                #print(left,right,A[left:right+1])
                z=right-left+1
                count+=(1+z)*(z-2)-(z*(z+1))/2+3
            left=right
        return int(count)
                
#len-3+1+len-4+1....len-len+1
#(1+len)*(len-3+1)-(len*(len+1)/2-3)
            

#attempt2:
'''
class Solution:
    def numberOfArithmeticSlices(self, A):
        n=len(A)
        if n<3:
            return 0
        diff=[0]*(n-1)
        #differences[i] holds the differences between A[i] and A[i+1]
        i=0
        while(i<n-1):
            diff[i]=A[i]-A[i+1]
        left=0
        count=0
        while(left<n-2):
            print(left)
            right=left+1
            while(right<n-1 and diff[right]==diff[left]):
                right+=1
            if right-left+1>2:
                z=right-left+1
                count+=2**z-(1+z+(z*(z-1))/2)
            left=right+1
        return count

A=[1,2,3,4,5]
obj=Solution()
print(obj.numberOfArithmeticSlices(A))
'''
