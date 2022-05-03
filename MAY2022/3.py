#attempt3:
class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        sorted_arr = sorted(arr)
        leftmost,rightmost = -1,-1
        for i in range(n):
            if sorted_arr[i] != arr[i]:
                leftmost = i
                break
        if leftmost != -1:
            for i in range(n-1,leftmost,-1):
                if arr[i] != sorted_arr[i]:
                    rightmost = i
                    break
            return rightmost-leftmost+1
        return 0

#attempt2: WA
'''
class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n==1:
            return 0
        right_unsorted_index = -1
        left_unsorted_index = -1
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                right_unsorted_index = i
                while(right_unsorted_index+1<n and arr[right_unsorted_index+1] == arr[i+1]):
                    right_unsorted_index += 1
                break
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                left_unsorted_index = i
                while(left_unsorted_index-1>=0 and arr[left_unsorted_index-1] == arr[i-1]):
                    left_unsorted_index -= 1
                break
        if right_unsorted_index != -1 and left_unsorted_index != -1:
            return right_unsorted_index-left_unsorted_index+1
        return 0
                
                
            
                
'''

#attempt1: WA
'''
class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n==1:
            return 0
        right_unsorted_index = -1
        left_unsorted_index = -1
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                right_unsorted_index = i+1
                break
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                left_unsorted_index = i-1
                break
        if right_unsorted_index != -1 and left_unsorted_index != -1:
            return right_unsorted_index-left_unsorted_index+1
        return 0                
'''
