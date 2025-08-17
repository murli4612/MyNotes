# def division_by_2_without_operator(n):
#     return (n & 1) == 0

# print(division_by_2_without_operator(4))
# print(division_by_2_without_operator(9))


# def reverse_word(s):
#     words = s.split()
#     reversed_word = words[::-1]
#     return ' '.join(reversed_word)



# input = "I am Murali"
# print(reverse_word(input))
# output = "Murali am I"
def charter_from_next_two(Char):
    # print(ord(Char),"oo")
    # if Char in ['X','Y','Z']:
    #     if Char =='X':
    #         return 'A'
    #     elif Char == 'Y':
    #         return 'B'
    #     elif Char == 'Z':
    #         return 'C'
    if Char.isupper():
        return chr((ord(Char) - ord('A') + 3) % 26 + ord('A'))
    
    # return chr(ord(Char) + 3 )

print(charter_from_next_two('A'))
print(charter_from_next_two('M'))
print(charter_from_next_two('Y'))

# A -> D
# M -> P
# Y -> B

# Let employemm table (name, salary)
# select name from employee order by salary Limit 2

class A:
    def __init__(a,b,c):
	    print(b,c)

# A()
# A(1)
A(1,2)