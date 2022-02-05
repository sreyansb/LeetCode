#attempt4: TOOK HINT : Improved attempt1: Use index of the linked list instead
#of the node itself
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush,heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        finnode = ListNode()
        finnodec = finnode
        for i,n in enumerate(lists):
            val = float('inf')
            if lists[i]:
                val = lists[i].val
            heappush(heap,(val,i))
        while(heap and heap[0][0]!=float('inf')):
            val,index = heappop(heap)
            finnode.next = ListNode(val)
            finnode = finnode.next
            lists[index] = lists[index].next
            node = lists[index]
            val1 = float('inf')
            if node:
                val1 = node.val
            heappush(heap,(val1,index))
            
        return finnodec.next

#attempt3: 6324ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
        def notnullall(a):
            for i in a:
                if i:
                    return True
            return False
        def findmin(a):
            minval = float('inf')
            minnode = -1
            for i in a:
                if i[0]<minval:
                    minval = i[0]
                    minnode = i[1]
            return (minval,minnode)
        heap = set()
        finnode = ListNode()
        finnodec = finnode
        for i in lists:
            if i:
                heap.add((i.val,i))
        while(notnullall(heap)):
            nextmin = findmin(heap)
            finnode.next = ListNode(nextmin[0])
            finnode = finnode.next
            heap.remove(nextmin)
            newnode = nextmin[1].next
            if newnode:
                heap.add((newnode.val,newnode))        
        
        return finnodec.next

#attempt2: 5130ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
        def notnullall(a):
            for i in a:
                if i:
                    return True
            return False
        def findmin(a):
            minval = float('inf')
            minnode = -1
            for i in a:
                if i[0]<minval:
                    minval = i[0]
                    minnode = i[1]
            if minval == float('inf'):
                return tuple()
            return (minval,minnode)
        heap = set()
        finnode = ListNode()
        finnodec = finnode
        for i in lists:
            if i:
                heap.add((i.val,i))
        while(True):
            nextmin = findmin(heap)
            if not(nextmin):
                break
            finnode.next = ListNode(nextmin[0])
            finnode = finnode.next
            heap.remove(nextmin)
            newnode = nextmin[1].next
            if newnode:
                heap.add((newnode.val,newnode))        
        return finnodec.next

#attempt1: Tried using heapq but doesn't work since ListNode doesn't support
#lessthanorequal(__le__) and lessthan (__lt__) functions
#both heapq and SortedList don't work
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush,heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        finnode = ListNode()
        finnodec = finnode
        for i in lists:
            val = float('inf')
            if i:
                val = i.val
            heappush(heap,(val,i))
        while(heap[0][0]!=float('inf')):
            val,node = heappop(heap)
            finnode.next = node
            finnode.next.next = None
            finnode = finnode.next
            val = float('inf')
            if node:
                val = node.val
            heappush(heap,(val,node))
        return finnodec.next
'''
