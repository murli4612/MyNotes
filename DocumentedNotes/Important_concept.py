To delete K consecutive duplicate characters from a string, we can use a stack-based approach.

🔹 Approach: Stack-Based Solution
Use a stack to store characters along with their frequency.
Traverse the string and push each character onto the stack:
If the top of the stack has the same character, increase its count.
If the count reaches K, remove that character from the stack.
Construct the final string from the remaining characters in the stack.

✅ Python Implementation
def remove_k_consecutive_duplicates(s, k):
    stack = []  # Stack to store (character, frequency)

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1] = (char, stack[-1][1] + 1)  # Increment count
        else:
            stack.append((char, 1))  # Push new character

        if stack[-1][1] == k:  # Remove if count reaches K
            stack.pop()

    # Reconstruct string from stack
    return "".join(char * count for char, count in stack)

# ✅ Example Usage
s = "deeedbbcccbdaa"
k = 3
print(remove_k_consecutive_duplicates(s, k))  
# 🔥 Output: "aa"



🔹 Explanation with Example
Input: "deeedbbcccbdaa", K = 3
Step	Stack Content	Action
d	[(d,1)]	Add 'd'
e	[(d,1), (e,1)]	Add 'e'
e	[(d,1), (e,2)]	Increment count
e	[(d,1), (e,3)]	Count = 3, Remove
d	[(d,1), (d,1)]	Add 'd'
b	[(d,1), (d,1), (b,1)]	Add 'b'
b	[(d,1), (d,1), (b,2)]	Increment count
c	[(d,1), (d,1), (b,2), (c,1)]	Add 'c'
c	[(d,1), (d,1), (b,2), (c,2)]	Increment count
c	[(d,1), (d,1), (b,2), (c,3)]	Count = 3, Remove
b	[(d,1), (d,1), (b,2), (b,1)]	Add 'b'
d	[(d,1), (d,1), (b,2), (b,1), (d,1)]	Add 'd'
a	[(d,1), (d,1), (b,2), (b,1), (d,1), (a,1)]	Add 'a'
a	[(d,1), (d,1), (b,2), (b,1), (d,1), (a,2)]	Increment count
Final Output: "aa"





🔹 Time Complexity
O(N) → Each character is processed once.
O(N) space for the stack.


1. Creating a Generator Function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1  # State is maintained

# Using the generator
gen = count_up_to(5)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

for num in gen:
    print(num)  # Output: 3, 4, 5



2. Generator Expressions (Like List Comprehension)
gen_exp = (x**2 for x in range(5))
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1



3. Infinite Generators
Useful for creating infinite sequences like Fibonacci numbers.


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(5):
    print(next(fib_gen))  # Output: 0, 1, 1, 2, 3



4. Generator vs List Performance
Generators are faster and use less memory than lists.

import sys

lst = [x**2 for x in range(1000000)]
gen = (x**2 for x in range(1000000))

print(sys.getsizeof(lst))  # Large memory usage
print(sys.getsizeof(gen))  # Small memory usage



Using yield from (Nested Generators)
If a generator calls another generator, we can use yield from.

def generator1():
    yield from [1, 2, 3]

def generator2():
    yield from generator1()
    yield from [4, 5]

for num in generator2():
    print(num)




3. Returning Values from Decorated Functions

If the original function returns a value, ensure the wrapper returns it.
def square_decorator(func):
    def wrapper(n):
        result = func(n)
        return result * result
    return wrapper

@square_decorator
def get_number(n):
    return n

print(get_number(4))  # Output: 16


