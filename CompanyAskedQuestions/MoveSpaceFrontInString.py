def moveSpaceFront(s):
    chars = list(s)
    length  = len(s) -1
    for i in range(length , -1 ,-1):
        if chars[i] != ' ':
            chars[i],chars[length] = chars[length], chars[i]
            length-=1
    return ''.join(chars)

s ="ab ff gg kk"
print(moveSpaceFront(s))
            