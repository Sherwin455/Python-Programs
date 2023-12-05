Z PATTERN
l=input()
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if i==0 or i+j==len(l)-1 or i==len(l)-1:
            print(l[j],end=" ")
        else:
            print(" ",end=" ")
    print()
