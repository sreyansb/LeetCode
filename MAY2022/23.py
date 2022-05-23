#attempt1:
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count_zero_one = []
        for string in strs:
            count_zero_one.append([0,0])
            for char in string:
                count_zero_one[-1][int(char)] += 1
        leng = len(count_zero_one)
        
        @lru_cache(None)
        def find_answers(leftzeros,leftones,index):
            if index >= leng:
                return 0
            if count_zero_one[index][0]<=leftzeros and count_zero_one[index][1]<=leftones:
                return max(find_answers(leftzeros,leftones,index+1),1+find_answers(leftzeros-count_zero_one[index][0],leftones-count_zero_one[index][1],index+1))
            return find_answers(leftzeros,leftones,index+1)
        
        return find_answers(m,n,0)
        
