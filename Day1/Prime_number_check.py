n=12
list1=[]
i=1
count1=0
while(i*i<=n):
    if(n%i==0):
        count1+=1
        if(n/i!=i):
            count1+=1
            if(count1>2):
                print("not prime")
                break
    i+=1
if(count1==2):
    print(f"{n} is a prime number!")
