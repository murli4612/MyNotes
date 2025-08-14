
import os
my_file = os.path.join('A', 'B', 'C', 'ABCbook.txt')
def merge_sort(arr):
    # base condition
    
    if len(arr) <=1:
        with open("file.txt", "w") as f:
            f.write(arr)
    
    with open("file.txt", "r") as f:
        lines = len(f.readlines())
        mid = lines//2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
    return merge(left_half , right_half)

def merge(left,right):
    sorted_arry = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arry.append(left[i])
            i +=1
        else:
            sorted_arry.append(right[j])
            j +=1
    sorted_arry.extend(left[i:])
    sorted_arry.extend(right[j:])
    return sorted_arry
    



def file_read(input_file,path):
    
    with open(input_file_file) as f:
    # your code to work on the file goes here
        result = []
        for line in f:
            result = merge_sort(line)
    
    








arr = [3,9,1,4,5]

print(merge_sort(arr))