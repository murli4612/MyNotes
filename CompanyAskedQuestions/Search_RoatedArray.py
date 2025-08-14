def search_sorted_array(array, target):
    left , right = 0, len(array) - 1
    
    while left < right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        #right part sorted
        if array[left] >= array[mid]:
            if target > array[mid] and target < array[left]:
                left = mid + 1
            else:
                right  = mid - 1
                
            
        #left part sorted
        else:
            if target > array[mid] and target > array[right]:
                left = mid + 1
            else:
                right = mid -1
    return -1
                
# array =  [4,5,6,7,8,1,2]   
array =  [7,8,1,2,4,5,6]   
target = 8
index =search_sorted_array(array, target)
print(array[index])      
            
# # Example : [4,5,6,7,8,1,2]
# Algo:
#     step 1) find the part which is sorted:
#     step 2) then we need to identify which part target should present , left or right of mid

 #left sorted array
        # if array[left] <= array[mid]:
        #     if target > array[mid] or target < array[left]:
        #         left = mid + 1
        #     else:
        #         right = mid + 1
        # #right sorted array
        # else:
        #     if target < array[mid] or target > array[right]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1