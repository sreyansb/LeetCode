#attempt2:
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class MyHashMap:
    def __init__(self):
        self.size=1000
        self.li=[None]*1005
        
    def put(self, key: int, value: int) -> None:
        index=key%self.size
        if self.li[index]==None:
            self.li[index]=Node(key,value)
        else:
            head=self.li[index]
            parent=None
            while(head and head.key!=key):
                parent=head
                head=head.next
            if head:
                head.value=value
            else:
                parent.next=Node(key,value)       

    def get(self, key: int) -> int:
        index=key%self.size
        head=self.li[index]
        while(head):
            if head.key==key:
                return head.value
            head=head.next
        return -1

    def remove(self, key: int) -> None:
        index=key%self.size
        head=self.li[index]
        parent=None
        while(head and head.key!=key):
            parent=head
            head=head.next
        if head:
            if parent:
                parent.next=head.next
            else:
                self.li[index]=head.next
            del head

#attempt1:
'''
class MyHashMap:

    def __init__(self):
        self.li=[-1]*((10**6)+1)        

    def put(self, key: int, value: int) -> None:
        self.li[key]=value
        

    def get(self, key: int) -> int:
        return self.li[key]
        

    def remove(self, key: int) -> None:
        self.li[key]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
'''
