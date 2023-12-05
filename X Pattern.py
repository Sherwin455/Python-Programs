l=input()
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if i==j or i+j==len(l)-1:
            print(l[i],end=" ")
        else:
            print(" ",end=" ")
    print()
