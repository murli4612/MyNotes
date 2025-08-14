# def allPalindromSubstring(s):
#     result =[]
    
#     for i in range(len(s)):
        
#         p1 = expandPalindrom(s,i,i)
#         result.append(p1)
#         p2 = expandPalindrom(s,i,i +1) 
#         print(p2)
#         result.append(p2)
#     return result       
# def expandPalindrom(s,l,r):
#     while  l >=0 and r < len(s) and s[l]== s[r]:
#         l -=1
#         r +=1
#         return s[l + 1: r]
    
# s ="aaa"
# print(allPalindromSubstring(s))
    
    
def allPalindromSubstring(s):
    result = []

    for i in range(len(s)):
        # Odd-length palindromes
        p1=expandPalindrom(s, i, i)
        result.append(s[i:p1])
        # Even-length palindromes
        p2=expandPalindrom(s, i, i + 1)
        result.append(s[i:p2])

    return result

def expandPalindrom(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        # result.append(s[l:r+1])
        l -= 1
        r += 1
        return r - l +1

# Example usage
s = "aaa"
print(allPalindromSubstring(s))
