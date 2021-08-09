#attempt2:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        final=""
        p1=0
        p2=0
        num1=num1[::-1]
        num2=num2[::-1]
        len1=len(num1)
        len2=len(num2)
        while(p1<len1 and p2<len2):
            sumy=int(num1[p1])+int(num2[p2])+carry
            final+=str(sumy%10)
            carry=sumy//10
            p1+=1
            p2+=1
        while(p1<len1):
            sumy=int(num1[p1])+carry
            final+=str(sumy%10)
            carry=sumy//10
            p1+=1
        while(p2<len2):
            sumy=int(num2[p2])+carry
            final+=str(sumy%10)
            carry=sumy//10
            p2+=1
        if carry:
            final+=str(carry)
        return final[::-1]

#attempt1:WA because didnt take care of last condition that carry can be non zero
# at end of computation and has to be added at end of the string
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        final=""
        p1=0
        p2=0
        num1=num1[::-1]
        num2=num2[::-1]
        len1=len(num1)
        len2=len(num2)
        while(p1<len1 and p2<len2):
            sumy=int(num1[p1])+int(num2[p2])+carry
            final+=str(sumy%10)
            carry=sumy//10
            p1+=1
            p2+=1
        while(p1<len1):
            sumy=int(num1[p1])+carry
            final+=str(sumy%10)
            carry=sumy//10
            p1+=1
        while(p2<len2):
            sumy=int(num2[p2])+carry
            final+=str(sumy%10)
            carry=sumy//10
            p2+=1
        return final[::-1]
'''

