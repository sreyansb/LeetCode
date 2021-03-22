#attempt2:create a dictionary again for checking if vowels can be replaced by *
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordlist1=set(wordlist)
        worddict={}
        worddict1={}
        
        for i in wordlist:
            k=i.lower()
            if k not in worddict:
                worddict[k]=[i]
            #worddict[k].append(i)
            j=k.replace("a",'*').replace("e","*").replace("i","*").replace("o","*").replace("u","*")
            if j not in worddict1:
                worddict1[j]=[]
            worddict1[j].append(i)
        
        #print(worddict1)
        ans=[]
        vowels={'a','e','i','o','u'}
        
        for i in queries:
            anss=""
            number=1
            if i in wordlist1:
                ans.append(i)
                continue
                
            k=i.lower()
            if k in worddict:
                anss=worddict[k][0]
                ans.append(anss)
                continue
            
            k=k.replace("a",'*').replace("e","*").replace("i","*").replace("o","*").replace("u","*")
            if k in worddict1:
                ans.append(worddict1[k][0])
            else:
                ans.append("")
        return ans        

#attempt1:TLE: problem yeh hai ki
'''
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordlist1=set(wordlist)
        ans=[]
        vowels={'a','e','i','o','u'}
        for i in queries:
            anss=""
            number=1
            if i in wordlist1:
                ans.append(i)
                continue
            for j in wordlist:
                if i.lower()==j.lower():
                    anss=j
                    break
                if len(i)!=len(j):
                    continue
                k,l=i.lower(),j.lower()
                flag=1
                if number:
                    for m in range(len(k)):
                        if l[m]!=k[m]:
                            if k[m] in vowels and l[m] in vowels:
                                pass
                            else:
                                flag=0
                                break
                    if flag:
                        anss=j
                        number=0
            ans.append(anss)
        return ans
        
'''
