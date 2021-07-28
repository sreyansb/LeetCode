#attempt2: TOOK HELP AC On experimentation I found out that odd numbers and even numbers need to be separated and kept
#in different halves(2*nums[k] wont be satisfied if different parity).
#made similar changes but WA still because condition not following.
#TOOK HELP AND SAW THAT YOU GOT TO PERFORM RECURSION FOR EACH HALF BY DIVIDING EVENS AND ODDS  

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        arr=list(range(1,n+1))
        def fn(arr):
            n=len(arr)
            if n<=1:
                return arr
            arr=fn([arr[i] for i in range(n) if i%2])+fn([arr[i] for i in range(n) if i%2==0])
            return arr
        return fn(arr)

#attempt1: WA I thought it was about reversing halves, not correct
'''
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        arr=list(range(1,n+1))
        mid=(n-1)//2
        arr=arr[:mid+1][::-1]+arr[mid+1:][::-1]
        return arr
'''