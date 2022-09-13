#attempt2:
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        index = 0
        n = len(data)
        
        def checkMaskValue(mask,value):
            str_bin_value = str(bin(value))[2:]
            str_bin_value = "0"*(8-len(str_bin_value))+str_bin_value
            return str_bin_value.startswith(mask)
        
        def checkSecondaryMask(value):
            secondaryMask = "10"
            return checkMaskValue(secondaryMask,value)
        
        def checkFor1(value):
            mask = "0"
            return checkMaskValue(mask,value)
        
        def checkFor2(value,secondValue):
            mask = "110"
            return (checkMaskValue(mask,value) and checkSecondaryMask(secondValue))
        
        def checkFor3(value,secondValue,thirdValue):
            mask = "1110"
            return (checkMaskValue(mask,value) and checkSecondaryMask(secondValue) and checkSecondaryMask(thirdValue))
        
        def checkFor4(value,secondValue,thirdValue,fourthValue):
            mask = "11110"
            return (checkMaskValue(mask,value) and checkSecondaryMask(secondValue) and checkSecondaryMask(thirdValue) and checkSecondaryMask(fourthValue))
        
        while(index < n):
            if checkFor1(data[index]):
                index += 1
            elif index+1<n and checkFor2(data[index],data[index+1]):
                index += 2
            elif index+2<n and checkFor3(data[index],data[index+1],data[index+2]):
                print("here")
                index += 3
            elif index+3<n and checkFor4(data[index],data[index+1],data[index+2],data[index+3]):
                index += 4
            else:
                return False
        return True
                
            

#attempt1: WA Spelling Mistake
'''
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        index = 0
        n = len(data)
        
        def checkMaskValue(mask,value):
            str_bin_value = str(bin(value))[2:]
            str_bin_value = "0"*(8-len(str_bin_value))+str_bin_value
            return str_bin_value.startswith(mask)
        
        def checkSecondaryMask(value):
            secondaryMask = "10"
            return checkMaskValue(secondaryMask,value)
        
        def checkFor1(value):
            mask = "0"
            return checkMaskValue(mask,value)
        
        def checkFor2(value,secondValue):
            mask = "110"
            return (checkMaskValue(mask,value) and checkSecondaryMask(secondValue))
        
        def checkFor3(value,secondValue,thirdValue):
            mask = "1110"
            return (checkMaskValue(mask,value) and checkSecondaryMask(secondValue) and checkSecondaryMask(thirdValue))
        
        def checkFor4(value,secondValue,thirdValue,fourthValue):
            mask = "11110"
            return (checkMaskValue(mask,value) and checkSecondaryMask(secondValue) and checkSecondaryMask(thirdValue) and checkSecondaryValue(fourthValue))
        
        while(index < n):
            if checkFor1(data[index]):
                index += 1
            elif index+1<n and checkFor2(data[index],data[index+1]):
                index += 2
            elif index+2<n and checkFor3(data[index],data[index+1],data[index+2]):
                print("here")
                index += 3
            elif index+3<n and checkFor4(data[index],data[index+1],data[index+2],data[index+3]):
                index += 4
            else:
                return False
        return True
'''
