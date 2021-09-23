#attempt1: 82% Just remember that the smallest one is theone with "a"
#at the earliest position
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<=1:
            return ""
        palindrome=list(palindrome)
        for i in range(len(palindrome)):
            if palindrome[i]=="a":
                continue
            else:
                temp=palindrome[i]
                palindrome[i]="a"
                if palindrome[::-1]!=palindrome:
                    return "".join(palindrome)
                palindrome[i]=temp
        if palindrome[-1]!="b":
            palindrome[-1]="b"
        return "".join(palindrome)
