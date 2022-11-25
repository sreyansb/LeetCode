#attempt1: TOOK HELP
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = [(-float('inf'),-1)]
        totalSum = 0
        sums = {-1:0}
        for index in range(n):
            while(stack and stack[-1][0] > arr[index]):
                stack.pop()
            sums[index] = sums[stack[-1][-1]] + (index-stack[-1][-1])*arr[index]
            stack.append((arr[index],index))
        #print(sums)
        return sum(sums.values())%(1000000007)
# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
        
#         stack, sums = [], [0] * len(arr)

#         for i,n in enumerate(arr):
#             while stack and arr[stack[-1]] > n:
#                 stack.pop()
#             j = stack[-1] if stack else -1
            
#             sums[i] = sums[j] + (i-j)*n
#             stack.append(i)
        
#         return sum(sums) % (1_000_000_007)
