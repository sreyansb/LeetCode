#attempt3_my_soln : TOOK HELP
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        di = {}
        for i in nums:
            curdi = di
            for mask in range(32,-1,-1):
                if (i>>mask)&1:#it cant be num&(1<<i) because to check if
                #last digit is odd we need to "AND" it with 1
                    if 1 not in curdi:
                        curdi[1] = {}
                    curdi = curdi[1]
                else:
                    if 0 not in curdi:
                        curdi[0] = {}
                    curdi = curdi[0]
            curdi["e"] = i
        maxie = 0
        for i in nums:
            curdi = di
            for mask in range(32,-1,-1):
                b = (i>>mask)&1
                if b^1 in curdi:
                    curdi = curdi[b^1]
                else:
                    curdi = curdi[b]
            if "e" in curdi:
                maxie = max(maxie,i^curdi["e"])
        return maxie

#attempt3_copy: TOOK HELP
'''
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:     
        trie = {}
        for num in nums: 
            node = trie
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node: 
                    node[bit] = {}
                    
                node = node[bit]
            
            node["$"] = num
            
        ans = 0 
        for num in nums: 
            node = trie 
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if (1 - bit) in node: 
                    node = node[1 - bit]
                else: 
                    node = node[bit]
            
            ans = max(ans, num^node["$"])
            
        return ans
'''

#attempt2: WRONG IMPLEMENTATION
'''
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        """
        di = {i:set() for i in range(32)}
        highestpower = 0
        for i in range(n):
            i_copy = nums[i]
            curpow = 0
            while(i_copy):
                if i_copy&1:
                    di[curpow].add(i)
                curpow += 1
                i_copy >>= 1
            highestpower = max(highestpower,curpow)
        #print(di)
        valid = set([i for i in range(n)])
        invalid = set([i for i in range(n)])
        for i in range(highestpower,-1,-1):
            if di[i]&valid:
                valid = valid&di[i]
                invalid = invalid-di[i]
            print(i,valid,invalid)
        maxie = 0
        for index_i in valid:
            for index_j in invalid:
                maxie = max(maxie,nums[index_i]^nums[index_j])
        return maxie
        """
        """
        for i in range(n):
            for j in range(i+1,n):
                print(i,j,nums[i]^nums[j])
        return 0
        """
'''

#attempt1: Wrong Idea : It is not just max(max(array)^i for i in array)
'''
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = max(nums)
        return max([i^n for i in nums])
'''
