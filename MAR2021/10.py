#attempt1:
class Solution:
    def intToRoman(self, num: int) -> str:
        ans=""
        di=[{1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'},\
        {1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'},\
        {1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'},{1:'M',2:'MM',3:'MMM'}]
        poww=0
        for i in str(num)[::-1]:
            if i=='0':
                poww+=1
                continue
            ans=di[poww][int(i)]+ans
            poww+=1
        return ans
        
            
