class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        l1=len(v1)
        l2=len(v2)
        if l1<l2:
            v1+=["0"]*(l2-l1)
            l1=l2
        else:
            v2+=["0"]*(l1-l2)
            l2=l1
        i=0
        #print(v1,v2)
        while(i<l1):
            try:
                a=int(v1[i].lstrip("0"))
            except:
                a=0
            try:
                b=int(v2[i].lstrip("0"))
            except:
                b=0
            if a<b:
                return -1
            elif a>b:
                return 1
            i+=1
        return 0
