#attempt2:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        
        if s3_len!=s1_len+s2_len:
            return False
        
        @lru_cache(None)
        def is_it_interleaved(index_s1,index_s2,index_s3):
            if index_s1>=s1_len:
                return s2[index_s2:] == s3[index_s3:]
            if index_s2>=s2_len:
                return s1[index_s1:] == s3[index_s3:]
            ans = False
            if s3[index_s3] == s2[index_s2]:
                ans = is_it_interleaved(index_s1,index_s2+1,index_s3+1)
            if s3[index_s3] == s1[index_s1]:
                ans = ans or is_it_interleaved(index_s1+1,index_s2,index_s3+1)
            return ans
        
        return is_it_interleaved(0,0,0)
                
        

#attempt1: Runtie Error becasue didn't check that s3_len == s1_len+s2_len
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        
        @lru_cache(None)
        def is_it_interleaved(index_s1,index_s2,index_s3):
            if index_s1>=s1_len:
                return s2[index_s2:] == s3[index_s3:]
            if index_s2>=s2_len:
                return s1[index_s1:] == s3[index_s3:]
            ans = False
            if s3[index_s3] == s2[index_s2]:
                ans = is_it_interleaved(index_s1,index_s2+1,index_s3+1)
            if s3[index_s3] == s1[index_s1]:
                ans = ans or is_it_interleaved(index_s1+1,index_s2,index_s3+1)
            return ans
        
        return is_it_interleaved(0,0,0)
                
        
'''
