#attempt1: Read question properly
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        first = 0
        second = 1
        third = 1
        number = 3
        while(number <= n):
            number += 1
            fourth = first+second+third
            first = second
            second = third
            third = fourth
            #print(number,first,second,third,fourth)
        return third
