def claimStairs(n):
    first = 1
    second = 2
    
    if n == 1 or n == 2:
        return n
    else:
        for i in range (2, n):
            temp = first
            first = second 
            second = temp + second
            # or
            # first , second = second , first + second
    return second
n = 5

print(claimStairs(n))