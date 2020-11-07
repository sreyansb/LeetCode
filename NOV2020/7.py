#attempt2: 89%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not(l1) and not(l2):
            return None
        
        def findlen(head):
            n=0
            while(head):
                n+=1
                head=head.next
            return n
                
        def findans(head1,head2,diff):
            #head1 has larger length
            st=[ListNode(-1)]
            while(diff):
                k=ListNode(head1.val)
                st[-1].next=k
                st.append(k)
                head1=head1.next
                diff-=1
            carry=0
            while(head1 and head2):
                valt=(head1.val+head2.val+carry)
                val=valt%10
                carry=valt//10
                news=[]
                while(carry):
                    j=st.pop()
                    temp=j.val
                    if temp==-1:
                        newnode=ListNode(carry)
                        newnode.next=j.next
                        j.next=newnode
                        news+=[newnode,j]
                        carry=0
                        break
                    else:
                        j.val=(temp+carry)%10
                        carry=(temp+carry)//10
                        news.append(j)
                while(news):
                    st.append(news.pop())
                st[-1].next=ListNode(val)
                st.append(st[-1].next)
                head1=head1.next
                head2=head2.next
            return st[1]
        
        le1=findlen(l1)
        le2=findlen(l2)
        if le1>le2:
            return findans(l1,l2,le1-le2)
        else:
            return findans(l2,l1,le2-le1)
            

#attempt1: 50.54%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            prev=None
            while(head):
                temp=head.next
                head.next=prev
                prev=head
                head=temp
            return prev       
        def findlen(head):
            n=0
            while(head):
                n+=1
                head=head.next
            return n
        n1=findlen(l1)
        n2=findlen(l2)
        head1=reverse(l1)
        head2=reverse(l2)
        carry=0
        ans=ListNode()
        anshead=ans
        #print(head1.val,head2.val)
        while(head1 and head2):
            k=(head1.val+head2.val+carry)
            ans.next=ListNode(k%10)
            carry=k//10
            ans=ans.next
            head1=head1.next
            head2=head2.next
        while(head1):
            k=head1.val+carry
            ans.next=ListNode(k%10)
            carry=k//10
            head1=head1.next
            ans=ans.next
        while(head2):
            k=head2.val+carry
            ans.next=ListNode(k%10)
            carry=k//10
            head2=head2.next
            ans=ans.next
        if carry:
            ans.next=ListNode(carry)
        return reverse(anshead.next)
"""          
