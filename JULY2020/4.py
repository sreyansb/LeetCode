def findsol(n):
        while(n%2==0):
            n//=2
        for i in range(3,6,2):
            while(n%i==0):
                n//=i
        return n==1
    
class Solution:            
    def nthUglyNumber(self, n: int) -> int:
        if n<=0:
            return 0
        else:
            sorte=[1]
            numbers=1
            pointer1=0
            pointer2=0
            pointer3=0
            while(numbers<n):
                m1=sorte[pointer1]*2
                m2=sorte[pointer2]*3
                m3=sorte[pointer3]*5
                k=min(m1,m2,m3)
                sorte.append(k)
                if k==m1:
                    pointer1+=1
                if k==m2:
                    pointer2+=1
                if k==m3:
                    pointer3+=1
                numbers+=1
            return k[-1]
                    
        '''
        l1=[1]
        l2=[2]
        l3=[3]
        sorte=[1,2,3]
        number=n
        if number==1:
            return 1
        elif number==2:
            return 2
        elif number==3:
            return 3
        else:
            number=3
            while(number<n):
                if l1[0]*2
        '''
        
        '''
        u=1
        l=[1]
        front=0
        number=1
        while(number<n):
            l.extend([l[front]*2,l[front]*3,l[front]*5])
            number+=3
            front+=1
        print()
        '''
        
        '''
        number=1
        i=2
        if n==0:
            return 0
        while(number!=n):
            if findsol(i):
                number+=1
            i+=1
        return i-1
        '''
            
obj=Solution()
print(obj.nthUglyNumber(10))
