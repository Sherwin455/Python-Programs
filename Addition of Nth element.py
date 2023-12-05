l=list(map(int,input().split()))
n=int(input())
sum=0
if(list=='\0'):
    print("-1")
elif(n>len(l)):
    print("0")
else:
    for i in range(n-1,len(l),n):
        sum=sum+l[i]
    print(sum)
        

