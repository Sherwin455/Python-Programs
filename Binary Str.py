s=input()
res=int(s[0])
for i in range(1,len(s)):
    if(s[i]=="A"):
        res=res&int(s[i+1])
    elif(s[i]=="B"):
        res=res|int(s[i+1])
    elif(s[i]=="C"):
        res=res^int(s[i+1])
print(res)
        
        
