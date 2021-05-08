#attempt1: TOOK HELP totally stumped me
#it is a mathematical question
#need to look at from other side i.e. instead of doing square root
#make the squares from their square roots.
#Max limit of left,right is 10^18
#so max square root is 10^9 = 10 digits
#We use string concatenation. Assume a string number 'a' of length x.
#To make palindrome square roots:
#we need a+a(reversed) i.e. even length palindrome
#or we need a+(a(reversed)[1:]) i.e. odd length palindrome
#Therefore length of 'a' can be max 5(concatenated) to make 10 max
#**max 5 digit number is 99999**. Therefore maxie is 100000 and run your code

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        maxie=100000
        ans=0
        left=int(left)
        right=int(right)
        for i in range(maxie):
            s=str(i)
            k1=s+(s[::-1][1:])
            if k1==k1[::-1]:
                k1=int(k1)
                num=k1*k1
                if num>right:
                    break
                if num>=left:
                    num=str(num)
                    if num==num[::-1]:
                        ans+=1
        for i in range(maxie):
            s=str(i)
            k1=s+s[::-1]
            if k1==k1[::-1]:
                k1=int(k1)
                num=k1*k1
                if num>right:
                    break
                if num>=left:
                    num=str(num)
                    if num==num[::-1]:
                        ans+=1
        return ans
