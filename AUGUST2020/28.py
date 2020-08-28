#1st attempt -> slow  but it was hit and miss, I changed number of rand7()
#continuously and then found the answer.

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        return (rand7()+rand7()+rand7()+rand7()+rand7()+rand7()+rand7())%10+1
            
        
        
