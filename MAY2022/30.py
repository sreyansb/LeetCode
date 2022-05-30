#attempt1:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        multiplier = 1
        
        if dividend<0:
            multiplier *= -1
            dividend *= -1
            
        if divisor < 0:
            multiplier *= -1
            divisor *= -1
        
        if dividend<divisor:
            return 0
        
        ans = 0
        divisor_str = str(divisor)
        divisor_str = divisor_str.lstrip("0")
        divisor_len = len(divisor_str)
        dividend_str = str(dividend)
        dividend_str = dividend_str.lstrip("0")
        dividend_len = len(dividend_str)
        index = divisor_len-1
        remainder = dividend_str[:divisor_len-1]
        while(index < dividend_len):
            current_dividend_str = remainder+dividend_str[index]
            current_dividend = int(current_dividend_str)
            value = 0
            while(current_dividend>=divisor):
                value += 1
                current_dividend -= divisor
            ans = ans*10 + value
            remainder = str(current_dividend)
            index += 1
            #print(remainder,index,ans)
        return max(min((1<<31)-1,ans*multiplier),-(1<<31))
