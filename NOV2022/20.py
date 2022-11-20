#attempt8:
class Solution:
    def calculate(self, s: str) -> int:
        number_stack = ["0"]
        operator_stack = []
        isPrevCharOperator = False
        def calculate_operator(operator,str1, str2):
            if operator == "+":
                return str(int(str1)+int(str2))
            else:
                return str(int(str1)-int(str2))

        for char in s:
            if char == " ":
                continue
            if char.isdigit():
                if isPrevCharOperator:
                    number_stack.append(char)
                else:
                    number_stack[-1] += char
                isPrevCharOperator = False
            else:
                if char == ")":
                    while(operator_stack[-1] != "("):
                        operator = operator_stack.pop()
                        str2,str1 = number_stack.pop(),number_stack.pop()
                        number_stack.append(calculate_operator(operator,str1,str2))
                    operator_stack.pop()
                    isPrevCharOperator = True
                elif char == "(":
                    number_stack.append("0")
                    operator_stack.append("(")
                    isPrevCharOperator = False
                else:
                    while(operator_stack and operator_stack[-1] != "("):
                        operator = operator_stack.pop()
                        str2,str1 = number_stack.pop(),number_stack.pop()
                        number_stack.append(calculate_operator(operator,str1,str2))
                    operator_stack.append(char)
                    isPrevCharOperator = True
            #print(s,number_stack,operator_stack)
        while(operator_stack):
            operator = operator_stack.pop()
            str2,str1 = number_stack.pop(),number_stack.pop()
            number_stack.append(calculate_operator(operator,str1,str2))
        
        try:
            return int("".join(number_stack))
        except:
            return int("".join(number_stack[1:]))
                        

#attempt1:  Runtime Error
'''
class Solution:
    def calculate(self, s: str) -> int:
        return eval(s)
'''
