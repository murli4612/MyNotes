# [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
#   [0, 0, 0, 0, 0, 1, 1, 1, 1, 1



def move_zero_to_front(list1):
    
    n = len(list1)
    i ,j =0 , n
    while j < n:
        if list1[j] == 0:
            print(list1[i])
            list1[i], list1[j] = list1[j] , list1[i]
            i +=1
            
        j +=1
    return list1
            
    
list1 = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
# list1 = [0, 1, 0]

print(move_zero_to_front(list1))
    