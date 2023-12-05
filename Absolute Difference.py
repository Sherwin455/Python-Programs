l=list(map(int,input().split()))
a=int(input())
diff=int(input())
c=0
for i in range(0,len(l)):
    if(abs(l[i]-a)<=diff):
            c=c+1 
print(c)
if(c==0):
    print("-1")
    
