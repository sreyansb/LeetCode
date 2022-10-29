#attempt2:
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        exact = zip(plantTime, growTime)
        exact = list(exact)
        exact.sort(key = lambda x:-x[1])
        plantT_last = 0
        total_time = 0
        # 1 0 0
        #   1 1 1 0 0
        #         1 1 0
        #             1 1 0
        #print(exact)
        for pTime,gTime in exact:
            plantT_last += pTime
            total_time = max(total_time,plantT_last + gTime)
        
        return total_time
            

#attempt1: WA because total_time can be greater 
'''
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        exact = zip(plantTime, growTime)
        exact = list(exact)
        exact.sort(key = lambda x:(-x[1],x[0]))
        plantT_last = 0
        total_time = 0
        # 1 0 0
        #   1 1 1 0 0
        #         1 1 0
        #             1 1 0
        for pTime,gTime in exact:
            plantT_last += pTime
            total_time = plantT_last + gTime
        
        return total_time
            
'''
