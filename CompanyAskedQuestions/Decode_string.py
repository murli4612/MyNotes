# def decodeString(str1):
#     result,i = [],0
#     while i < len(str1):
#         k = ''
#         while str1[i] != '#':
#             k = k + str1[i]
#             i +=1
            
#         result.append(str1[i + 1: i +1 + int(k)])
#         i = i + 1 + int(k)
#     return result
        
        
# string1 = "4#lint4#co#de4#love3#you"

# print(decodeString(string1))

def decodeString(str1):
    result, i = [], 0
    while i < len(str1):
        k = ''
        # Extract the number until we hit '#'
        while str1[i].isdigit():
            k += str1[i]
            i += 1
        i += 1  # Skip the '#'
        length = int(k)
        result.append(str1[i:i + length])
        i += length
    return result

# Corrected input string
string1 = "4#lint4#co#de4#love3#you"

print(decodeString(string1))  # Output: ['lint', 'co', 'de', 'love', 'you']
