#attempt2:
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def fun(word):
            if len(set(word)) == len(word):
                return True
            return False
        
        filtered = list(filter(fun,arr))
        max_ans = [0]
        n = len(filtered)
        
        @lru_cache(None)
        def dfs(cur_word,cur_index):
            max_ans[0] = max(max_ans[0],len(cur_word))
            for next_index in range(cur_index,n):
                if len(filtered[next_index]+cur_word) == len(set(filtered[next_index]+cur_word)):
                    dfs(cur_word+filtered[next_index],next_index)
        
        for index,word in enumerate(filtered):
            dfs(word,index)
            
        return max_ans[0]

#attempt1: WA because was using a different array rather than the one
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def fun(word):
            if len(set(word)) == len(word):
                return True
            return False
        
        filtered = list(filter(fun,arr))
        max_ans = [0]
        n = len(filtered)
        
        @lru_cache(None)
        def dfs(cur_word,cur_index):
            max_ans[0] = max(max_ans[0],len(cur_word))
            for next_index in range(cur_index,n):
                if len(filtered[next_index]+cur_word) == len(set(filtered[next_index]+cur_word)):
                    dfs(cur_word+arr[next_index],next_index)
        
        for index,word in enumerate(filtered):
            dfs(word,index)
            
        return max_ans[0]
'''
