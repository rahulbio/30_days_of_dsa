N=780

i=2
list1=[]
while(i*i<=N):
    if(N%i==0):
        list1.append(i)
        while(N%i==0):
            N=N//i
    i+=1


if(N!=1):
    list1.append(N)


print(list1)