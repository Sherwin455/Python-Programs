a=input()
b=[]
for i in range(len(a)):
    if(a.count(str(i))==int(a[i])):
        b.append(a[i])
        k=set(b)
print(len(k))
