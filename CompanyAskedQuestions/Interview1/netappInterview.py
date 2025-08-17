# arr=[2,3,5,8,9]     k =3
# output = 7

def find_k_missing_numbers(arrayA, k):
    missingA = []
    num_set = set(arrayA)
    i = 1
    while len(missingA) < k:
        if i not in num_set and i > arrayA[0]:
            missingA.append(i)
        i +=1
    return missingA[k-1]
  
            
arr=[2,3,5,8,9]   
k =3
find_k_missing_numbers(arr,k)
        
        