#attempt1:
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        #create a suffix tree
        di={}
        for i in words:
            k=di
            for j in i[::-1]:
                if j not in k:
                    k[j]={}
                k=k[j]
            k['#']=1
        #print(di)
        count=0
        def countmax(d,number):
            if '#' in d and len(d.keys())==1:
                return number+1
            maxie=0
            for j in d:
                if j!='#':
                    maxie+=countmax(d[j],number+1)
            return maxie
                
        for i in di:
            count+=countmax(di[i],1)
        return count
        
