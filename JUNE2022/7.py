#attempt6: Others were WA becayse of algo mistakes.
#Go and fill from back
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        to_be_filled_index = m+n-1
        
        if n==0:
            return
        
        index1 = m-1
        index2 = n-1
        
        while(index1>=0 and index2>=0):
            val = -1
            if nums1[index1] > nums2[index2]:
                val = nums1[index1]
                index1 -= 1
            else:
                val = nums2[index2]
                index2 -= 1
            nums1[to_be_filled_index] = val
            to_be_filled_index -= 1

        while(index2>=0):
            nums1[to_be_filled_index] = nums2[index2]
            index2 -= 1
            to_be_filled_index -= 1

        return
            
        
