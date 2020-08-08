class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li=[str(i) for i in range(1,n+1)]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                li[i-1]="FizzBuzz"
            elif i%3==0:
                li[i-1]="Fizz"
            elif i%5==0:
                li[i-1]="Buzz"
        return li
            
        
