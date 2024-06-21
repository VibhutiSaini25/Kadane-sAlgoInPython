def max_sub_sum(arr):
    if not arr:
        return 0
    max_so_far=arr[0]
    max_last=arr[0]
    for i in range(1,len(arr)):
        max_last=max(arr[i],max_last+arr[i])
        max_so_far=max(max_so_far,max_last)

    return max_so_far


arr=[1,2,3,-2,5]
print(max_sub_sum(arr))