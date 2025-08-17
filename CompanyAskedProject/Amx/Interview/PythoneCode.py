# def move_spaces_to_front_swap(char_list):
#     n = len(char_list)
#     j = n - 1

#     # Traverse from end and move non-space characters to end using swaps
#     for i in range(n - 1, -1, -1):
#         if char_list[i] != ' ':
#             # Swap only if i != j to avoid unnecessary swaps
#             char_list[i], char_list[j] = char_list[j], char_list[i]
#             j -= 1

# # Example usage
# s = "move space front"
# char_list = list(s)
# move_spaces_to_front_swap(char_list)
# # print(''.join(char_list))
# import csv

# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', '30', 'New York, NY'],    # comma inside cell
#     ['Bob', '25', 'Los "Angeles"']      # quotes inside cell
# ]

# with open('output.csv', 'w', newline='') as f:
#     print("mm")
#     writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
#     writer.writerows(data)

# from collections import defaultdict

# count = defaultdict(int)
# count['a'] ="o"
# count['b'] += 1
# # count['a'] += 2
# print(count)  # {'a': 1, 'b': 1}

my_dict = {}

# Setting key-value pairs
my_dict["name"] = "Alice"
my_dict["age"] = 30
my_dict[42] = "answer"
my_dict[(1, 2)] = "tuple key"

print(my_dict["name"])     # Alice
print("age" in my_dict)    # True
print(len(my_dict))        # 4

# Iterating
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Deleting
del my_dict["age"]
my_dict.clear()  # Removes all entries





