a=[0,0,1,2,1,0,1,0,1,2,1,0]

list1=[]

count0=0
count1=0
count2=0


for i in range(len(a)):
    if a[i]==0:
        count0+=1
    elif a[i]==1:
        count1+=1
    elif a[i]==2:
        count2+=1
print(count1,count2,count0)

for j in range(count0):
    list1.append(0)


for k in range(count1):
    list1.append(1)


for l in range(count2):
    list1.append(2)


print(list1)

