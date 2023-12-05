n=int(input())
m=int(input())
hcf=1
for i in range(1,max(n,m)):
    if (n%i==0 and m%i==0):
        hcf=i 
print(hcf)
