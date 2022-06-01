#attempt1:
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        account = []
        for word in words:
            letters_present = set(word)
            word_len = len(word)
            account.append((letters_present,word_len))
        ans = 0
        account_len = len(account)
        for base_index in range(account_len):
            word_set,word_leng = account[base_index]
            for further_index in range(base_index+1,account_len):
                ans = max(ans,0 if word_set&account[further_index][0] else word_leng*account[further_index][1])
        return ans
        
