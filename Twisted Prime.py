def Twisted(n):
    n=int(n)
    c=0
    for i in range (2,n+1):
        if(n%i==0):
            c+=1 
    if c==2:
        return(True)
    else:
        return("Non Prime")  
n=input()
if(Twisted(n) and Twisted(n[::-1])):
    print(True)
else:
    print(False)

