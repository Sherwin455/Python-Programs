n=input()
i=0
j=len(n)-1
m=[]
while(i<len(n) ):
    while(i<len(n) and n[i]!=n[j]):
        m.append(n[i])
        i+=1  
    j-=1  
    i+=1
for k in range(len(m)-1,-1,-1):
    print(m[k],end="")
