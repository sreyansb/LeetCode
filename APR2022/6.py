#attempt4: 9990ms
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        n = len(arr)
        for top_ele in range(n):
            ele_to_search_for = target-arr[top_ele]
            di = {}
            for rest_of_eles_index in range(top_ele+1,n):
                rest_of_eles = arr[rest_of_eles_index]
                if ele_to_search_for-rest_of_eles in di:
                    ans += di[ele_to_search_for-rest_of_eles]
                if rest_of_eles not in di:
                    di[rest_of_eles] = 0
                di[rest_of_eles] += 1
        return ans%1000000007

#attempt3: TLE
'''
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        n = len(arr)
        for top_ele in range(n):
            ele_to_search_for = target-arr[top_ele]
            di = {}
            for rest_of_eles_index in range(top_ele+1,n):
                if ele_to_search_for-arr[rest_of_eles_index] in di:
                    ans += di[ele_to_search_for-arr[rest_of_eles_index]]
                if arr[rest_of_eles_index] not in di:
                    di[arr[rest_of_eles_index]] = 0
                di[arr[rest_of_eles_index]] += 1
            ans %= 1000000007
        return ans
'''

#attempt2: TLE
'''
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        n = len(arr)
        for top_ele in range(n):
            ele_to_search_for = target-arr[top_ele]
            di = {}
            for rest_of_eles_index in range(top_ele+1,n):
                if ele_to_search_for-arr[rest_of_eles_index] in di:
                    ans += di[ele_to_search_for-arr[rest_of_eles_index]]
                if arr[rest_of_eles_index] not in di:
                    di[arr[rest_of_eles_index]] = 0
                di[arr[rest_of_eles_index]] += 1
                ans %= 1000000007
        return ans
'''

#attempt1: TLE
'''
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        n = len(arr)
        for top_ele in range(n):
            ele_to_search_for = target-arr[top_ele]
            di = {}
            for rest_of_eles_index in range(top_ele+1,n):
                if ele_to_search_for-arr[rest_of_eles_index] in di:
                    ans += di[ele_to_search_for-arr[rest_of_eles_index]]
                if arr[rest_of_eles_index] not in di:
                    di[arr[rest_of_eles_index]] = 0
                di[arr[rest_of_eles_index]] += 1
        return ans%(1000000007)
'''
