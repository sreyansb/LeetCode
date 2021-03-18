#attempt2: 1st one was WA because if n<3 the return should be len(set(nums)) and not n
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return len(set(nums))
        if len(set(nums))==1:
            return 1            
        sols=[2 for i in range(n)]
        i=n-3
        anys="any"
        adds="add"
        subs="sub"
        try:
            sols[-2]=[2,(nums[-2]-nums[-1])//(abs(nums[-2]-nums[-1]))]
        except:
            sols[-2]=[1,0]
        #sols[-2][1] represents difference between consecutive terms first one-second one
        #increasing sequence means -1 and decreasing sequence is 1
        while(i>-1):
            j=i+1
            symb,sign=0,0
            answ=2
            while(j<n-1):
                try:
                    sign=(nums[i]-nums[j])//abs(nums[i]-nums[j])
                    if sign==sols[j][-1]*-1:
                        answ=max(answ,sols[j][0]+1)
                        if answ==sols[j][0]+1:
                            symb=sign
                    elif sols[j][-1]==0:
                        answ=max(answ,2)
                        if answ==2:
                            symb=sign
                except:
                    pass
                j+=1
            if symb:
                sols[i]=[answ,symb]
            else:
                sols[i]=[answ,sign]
            i-=1
        return sols[0][0]
            
                
                
