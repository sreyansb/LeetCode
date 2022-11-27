#ATTEMPT2: ONLY COPIED Didn't understand
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        print(n)
        liofdi=[{} for i in range(n)]
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]-nums[j] not in liofdi[i]:
                    liofdi[i][nums[i]-nums[j]]={}
                try:
                    for k in liofdi[j][nums[i]-nums[j]]:
                        if k+1 not in liofdi[i][nums[i]-nums[j]]:
                            liofdi[i][nums[i]-nums[j]][k+1]=0
                        liofdi[i][nums[i]-nums[j]][k+1]+=liofdi[j][nums[i]-nums[j]][k]
                except:
                    pass
                finally:
                    if 2 not in liofdi[i][nums[i]-nums[j]]:
                        liofdi[i][nums[i]-nums[j]][2]=0
                    liofdi[i][nums[i]-nums[j]][2]+=1
            for diff in liofdi[i]:
                for leng in liofdi[i][diff]:
                    deng=liofdi[i][diff][leng]
                    ans+=deng if leng>2 else 0
        return ans
                
                
            
        
