class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        if num_people==0 or candies==0:
            return [0]*num_people
        ans=[0]*num_people
        index=0
        number=1
        total=0
        while(total<=candies):
            ans[index]+=min(number,candies-total)
            total+=number
            number+=1
            index=(index+1)%num_people
            #print(index,ans)
        return ans
        
        