4. Using functools.wraps (Preserves Original Function Metadata)
When using decorators, the original function’s __name__ and __doc__ might be lost. Use functools.wraps() to fix this

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is an example function."""
    print("Example function running")

print(example.__name__)  # Output: example
print(example.__doc__)   # Output: This is an example function.



Example 1: Filter Dictionary by Value
✅ Keep only items where the value is greater than 
data = {"a": 10, "b": 60, "c": 30, "d": 80, "e": 90}

filtered_data = {key: value for key, value in data.items() if value > 50}
print(filtered_data)

Output:
{'b': 60, 'd': 80, 'e': 90}


Example 2: Filter Dictionary Based on a Specific Key-Value Condition
✅ Keep only items where the value is "active"

users = {"Alice": "active", "Bob": "inactive", "Charlie": "active", "David": "pending"}

active_users = {key: value for key, value in users.items() if value == "active"}
print(active_users)

out:
{'Alice': 'active', 'Charlie': 'active'}


Example 3: Filter Nested Dictionary
✅ Keep employees with a salary greater than 50000

employees = {
    "John": {"age": 25, "salary": 40000},
    "Jane": {"age": 28, "salary": 55000},
    "Mike": {"age": 30, "salary": 60000},
}

filtered_employees = {k: v for k, v in employees.items() if v["salary"] > 50000}
print(filtered_employees)

output:
{'Jane': {'age': 28, 'salary': 55000}, 'Mike': {'age': 30, 'salary': 60000}}

Example 4: Using filter() Function

data = {"a": 10, "b": 60, "c": 30, "d": 80, "e": 90}

filtered_data = dict(filter(lambda item: item[1] > 50, data.items()))
print(filtered_data)

output:
{'b': 60, 'd': 80, 'e': 90}


✅ Best Approach?

Dictionary Comprehension is the most readable and efficient.
filter() can be useful for functional programming.


2️⃣ Filter Nested Dictionary (Multiple Levels)
✅ Example: Remove students with marks < 50 in any subject

students = {
    "Alice": {"math": 80, "science": 90},
    "Bob": {"math": 45, "science": 55},
    "Charlie": {"math": 60, "science": 40},
}

filtered_students = {name: subjects for name, subjects in students.items() if all(marks >= 50 for marks in subjects.values())}
print(filtered_students)

output:

{'Alice': {'math': 80, 'science': 90}}


3️⃣ Recursive Filtering for Deeply Nested Dictionary
✅ Example: Remove values below a threshold in deeply nested dict

def filter_nested(d, threshold=50):
    if isinstance(d, dict):
        return {k: filter_nested(v, threshold) for k, v in d.items() if isinstance(v, dict) or v >= threshold}
    return d

data = {
    "A": {"math": 80, "science": 90},
    "B": {"math": 45, "science": 55},
    "C": {"math": 60, "science": {"physics": 40, "chemistry": 85}},
}

filtered_data = filter_nested(data, 50)
print(filtered_data)

output:
    
{
    'A': {'math': 80, 'science': 90},
    'C': {'math': 60, 'science': {'chemistry': 85}}
}

4️⃣ Using filter() for Nested Dictionary

data = {
    "A": {"math": 80, "science": 90},
    "B": {"math": 45, "science": 55},
    "C": {"math": 60, "science": {"physics": 40, "chemistry": 85}},
}

filtered_data = {k: dict(filter(lambda item: item[1] >= 50 if isinstance(item[1], int) else True, v.items())) for k, v in data.items()}
print(filtered_data)

Output:

{
    'A': {'math': 80, 'science': 90},
    'B': {'science': 55},
    'C': {'math': 60, 'science': {'chemistry': 85}}
}


def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()  # Sort intervals based on the start time
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        
        if start <= last_end:
            merged[-1][1] = max(last_end, end)  # Merge overlapping intervals
        else:
            merged.append([start, end])  # Add non-overlapping interval
    
    return merged

# Example usage
intervals = [[1,3],[2,4],[5,6],[8,10]]
result = merge_intervals(intervals)
print(result)  # Output: [[1, 4], [5, 6], [8, 10]]




def filter_value(users):
    result = {}

    for user in users:
        profile = user.get("profile", {})
        if user.get("active") and "city" in profile:
            city = profile["city"].lower()
            name = profile["name"].lower()

            if city not in result:
                result[city] = []

            result[city].append(name)

    return result

users = [
    {"profile": {"name": "Tushar", "email": "tushar@datahash.com", "city": "bangalore"}, "active": True},
    {"profile": {"name": "Sachin", "email": "sachin@datahash.com", "city": "bangalore"}, "active": True},
    {"profile": {"name": "Rahul", "email": "rahul@datahash.com", "city": "gurgaon"}, "active": False},
    {"profile": {"name": "Sid", "email": "sid@datahash.com", "city": "gurgaon"}, "active": True},
    {"profile": {"name": "John", "email": "john@datahash.com"}, "active": True}
]

output = filter_value(users)
print(output)

#output
{"bangalore": ["tushar", "sachin"], "gurgaon": ["sid"]}
    
    
    
 data = [
    {"hostname": "10.16.08.09", "Candidate": "Rajat", "password": "asdadwf"},
    {"hostname": "", "Candidate": "Rajat1", "password": ""},
    {"hostname": "", "Candidate": "Rajat1", "password": ""},
    {"hostname": "", "Candidate": "Rajat1", "password": ""},
]

# Step 1: Create a dictionary to store the frequency of each candidate
candidate_counts = {}

# Step 2: Iterate through the data and count occurrences manually
for item in data:
    candidate = item.get("Candidate", "").strip()  # Get candidate name, handle missing keys
    if candidate:  # Ignore empty candidate names
        candidate_counts[candidate] = candidate_counts.get(candidate, 0) + 1

print(candidate_counts, "candidate_counts")

# Step 3: Find the most frequent candidate manually
most_frequent_candidate = None
max_count = 0

for candidate, count in candidate_counts.items():
    if count > max_count:
        max_count = count
        most_frequent_candidate = candidate

# Step 4: Print the result
print("Most frequent candidate:", most_frequent_candidate if most_frequent_candidate else "No candidates found")




data = [
{"hostname": "10.16.08.09", "Candidate": "Rajat", "password": "asdadwf"},
{"hostname": "", "Candidate": "Rajat1", "password": ""},
{"hostname": "", "Candidate": "Rajat1", "password": ""},
{"hostname": "", "Candidate": "Rajat1", "password": ""},
# Add more dictionaries to the list as needed
]
from collections import Counter
# Extract candidate names from the "Candidate" key in each dictionary
candidates = [item["Candidate"] for item in data if "Candidate" in item]
# Use Counter to count occurrences of each candidate
candidate_counts = Counter(candidates)
print(candidate_counts,"candidate_counts")
# Find the most frequent candidate
most_frequent_candidate = candidate_counts.most_common(1)
print(most_frequent_candidate)
# Print the result
print("Most frequent candidate:", most_frequent_candidate[0][0] if
most_frequent_candidate else "No candidates found")
