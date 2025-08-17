def second_max(list_A):
    
    if len(list_A) < 2:
        return None
    
    max_val = float('-inf')
    second_max = float('-inf')
    for number in list_A:
        if number > max_val:
            second_max = max_val
            max_val = number
            
        elif number > second_max and number != max_val:
            second_max = number
    return second_max 
            
    
    
arrayA = [-1,-3, -2,-10]

print(second_max(arrayA))