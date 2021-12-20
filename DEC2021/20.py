#attempt1: It is all about finding the min diff
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mindiff = float('inf')
        ans = []
        arr.sort()
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff<mindiff:
                mindiff = diff
                ans = [[arr[i],arr[i+1]]]
            elif diff==mindiff:
                ans.append([arr[i],arr[i+1]])
        return ans
