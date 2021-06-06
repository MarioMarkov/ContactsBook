
#
# def partition(data,left,right):
#     pivot = data[left]
#     left_index = left+1
#     right_index = right
#
#     while True:
#         while left_index<=right_index and data[left_index]<=pivot:
#             left_index+=1
#
#         while right_index >= left_index and data[right_index] >= pivot:
#             right_index -= 1
#         if(right_index<=left_index):
#             break
#         data[left_index],data[right_index] = data[right_index], data[left_index]
#         print(data)
#
#     data[left],data[right_index]= data[right_index],data[left]
#     print(data)
#     return right_index
#
# def quicksort(data,left,right):
#     if(right<=left):
#         return
#     else:
#         pivot = partition(data,left,right)
#         quicksort(data,left,pivot-1)
#         quicksort(data,pivot+1,right)
#
# quicksort(data,0,len(data)-1)

data = [9,5,7,4,2,8,1,10,6,3]
def partition(arr,l,r):
    pivot =arr[r]
    i= l-1
    for j in range(l,r):
        if (arr[j]<pivot):
            i= i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[r] = arr[r],arr[i+1]

    # index of pivot
    return i+1

def quicksort(arr,l,r):
    if (l>=r):
        return
    pivot  = partition(arr,l,r)
    # for left of the pivot
    quicksort(arr,l,pivot-1)
    # for right of the pivot
    quicksort(arr,pivot+1,r)



quicksort(data,0,len(data)-1)
print(data)




