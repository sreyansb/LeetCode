#attempt1:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        di_number_index = {}
        for index,number in enumerate(nums):
            if number not in di_number_index:
                di_number_index[number] = []
            di_number_index[number].append(index)
        for number in di_number_index:
            for index in range(1,len(di_number_index[number])):
                if di_number_index[number][index] - di_number_index[number][index-1] <= k:
                    return True
        return False
        
