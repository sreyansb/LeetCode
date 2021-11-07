#attempt2: 74 ms and 14MB
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        power = 1
        
        def reverse_multiply(i,num1):
            carry = 0
            ans = 0
            power = 1
            i = int(i)
            for j in num1[::-1]:
                middle = i*int(j)+carry
                ans += (middle%10)*power
                power *= 10
                carry = middle//10
            if carry:
                ans += carry*power
            return ans                
        
        di = {}
        for i in num2[::-1]:
            if i not in di:
                di[i] = reverse_multiply(i,num1)
            ans += di[i] * power
            power *= 10
        return str(ans)

#attempt1: WA Forgot that carry can exist even at end
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        power = 1
        
        def reverse_multiply(i,num1):
            carry = 0
            ans = 0
            power = 1
            i = int(i)
            for j in num1[::-1]:
                middle = i*int(j)+carry
                ans += (middle%10)*power
                power *= 10
                carry = middle//10
            return ans                
        
        di = {}
        for i in num2[::-1]:
            if i not in di:
                di[i] = reverse_multiply(i,num1)
            ans += di[i] * power
            power *= 10
        return str(ans)
'''
