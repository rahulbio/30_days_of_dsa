a= [7,1,5,3,6,4]

left=0
right=1

max_p=0

while(right<len(a)):
    if(a[left]>a[right]):
        left=right
    else:
        max_p=max(max_p,a[right]-a[left])
    
    right+=1



print(max_p)