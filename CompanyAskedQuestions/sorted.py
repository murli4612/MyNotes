# people = {
#     "item": [
#         {'name': 'Bob', 'age': 25},
#         {'name': 'Alice', 'age': 30},
#         {'name': 'Charlie', 'age': 35}
#     ]
# }

# # Sorting the list of dictionaries based on 'age' in descending order
# sorted_people_desc = sorted(people["item"], key=lambda x: x['age'], reverse=True)

# print(sorted_people_desc)


# people1 =[
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Charlie', 'age': 35}
# ]

# sorted_people_desc = sorted(people1, key=lambda x: x['age'], reverse=True)
# print(sorted_people_desc)


# from functools import reduce
# words = ["apple", "banana", "cat", "do", "elephant", "giraffe"]
# # Step 1: Filter - Keep words with more than two characters
# filtered_words = filter(lambda word: len(word) > 2, words)
# word_lengths = list(map(len, filtered_words))
# print(word_lengths)


# matrix = [["apple", "banana", "cherry"],
# ["date", "fig", "grape"],
# ["kiwi", "lemon", "mango"]]
# modified_matrix = [fruit.capitalize() for row in matrix for fruit in row]
# print(modified_matrix)
# #

def remove_non_alpha_chars(s):
    chars = list(s)
    i = 0
    while i < len(chars):
        if not chars[i].isalpha():
            # print("nnn", i)
            chars.pop(i)
        else:
            # print("ttt", i)
            i += 1
    return ''.join(chars)
s = "$Gee*k;s..1fo, r'Ge^eks?"
print(remove_non_alpha_chars(s))

# import requests
# # Make a request to a JSON API
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# print(response,"res--")
# # Parse the JSON response
# json_data = response.json()
# print(json_data,"jjjj")
# # Access specific data from the JSON
# print("Title:", json_data['title'])

# import json
# # Read configuration from JSON file
# with open('config.json', 'r') as file:
#     config = json.load(file)