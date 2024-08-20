list1=[[1,3],[2,6],[8,10],[15,18]]


n=len(list1)
list1.sort()

ans=[]


for i in range(n):
    if not ans or ans[-1][1]<list1[i][0]:
        ans.append(list1[i])  # adding if its not in the interval
    

    else:
        ans[-1][1]=max(ans[-1][1],list1[i][1])  # comparing and change only the 1st index


print(ans)



# arr=[[1,3],[2,6],[8,10],[15,18]]
# n = len(arr) # size of the array

# # sort the given intervals:
# arr.sort()

# ans = []

# for i in range(n):
#     # if the current interval does not
#     # lie in the last interval:
#     if not ans or ans[-1][1]<arr[i][0]:
#         ans.append(arr[i])
#     # if the current interval
#     # lies in the last interval:
#     else:
#         ans[-1][1] = max(ans[-1][1], arr[i][1])


# print(ans)

