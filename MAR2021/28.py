#attempt1:
class Solution:
    def originalDigits(self, s: str) -> str:
        nustr={0:"zero",6:"six",8:"eight",4:"four",2:"two",1:"one",3:"three",5:"five",7:"seven",9:"nine"}
        ans=[]
        counts={}
        for i in s:
            if i not in counts:
                counts[i]=0
            counts[i]+=1
        if 'z' in counts:#zero goes
            ans.extend(['0']*counts['z'])
            counts['e']-=counts['z']
            counts['r']-=counts['z']
            counts['o']-=counts['z']
            counts['z']=0
        if 'x' in counts:#six goes
            ans.extend(['6']*counts['x'])
            counts['i']-=counts['x']
            counts['s']-=counts['x']
            counts['x']=0
        if 'g' in counts:#eight goes
            ans.extend(['8']*counts['g'])
            counts['e']-=counts['g']
            counts['i']-=counts['g']
            counts['h']-=counts['g']
            counts['t']-=counts['g']
            counts['g']=0
        if 'u' in counts:#4 goes
            ans.extend(['4']*counts['u'])
            counts['o']-=counts['u']
            counts['f']-=counts['u']
            counts['r']-=counts['u']
            counts['u']=0
        if 'w' in counts:#2 goes
            ans.extend(['2']*counts['w'])
            counts['t']-=counts['w']
            counts['o']-=counts['w']
            counts['w']=0
        if 'o' in counts and counts['o']:#1 goes
            ans.extend(['1']*counts['o'])
            counts['n']-=counts['o']
            counts['e']-=counts['o']
            counts['o']=0
        if 't' in counts and counts['t']:#1 goes
            ans.extend(['3']*counts['t'])
            counts['h']-=counts['t']
            counts['e']-=2*counts['t']
            counts['r']-=counts['t']
            counts['t']=0
        if 'f' in counts and counts['f']:#1 goes
            ans.extend(['5']*counts['f'])
            counts['i']-=counts['f']
            counts['e']-=counts['f']
            counts['v']-=counts['f']
            counts['f']=0
        if 'v' in counts and counts['v']:#1 goes
            ans.extend(['7']*counts['v'])
            counts['s']-=counts['v']
            counts['e']-=2*counts['v']
            counts['n']-=counts['v']
            counts['v']=0
        if 'i' in counts and counts['i']:
            ans.extend(['9']*counts['i'])
        return "".join(sorted(ans))
