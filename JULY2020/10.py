
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

        
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not(head):
            return
        s,final=[head],[]
        while(s):
            k=s.pop()
            final.append(k)
            if k.next:
                s.append(k.next)
            if k.child:
                s.append(k.child)
        for i in range(len(final)-1):
            final[i].next=final[i+1]
            final[i+1].prev=final[i]
            final[i].child=None
        final[-1].chld=None
        return final[0]

obj1=Node()
obj2=Node()
obj3=Node()
obj4=Node()
obj5=Node()
obj6=Node()
obj7=Node()
obj8=Node()
obj9=Node()
obj10=Node()
obj11=Node()
obj12=Node()

obj1.val=1
obj2.val=2
obj3.val=3
obj4.val=4
obj5.val=5
obj6.val=6
obj7.val=7
obj8.val=8
obj9.val=9
obj10.val=10
obj11.val=11
obj12.val=12

obj1.next=obj2
obj2.prev=obj1
obj2.next=obj3
obj3.prev=obj2
obj3.next=obj4
obj4.prev=obj3
obj4.next=obj5
obj5.prev=obj4
obj5.next=obj6
obj6.prev=obj5
obj3.child=obj7
obj7.next=obj8
obj8.prev=obj7
obj8.next=obj9
obj9.prev=obj8
obj9.next=obj10
obj10.prev=obj9
obj8.child=obj11
obj11.next=obj12
obj12.prev=obj11

k=obj1
i=1
while(k):
    print(k.val,k,k.next,k.prev)
    k=k.next
    i+=1
    print()
    
k=obj3.child
while(k):
    print(k.val,k,k.next,k.prev)
    k=k.next
    i+=1
    print()

k=obj8.child
while(k):
    print(k.val,k,k.next,k.prev)
    k=k.next
    i+=1
    print()

sol=Solution()
print()
print(sol.flatten(obj1))
print()

k=obj1
i=1
while(k):
    print(k.val,k.next,k.prev)
    k=k.next
    i+=1   

"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def recurse(i,st):
    
    if i==None:
        return i

    print(i.val,i)
    
    if i.next==None:
        if len(st)>0:
            j=st.pop()
            j.prev=i
            i.next=j
        return i
    
    if i.child==None:
        return recurse(i.next,st)
        
        
    if i.child:
        #print(f"val {i.val}")
        d=i.next
        st.append(d)
        i.next=recurse(i.child,st)
        i.next.prev=i
        return recurse(d,st)
        

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        recurse(head,[])
        return head
"""


    
"""
while obj1:
    print(obj1.val)
    print(obj1.next)
    print(obj1.prev)
    print(obj1.child)
    print()
    obj1=obj1.next
"""
