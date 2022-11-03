#attempt2:
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        #words = set(words)
        di = {}
        maxl = 0
        for word in words:
            l1,l2 = word
            if (l2,l1) in di and di[(l2,l1)]:
                di[(l2,l1)] -= 2
                maxl += 4
            else:
                if (l1,l2) not in di:
                    di[(l1,l2)] = 0
                di[(l1,l2)] += 2
        for char1,char2 in di:
            if char1 == char2 and di[(char1,char2)]:
                maxl += 2
                break
        return maxl
                
            
        

#attempt1: WA because didn't understand question well
'''
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words = set(words)
        di = {}
        maxl = 0
        mid = False
        for word in words:
            if word[0] == word[1] and not(mid):
                mid = True
                maxl += 2
            l1,l2 = min(word),max(word)
            if (l1,l2) in di:
                di[(l1,l2)] -= 2
                maxl += 4
            else:
                di[(l1,l2)] = 2
        return maxl
                
            
        
'''
