def removeAdjacentDuplicate(s, k):
    stack = []  # Each element is [char, count]

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])
        
        if stack[-1][1] == k:
            stack.pop()

    # Reconstruct string
    res = ""
    for char, count in stack:
        res += char * count
    return res

s = "deeedbbcccbdaa"
k = 3
print(removeAdjacentDuplicate(s, k))
