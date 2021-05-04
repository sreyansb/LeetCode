#attempt4: TOOK HELP. we had to change the array itself.
#changing a wrong position of elements depends on i-2th index waala element
class Solution:
    def checkPossibility(self, a: List[int]) -> bool:
        n=len(a)
        cnt=0
        for i in range(1,n):
            if a[i-1]>a[i]:
                if cnt==1:
                    return False
                if i-2>=0:
                    if a[i-2]>a[i]:
                        a[i]=a[i-1]
                    else:
                        a[i-1]=a[i]
                else:
                    a[i-1]=a[i]
                cnt+=1
        return True
                        

#attempt3: TOOK HELP - didn't understand
'''
class Solution:
    def checkPossibility(self, a: List[int]) -> bool:
        n=0
        flag=1
        for i in range(1,len(a)):
            if a[i-1]<=a[i]:
                continue
            else:
                if (n==1 or (i-1>0 and i+1<len(a) and a[i+1]<a[i-1] and a[i]<a[i-2])):
                    return False
                n+=1
        return True
'''


#attempt2: WA
'''
class Solution:
    def checkPossibility(self, a: List[int]) -> bool:
        number=0
        for i in range(1,len(a)):
            if a[i-1]<=a[i]:
                continue
            else:
                number+=1
                a[i-1]=a[i]
                if number>1:
                    break
        return a==sorted(a)
'''

#attempt1:WA FAILED for [3,4,2,3]
'''
class Solution:
    def checkPossibility(self, a: List[int]) -> bool:
        number=0
        for i in range(1,len(a)):
            if a[i-1]<=a[i]:
                continue
            else:
                number+=1
                a[i-1]=a[i]
                if number>1:
                    break
        return number<=1
'''
