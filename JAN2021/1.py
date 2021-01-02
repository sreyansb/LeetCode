#attempt 1: Had an error in logic such that the elements of pieces which
#have length>1 should be continuous in arr
#this is correct solution
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for i in pieces:
            if len(i)==1:
                if not(arr.count(i[0])):
                    return False
            else:
                positions=[]
                for j in i:
                    if arr.count(j):
                        positions.append(arr.index(j))
                    else:
                        return False
                if positions!=sorted(positions):
                    return False
                for i in range(1,len(positions)):
                    if positions[i]!=positions[i-1]+1:
                        return False
        return True
        
