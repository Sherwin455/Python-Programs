n=input()
f=0
for i in range(len(n)):
    if(n[i]=='4' or n[i]=='7'):
            f=1 
    else:
        f=0
        break
if f==1:
    print("lucky num")
else:
    print("unlucky")
