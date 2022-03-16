#attempt2:
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_index = 0
        pop_index = 0
        n = len(pushed)
        while(push_index<n):
            stack.append(pushed[push_index])
            push_index += 1
            while(stack and stack[-1] == popped[pop_index]):
                stack.pop()
                pop_index += 1
        while(pop_index<n):
            if stack[-1] != popped[pop_index]:
                break
            stack.pop()
            pop_index += 1
        return not(stack)
                
        

#attempt1: WA because you need to pop as long as top element == head of popped
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_index = 0
        pop_index = 0
        n = len(pushed)
        while(push_index<n):
            stack.append(pushed[push_index])
            push_index += 1
            if stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        while(pop_index<n):
            if stack[-1] != popped[pop_index]:
                break
            stack.pop()
            pop_index += 1
        return not(stack)
'''
