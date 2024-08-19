#All are with respect to 0 index
#1st case (Printing the element at Nth row and Cth column)
matrix=[[1,1,1],[1,0,1],[1,1,1]]


row=[0]*len(matrix)        #initializing with zero to find the rows containing zero
column=[0]*len(matrix[0])   #initializing with zero to find the columns containing zero


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j]==0):
            row[i]=1
            column[j]=1

print(row)    # (0,1,0)
print(column) # (0,1,0)

for l in range(len(matrix)):
    for m in range(len(matrix[0])):
        if row[l] or column[m]:
            matrix[l][m]=0

print(matrix)