def find_min_index(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return low  # index of minimum

# ✅ Test
arr1 = [3, 4, 5, 6, 1, 2]
index1 = find_min_index(arr1)
print("Minimum element:", arr1[index1])  # Output: 1
print("Index:", index1)                  # Output: 4



def find_min_index_with_duplicates(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] < arr[high]:
            high = mid
        else:
            high -= 1  # cannot decide, safely reduce high

    return low  # index of minimum

# ✅ Test
arr2 = [2, 2, 2, 0, 1, 2]
index2 = find_min_index_with_duplicates(arr2)
print("Minimum with duplicates:", arr2[index2])  # Output: 0
print("Index:", index2)                          # Output: 3
