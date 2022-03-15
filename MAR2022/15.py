#attempt1: 76ms Unused open parentheses from the end have to be consumed first
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_parentheses_number = 0
        elements = []
        for i in s:
            toadd = 1
            if i == "(":
                open_parentheses_number += 1
            elif i == ")":
                if open_parentheses_number:
                    open_parentheses_number -= 1
                else:
                    toadd = 0
            if toadd :
                elements.append(i)
        final = "".join(elements)[::-1].replace("(","",open_parentheses_number)
        return final[::-1]
                
        
