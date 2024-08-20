a=[[1,2,3],
   [4,5,6],
   [7,8,9]]



for i in range(len(a)):
    for j in range(i+1,len(a[0])):
        a[i][j],a[j][i]=a[j][i],a[i][j]


print(a)
