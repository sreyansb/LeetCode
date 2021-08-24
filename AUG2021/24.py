#attempt2: For all sort of test cases
'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        if '+' not in num1:
            if 'i' not in num1:
                num1=num1+"+"
            else:
                num1="+"+num1
        if '+' not in num2:
            if 'i' not in num2:
                num2=num2+"+"
            else:
                num2="+"+num2
        n11,n12=num1.split("+")
        n21,n22=num2.split("+")
        if not n11:
            n11=0
        if not n12:
            n12=0
        if not n21:
            n21=0
        if not n22:
            n22=0
        
        n11,n21=int(n11),int(n21)
        n12,n22=int(n12[:-1]),int(n22[:-1])
        f1=(n11*n21-n22*n12)
        f2=(n12*n21+n22*n11)
        return f"{str(f1)}+{str(f2)}i"
'''

#attempt1: Assuming we always get a number of type a+bi
'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n11,n12=num1.split("+")
        n21,n22=num2.split("+")
        n11,n21=int(n11),int(n21)
        n12,n22=int(n12[:-1]),int(n22[:-1])
        f1=(n11*n21-n22*n12)
        f2=(n12*n21+n22*n11)
        return f"{str(f1)}+{str(f2)}i"
'''