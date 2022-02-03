#attempt4: Most of the times, answers are really simple!!!!
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ans = 0
        ipjsums = {}
        for i in range(n):
            for j in range(n):
                ipj = nums1[i]+nums2[j]
                if ipj not in ipjsums:
                    ipjsums[ipj] = 0
                ipjsums[ipj] += 1
        di = {}
        for k in range(n):
            for l in range(n):
                negipj = -(nums3[k]+nums4[l])
                if negipj in ipjsums:
                    ans += ipjsums[negipj]
        return ans

#attempt3: 1746 ms We don't have to write code for k and l together.
#We can just sum them together
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ans = 0
        ipjsums = {}
        for i in range(n):
            for j in range(n):
                ipj = nums1[i]+nums2[j]
                if ipj not in ipjsums:
                    ipjsums[ipj] = 0
                ipjsums[ipj] += 1
        di = {}
        for ipj in ipjsums:
            for j in range(n):
                if ipj+nums3[j] not in di:
                    di[ipj+nums3[j]] = 0
                di[ipj+nums3[j]] += ipjsums[ipj]
        for k in range(n):
            if -nums4[k] in di:
                ans += di[-nums4[k]]
        return ans

#attempt2: TLE because of O(200*200*200*2) complexity
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ans = 0
        for i in range(n):
            for j in range(n):
                ipj = nums1[i]+nums2[j]
                di = {}
                for k in range(n):
                    if ipj+nums3[k] not in di:
                        di[ipj+nums3[k]] = 0
                    di[ipj+nums3[k]] += 1
                for k in range(n):
                    if -nums4[k] in di:
                        ans += di[-nums4[k]]
                    
        return ans
'''

#attempt1: WA because i dont take into consideration l<k
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ans = 0
        for i in range(n):
            for j in range(n):
                ipj = nums1[i]+nums2[j]
                di = {}
                for k in range(n):
                    if ipj+nums3[k] not in di:
                        di[ipj+nums3[k]] = 0
                    di[ipj+nums3[k]] += 1
                    if -nums4[k] in di:
                        ans += di[-nums4[k]]
                    
        return ans
'''
