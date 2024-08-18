N=30

list1=[ True for _ in range(N+1)]

i=2

while(i*i<=N):
    if list1[i]:
        for j in range(i*i,N+1,i):
            list1[j]=False
    i+=1


list2=[]

for element in range(2,N+1):
    if(list1[element]):
        list2.append(element)

print(f"The prime numbers till 30 are {list2}")