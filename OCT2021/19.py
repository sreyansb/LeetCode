#attempt2: 83ms
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di = {}
        for i in range(len(nums2)):
            di[nums2[i]] = -1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    di[nums2[i]] = nums2[j]
                    break
        for i in range(len(nums1)):
            nums1[i] = di[nums1[i]]
        return nums1

#attempt1: 60 ms

'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di = {}
        for i in range(len(nums2)):
            di[nums2[i]] = -1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    di[nums2[i]] = nums2[j]
                    break
        ans = []
        for i in nums1:
            ans.append(di[i])
        return ans
'''