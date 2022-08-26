#attempt1:
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powersOf2 = []
        powerOf2 = 1
        def allDigits(number):
            di = {}
            for i in str(number):
                if i not in di:
                    di[i] = 0
                di[i] += 1
            return di
        while(powerOf2 <= (10**10)):
            powersOf2.append(allDigits(powerOf2))
            powerOf2 <<= 1
        nDigitSet = allDigits(n)
        #print(nDigitSet,powersOf2)
        for digitSet in powersOf2:
            if nDigitSet == digitSet:
                #print(digitSet,nDigitSet)
                return True
        return False
        
        
            
        
