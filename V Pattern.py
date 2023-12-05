V PATTERN
l=input()
m=len(l)*2-2
for i in range(0,len(l)):
    for j in range(m+1):
        if i==j or i+j==m:
            print(l[i],end=" ")
        else:
            print(" ",end=" ")
    print("")
