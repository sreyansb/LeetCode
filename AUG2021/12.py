#attempt1:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di={}
        for i in strs:
            k="".join(sorted(i))
            if k not in di:
                di[k]=[]
            di[k].append(i)
        ans=[]
        for i in di:
            ans.append(di[i])
        return ans