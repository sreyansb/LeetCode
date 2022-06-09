#attempt2:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        def binary_search(key,low,high):
            while(low <= high):
                mid = (low+high)//2
                if numbers[mid] == key:
                    return mid
                if numbers[mid] > key:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        
        for index in range(n):
            number = numbers[index]
            if target-number != number:
                nextindex = binary_search(target-number,0,n-1)
                if nextindex != -1:
                    return [index+1,nextindex+1]
            else:
                return [index+1,index+2]
        
        return [-1,-1]
        
        

#attempt1: WA because both the indexes cant be same
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        def binary_search(key,low,high):
            while(low <= high):
                mid = (low+high)//2
                if numbers[mid] == key:
                    return mid
                if numbers[mid] > key:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        
        for index in range(n):
            number = numbers[index]
            nextindex = binary_search(target-number,0,n-1)
            if nextindex != -1:
                return [index+1,nextindex+1]
        
        return [-1,-1]
        
        
'''
