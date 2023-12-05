l=list(map(int,input().split()))
even=[]
odd=[]

for i in range(0,len(l)):
    if(i%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
even.sort()
odd.sort()
print(even[len(even)-2]+odd[1])
        



