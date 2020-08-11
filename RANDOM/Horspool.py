def shifttable(pattern):
    m=len(pattern)
    dic={}
    i='A'
    while(i<='Z'):
        dic[i]=m
        i=chr(ord(i)+1)
    dic[" "]=m
    for i in range(m-1):
        dic[pattern[i]]=m-1-i
    return dic

text="JIM SAW ME IN A BARBERSHOP"
pattern="BARBER"
dic=shifttable(pattern)
print(dic)
i=len(pattern)-1
while(i<len(text)):
    k=0
    while(k<len(pattern) and pattern[len(pattern)-1-k]==text[i-k]):
        k+=1
    if k==len(pattern):
        print("final",i-len(pattern)+1)
        break
    else:
        print("i",k,i,text[i-k],text[i],dic[text[i]],pattern[len(pattern)-1-k])
        i+=dic[text[i]]
        print(i)

    
