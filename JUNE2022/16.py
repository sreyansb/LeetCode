#attempt1:AC
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def find_longest_palindrome(first_index,second_index):
            while(first_index>=0 and second_index<n and s[first_index] == s[second_index]):
                first_index -= 1
                second_index += 1
            return (second_index-1)-(first_index+1)+1
        maxans = 1
        maxstr = s[-1]
        for index in range(n-1):
            ans_odd = find_longest_palindrome(index,index)
            if ans_odd>maxans:
                maxans = ans_odd
                maxstr = s[index-(ans_odd-1)//2:index+1+(ans_odd-1)//2]
            ans_even = find_longest_palindrome(index,index+1)
            if ans_even>maxans:
                maxans = ans_even
                maxstr = s[index-(ans_even-1)//2:index+2+(ans_even-1)//2]
        return maxstr
            
            
                
