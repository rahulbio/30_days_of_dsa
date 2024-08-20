a=[1,2,3,-3,2,3,4,5,-2]
sum=0
maxi=float('-inf')
for i in range(len(a)):
    sum+=a[i]



    if(sum>maxi):
        maxi=sum
    
    if(sum<0):
        sum=0



print(f"The maximum sub array is {maxi}")