#1. Given n and c, find the element at the N and C


N=5
C=4


#      1 
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1 
# 1 5 10 10 5 1 


res=1
for i in range(C):
    res=res*(N-i)
    res=res//(i+1)

print(res)
