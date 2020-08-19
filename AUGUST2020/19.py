class Solution:
    def toGoatLatin(self, S: str) -> str:
        li=S.split()
        s="a"
        for i in range(len(li)):
            if li[i][0]=='a' or li[i][0]=='e' or li[i][0]=='i' or li[i][0]=='o' or li[i][0]=='u' or li[i][0]=='A' or li[i][0]=='E' or li[i][0]=='I' or li[i][0]=='O' or li[i][0]=='U':
                li[i]+="ma"+s
            else:
                li[i]=li[i][1:]+li[i][0]+"ma"+s
            s+="a"
        return " ".join(li)
                
        
