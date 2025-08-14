q)given an array of integer k, you need to find the total number of continuous subarray whose sum equals to k

Brute Force Approach:
A brute-force approach involves checking all possible subarrays and calculating their sums. 
We iterate over all possible starting points of the subarrays 
and for each starting point, iterate over all possible ending points while computing the sum.

Steps:
Use two nested loops:
The outer loop picks the starting index.
The inner loop picks the ending index and computes the sum of elements from the start index to the end index.
If the sum of any subarray equals k, increment the count.
Complexity Analysis:
Time Complexity: 
O(n2)
(since we compute the sum for each subarray)
Space Complexity: 
O(1) (no extra space is used)


def subarraySumBruteForce(nums, k):
    count = 0
    n = len(nums)

    # Iterate over all possible subarrays
    for start in range(n):
        sum_ = 0  # Initialize sum for each starting index
        for end in range(start, n):
            sum_ += nums[end]  # Compute sum for subarray [start:end]
            if sum_ == k:
                count += 1  # Found a valid subarray
    
    return count

# Example Usage:
nums = [1, 1, 1]
k = 2
print(subarraySumBruteForce(nums, k))  # Output: 2

nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(subarraySumBruteForce(nums, k))  # Output: 4

to get array also:
    
def subarraySumBruteForce(nums, k):
    count = 0
    n = len(nums)
    a =[]

    # Iterate over all possible subarrays
    for start in range(n):
        sum_ = 0
     
        # Initialize sum for each starting index
        for end in range(start, n):
            sum_ += nums[end]  # Compute sum for subarray [start:end]
            if sum_ == k:
                count += 1
                a.append(nums[start:end + 1])
                # Found a valid subarray
    print(a)
    return count

# Example Usage:
nums = [1, 1, 1]
k = 2
print(subarraySumBruteForce(nums, k))  # Output: 2

nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(subarraySumBruteForce(nums, k))  # Output: 4

[[1, 1], [1, 1]]
2
[[3, 4], [7], [7, 2, -3, 1], [1, 4, 2]]
4


------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is a classic problem that can be efficiently solved using a hashmap (dictionary) to keep track of cumulative sums. The approach follows these steps:

Approach:
Use a prefix sum to keep track of the running sum.
Use a hashmap (dictionary) to store the frequency of prefix sums encountered so far.
Iterate through the array:
Compute the prefix sum.
Check if prefix_sum - k exists in the hashmap (indicating a subarray ending at the current index with sum k).
Update the count of subarrays accordingly.
Store/update the prefix sum in the hashmap.
Complexity:

Time Complexity: 
O(n) (since we iterate through the array once)
Space Complexity: 
O(n) (for storing prefix sums)
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_sum_counts = {0: 1}  # Initialize hashmap with {0:1} to handle case where prefix_sum itself is k
    
    for num in nums:
        prefix_sum += num  # Update running sum
        
        # If (prefix_sum - k) exists in hashmap, it means there is a subarray that sums to k
        if prefix_sum - k in prefix_sum_counts:
            count += prefix_sum_counts[prefix_sum - k]
        
        # Update hashmap with current prefix_sum count
        prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1
    
    return count

# Example Usage:
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # Output: 2

nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(subarraySum(nums, k))  # Output: 4


Explanation:
Consider nums = [3, 4, 7, 2, -3, 1, 4, 2] and k = 7:

Prefix sums encountered: [3, 7, 14, 16, 13, 14, 18, 20]
The subarrays that sum to 7:
[3, 4]
[7]
[4, 7, 2, -3, 1]
[1, 4, 2]
The function correctly counts 4 such subarrays.


addeup question: printing array as well:
    
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_sum_counts = {0: [(-1, [])]}  # Map prefix_sum to list of (index, subarray)
    subarrays = []
    
    for i, num in enumerate(nums):
        prefix_sum += num  # Update running sum
        
        # If (prefix_sum - k) exists in hashmap, there are valid subarrays ending at index i
        if prefix_sum - k in prefix_sum_counts:
            for index, subarray in prefix_sum_counts[prefix_sum - k]:
                count += 1
                subarrays.append(subarray + nums[index + 1 : i + 1])  # Store the valid subarray
        
        # Add current prefix sum to hashmap
        if prefix_sum in prefix_sum_counts:
            prefix_sum_counts[prefix_sum].append((i, nums[: i + 1]))  # Store prefix up to index i
        else:
            prefix_sum_counts[prefix_sum] = [(i, nums[: i + 1])]

    return count, subarrays

# Example Usage:
nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
count, subarrays = subarraySum(nums, k)
print("Total Count:", count)
print("Subarrays:", subarrays)

brute force:
    
def subarraySumBruteForce(nums, k):
    count = 0
    subarrays = []
    n = len(nums)

    # Iterate over all possible subarrays
    for start in range(n):
        sum_ = 0
        temp_subarray = []
        temp =0
        print(temp, "0000")
        for end in range(start, n):
            sum_ += nums[end]
            temp_subarray.append(nums[end])
            print(temp_subarray,"sub")# Track elements of the subarray
            
            if sum_ == k:
                count += 1
                temp +=1
                print(temp,"cccc")
                subarrays.append(list(temp_subarray)) 
                print(subarrays,"main")# Store a copy of the subarray

    return count, subarrays

nums = [3, 4, -7, 2, 3, 1,1, 4, 2]
k = 7
count, subarrays = subarraySumBruteForce(nums, k)
print("Total Count:", count)
print("Subarrays:", subarrays)


Here's the implementation for Run-Length Encoding (RLE), which compresses a string by encoding consecutive repeating characters with their count.

def encode_rle(s):
    if not s:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(s[i - 1] + str(count))
            count = 1

    encoded.append(s[-1] + str(count))  # Append the last character count
    return "".join(encoded)


def decode_rle(encoded):
    decoded = []
    i = 0

    while i < len(encoded):
        char = encoded[i]
        count = 0
        i += 1
        while i < len(encoded) and encoded[i].isdigit():
            count = count * 10 + int(encoded[i])  # Handles multi-digit numbers
            i += 1
        decoded.append(char * count)

    return "".join(decoded)


# Example usage
s = "aaaaabbbccddd"
encoded = encode_rle(s)
print("Encoded:", encoded)  # Output: a5b3c2d3

decoded = decode_rle(encoded)
print("Decoded:", decoded)  # Output: aaaaabbbccddd


Explanation:
Encoding (Compression)

Traverse the string and count consecutive occurrences of each character.
Append char + count to the result.
Example: "aaaaabbbccddd" → "a5b3c2d3"
Decoding (Decompression)

Read character and count from the encoded string.
Repeat the character count times and build the original string.
Example: "a5b3c2d3" → "aaaaabbbccddd"


def encode_rule(s):
    
    if not s:
        return ""
    count = 1
    encode= []
    i = 0
    while i +1 < len(s):
        if s[i] == s[i+1]:
            count +=1
        else:
            #encode.append(f"{count}#{s[i]}")
            encode.append( str(count) +"#" + s[i])
            count =1
        i +=1
    #encode.append(f"{count}#{s[i]}")
    encode.append( str(count) +"#" + s[i])
    return "".join(encode)
def decode_rule(s):
    decode_sting = []
    i=0
    k=0
    while i < len(s):
        if s[i] != "#" and s[i].isdigit():
            print(s[i])
            k = k * 10 + int(s[i])
        elif s[i] == "#":
            decode_sting.append(k*s[i +1])
            k=0
            i+=1
        i+=1
    return "".join(decode_sting)

           
            
            
s = "aaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcckdddl"
encode_string = encode_rule(s)
print(encode_string)
print(decode_rule(encode_string))

25#a239#b2#c1#k3#d1#l
2
5
2
3
9
2
1
3
1
aaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcckdddl


        
    


1. Basic Stack with Pairs (Value, Count)
We will implement a stack where each element is stored as a pair (value, count).




class StackWithPairs:
    def __init__(self):
        self.stack = []

    def push(self, value):
        # If stack is empty or top element is different, add a new pair
        if not self.stack or self.stack[-1][0] != value:
            self.stack.append((value, 1))
        else:
            # Increment the count if the same value is pushed again
            last_value, last_count = self.stack.pop()
            self.stack.append((last_value, last_count + 1))

    def pop(self):
        if not self.stack:
            return None
        last_value, last_count = self.stack.pop()
        if last_count > 1:
            self.stack.append((last_value, last_count - 1))
        return last_value

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        print(self.stack)  # Debugging: Show stack contents


2. Testing the Stack with Pairs
stack = StackWithPairs()

stack.push(10)
stack.push(10)
stack.push(20)
stack.push(20)
stack.push(20)
stack.push(30)

stack.print_stack()  # Output: [(10, 2), (20, 3), (30, 1)]

print(stack.pop())   # Output: 30
print(stack.pop())   # Output: 20
stack.print_stack()  # Output: [(10, 2), (20, 2)]


3. Stack with Pairs for Tracking Min Values
class MinStack:
    def __init__(self):
        self.stack = []  # Stores (value, current_min)

    def push(self, value):
        current_min = min(value, self.stack[-1][1]) if self.stack else value
        self.stack.append((value, current_min))

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()[0]

    def get_min(self):
        if not self.stack:
            return None
        return self.stack[-1][1]

    def print_stack(self):
        print(self.stack)


Test MinStack

min_stack = MinStack()
min_stack.push(5)
min_stack.push(2)
min_stack.push(8)
min_stack.push(1)

print(min_stack.get_min())  # Output: 1
min_stack.pop()
print(min_stack.get_min())  # Output: 2


4. Explanation
Stack with (Value, Count)
Push the same number multiple times → Only the count increases.
Pop → Reduces the count instead of removing the element immediately.
Stack with (Value, Min)
Tracks the minimum element at every stage.
Useful in problems like finding the min value in O(1) time.

Time Complexity
Push: 
O(1) (Append to stack)
Pop: 
O(1) (Remove last element or decrement count)
Top/Get Min: 
O(1)

1. Encoding Function
This function compresses the string by grouping consecutive characters and storing them as (char, count) pairs.

def encode_rle_pairs(s):
    encoded_pairs = []
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:  # Count consecutive occurrences
            i += 1
            count += 1
        encoded_pairs.append((s[i], count))  # Store as a (char, count) pair
        i += 1
    
    return encoded_pairs



2. Decoding Function


This function expands the encoded pairs back into the original string.


def decode_rle_pairs(encoded_pairs):
    decoded_string = ""
    
    for char, count in encoded_pairs:
        decoded_string += char * count  # Repeat character `count` times

    return decoded_string


3. Testing the Functions
s = "aaaaabbbccddd"

encoded_pairs = encode_rle_pairs(s)
print("Encoded Pairs:", encoded_pairs)  
# Output: [('a', 5), ('b', 3), ('c', 2), ('d', 3)]

decoded_string = decode_rle_pairs(encoded_pairs)
print("Decoded String:", decoded_string)  
# Output: "aaaaabbbccddd"



4. Explanation
Encoding
"aaaaabbbccddd" → [('a', 5), ('b', 3), ('c', 2), ('d', 3)]
a appears 5 times → ('a', 5)
b appears 3 times → ('b', 3)
c appears 2 times → ('c', 2)
d appears 3 times → ('d', 3)


Decoding
[('a', 5), ('b', 3), ('c', 2), ('d', 3)] → "aaaaabbbccddd"
('a', 5) expands to "aaaaa"
('b', 3) expands to "bbb"
('c', 2) expands to "cc"
('d', 3) expands to "ddd"

5. Time Complexity
Encoding: 
O(n) – Iterates through the string once.
Decoding: 
O(n) – Expands stored pairs back into a string.


You can move all zeros in an array to the end while maintaining the order of non-zero elements using Python. Here’s an efficient approach using two-pointer technique:

def move_zeros_to_end(arr):
    non_zero_index = 0  # Pointer for placing non-zero elements
    
    # Move non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1

# Example usage:
arr = [0, 1, 0, 3, 12]
move_zeros_to_end(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]



Explanation:
Use a non_zero_index to track the position where the next non-zero element should be placed.
Iterate through the array and swap non-zero elements with elements at non_zero_index.
This ensures all non-zero elements are moved to the front while keeping their relative order, and zeros are shifted to the end.
This approach runs in O(n) time complexity and O(1) space complexity.

other way:
    
def move_zeros_to_end(arr):
    n = len(arr)
    i, j = 0, 0  # Two pointers

    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]  # Swap non-zero with zero
            i += 1
        j += 1

# Example usage:
arr = [0, 1, 0, 3, 12]
move_zeros_to_end(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]


Explanation:
Two pointers (i and j):
i keeps track of the position to place the next non-zero element.
j iterates through the array.
Swapping when encountering a non-zero:
If arr[j] is non-zero, swap arr[i] and arr[j], then move i forward.
Move j forward in every iteration.
Time Complexity:
O(n): The array is traversed once.
Space Complexity:
O(1): No extra space is used.
This is an efficient approach to shifting all zeros to the end while keeping the order of non-zero elements intact.


Here’s an OOP-based Python solution using a while loop to move zeros to the end of an array.

OOP Implementation:

class ArrayManipulator:
    def __init__(self, arr):
        self.arr = arr
    
    def move_zeros_to_end(self):
        n = len(self.arr)
        i, j = 0, 0  # Two pointers

        while j < n:
            if self.arr[j] != 0:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]  # Swap non-zero with zero
                i += 1
            j += 1

    def get_array(self):
        return self.arr

# Example Usage:
arr = [0, 1, 0, 3, 12]
manipulator = ArrayManipulator(arr)
manipulator.move_zeros_to_end()
print(manipulator.get_array())  # Output: [1, 3, 12, 0, 0]



Polymorphic Approach
We'll define a base class ArrayProcessor and two different subclasses that implement move_zeros_to_end() differently.

from abc import ABC, abstractmethod

# Base class (Abstract class)
class ArrayProcessor(ABC):
    def __init__(self, arr):
        self.arr = arr

    @abstractmethod
    def move_zeros_to_end(self):
        pass

    def get_array(self):
        return self.arr

# Subclass 1: Using two-pointer technique with while loop
class TwoPointerProcessor(ArrayProcessor):
    def move_zeros_to_end(self):
        i, j = 0, 0  # Two pointers

        while j < len(self.arr):
            if self.arr[j] != 0:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]  # Swap non-zero with zero
                i += 1
            j += 1

# Subclass 2: Using count method (Different approach)
class CountBasedProcessor(ArrayProcessor):
    def move_zeros_to_end(self):
        non_zero_elements = [num for num in self.arr if num != 0]  # Collect non-zero elements
        zero_count = len(self.arr) - len(non_zero_elements)  # Count zeros
        self.arr[:] = non_zero_elements + [0] * zero_count  # Append zeros

# Polymorphic function
def process_array(processor: ArrayProcessor):
    processor.move_zeros_to_end()
    print(processor.get_array())

# Example usage:
arr1 = [0, 1, 0, 3, 12]
arr2 = [4, 0, 5, 0, 2, 0, 8]

processor1 = TwoPointerProcessor(arr1)
processor2 = CountBasedProcessor(arr2)

# Calling the same method on different implementations
process_array(processor1)  # Output: [1, 3, 12, 0, 0]
process_array(processor2)  # Output: [4, 5, 2, 8, 0, 0, 0]


Polymorphism Concepts Used:
Abstract Base Class (ABC): ArrayProcessor ensures all subclasses implement move_zeros_to_end().
Method Overriding: TwoPointerProcessor and CountBasedProcessor override move_zeros_to_end() differently.
Polymorphic Behavior: process_array() works on both subclasses without knowing the exact implementation.
This demonstrates polymorphism by allowing different implementations of move_zeros_to_end() while maintaining a common interface.


q) Given an array temperatures where temperatures[i] represents the temperature on day i, return an array result where result[i] is
 the number of days until a warmer temperature occurs. 
If no future day has a higher temperature, result[i] should be 0.

Input:
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]


Output:
    [1, 1, 4, 2, 1, 1, 0, 0]


74 → 75 (1 day)
75 → 76 (4 days)
71 → 72 (2 days)
69 → 72 (1 day)
72 → 76 (1 day)
76 has no warmer day → 0
73 has no warmer day → 0

Optimized Monotonic Stack Solution (O(n) Time Complexity)
def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n  # Initialize result array with 0s
    stack = []  # Stack to store (index, temperature)
    
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index  # Calculate difference in days
        stack.append(i)  # Push current index to stack
    
    return result

# Example usage:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))



Explanation:
We iterate through the array while maintaining a monotonic decreasing stack (stores indices of temperatures).
For each temperature, we pop from the stack if the current temperature is warmer than the one at the top of the stack.
For each popped element, we compute the difference in days and store it in result.
Finally, the stack contains only the indices of temperatures with no warmer days ahead.


1. What is a Dictionary?

person = {"name": "Alice", "age": 25, "city": "New York"}

javascrpit:
const person = { name: "Alice", age: 25, city: "New York" };


(a) Creating a Dictionary
Python

my_dict = {"brand": "Toyota", "model": "Camry", "year": 2020}

JavaScript
const myDict = { brand: "Toyota", model: "Camry", year: 2020 };


(b) Accessing Values

Python
print(my_dict["brand"])  # Output: Toyota
print(my_dict.get("year"))  # Output: 2020


JavaScript
console.log(myDict.brand);  // Output: Toyota
console.log(myDict["year"]); // Output: 2020


(c) Adding and Updating Values
Python
my_dict["color"] = "Red"  # Add new key-value pair
my_dict["year"] = 2022  # Update existing value


JavaScript
myDict.color = "Red";  // Add new key-value pair
myDict.year = 2022;  // Update existing value


(d) Removing Elements
Python
del my_dict["model"]  # Remove key-value pair
my_dict.pop("year")  # Removes and returns the value


JavaScript
delete myDict.model;  // Remove key-value pair

(e) Iterating Over Dictionary
Python
for key, value in my_dict.items():
    print(key, ":", value)


JavaScript
for (let key in myDict) {
  console.log(key + ":", myDict[key]);
}


3. Dictionary Methods
Python Dictionary Methods



Method	Description
dict.keys()	Returns all keys.
dict.values()	Returns all values.
dict.items()	Returns key-value pairs as tuples.
dict.get(key, default)	Returns value of key or default if key doesn’t exist.
dict.pop(key)	Removes a key and returns its value.
dict.update(other_dict)	Merges two dictionaries.
dict.clear()	Removes all items from the dictionary.

Example

print(my_dict.keys())  # Output: dict_keys(['brand', 'year', 'color'])
print(my_dict.values())  # Output: dict_values(['Toyota', 2022, 'Red'])


JavaScript Object Methods

Method	Description
Object.keys(obj)	Returns an array of keys.
Object.values(obj)	Returns an array of values.
Object.entries(obj)	Returns an array of key-value pairs.
obj.hasOwnProperty(key)	Checks if a key exists.

Example

console.log(Object.keys(myDict)); // Output: ["brand", "year", "color"]
console.log(Object.values(myDict)); // Output: ["Toyota", 2022, "Red"]


4. Nested Dictionaries
Dictionaries can contain other dictionaries.

Python
student = {
    "name": "John",
    "grades": {"math": 90, "science": 85}
}
print(student["grades"]["math"])  # Output: 90


JavaScript
const student = {
  name: "John",
  grades: { math: 90, science: 85 }
};
console.log(student.grades.math); // Output: 90


5. Dictionary Comprehension
Python allows dictionary comprehension for concise operations.

Python
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


No direct equivalent exists in JavaScript, but you can achieve a similar result using reduce().

JavaScript

const squares = [...Array(6).keys()].slice(1).reduce((acc, x) => {
  acc[x] = x * x;
  return acc;
}, {});

console.log(squares); // Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


6. Checking for Key Existence
Python
if "brand" in my_dict:
    print("Key exists")


JavaScript
if ("brand" in myDict) {
    console.log("Key exists");
}


7. Converting Between Dictionary and JSON
Since JavaScript objects are similar to JSON, you often need to convert between them.

Python
import json
json_string = json.dumps(my_dict)  # Convert dictionary to JSON
parsed_dict = json.loads(json_string)  # Convert JSON back to dictionary


JavaScript
const jsonString = JSON.stringify(myDict); // Convert object to JSON
const parsedObject = JSON.parse(jsonString); // Convert JSON to object


8. Sorting a Dictionary
Python dictionaries can be sorted using sorted(), while JavaScript uses Object.entries().

Python
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)

JavaScript
const sortedDict = Object.fromEntries(Object.entries(myDict).sort((a, b) => a[1] - b[1]));
console.log(sortedDict);

Conclusion
Concept	Python Dictionary	JavaScript Object
Creation	dict = {}	const obj = {}
Accessing	dict["key"]	obj.key or obj["key"]
Adding/Updating	dict["key"] = value	obj.key = value
Removing	del dict["key"]	delete obj.key
Iteration	for k, v in dict.items():	for (let key in obj) {}
Methods	dict.keys(), dict.values(), dict.items()	Object.keys(obj), Object.values(obj), Object.entries(obj)
Check Existence	"key" in dict	"key" in obj
Convert to JSON	json.dumps(dict)	JSON.stringify(obj)


Here's the JavaScript code to group students based on the sports they play:

const students = {
  kiran: { sports: ["football", "basketball"] },
  arun: { sports: ["hockey", "CoCO", "Cricket"] },
  santhosh: { sports: ["basketball", "hockey"] }
};

const sports = {};

// Iterate through each student
for (const student in students) {
  students[student].sports.forEach((sport) => {
    if (!sports[sport]) {
      sports[sport] = []; // Initialize if not exists
    }
    sports[sport].push(student); // Add student to the respective sport
  });
}

console.log(sports);

Explanation:
Loop through each student in the students object.
Iterate over their sports array.
Check if the sport key exists in the sports object:
If not, initialize it with an empty array.
Add the student's name to the respective sport.
The result will be an object grouping students by the sports they play.
Output:
 {
  "football": ["kiran"],
  "basketball": ["kiran", "santhosh"],
  "hockey": ["arun", "santhosh"],
  "CoCO": ["arun"],
  "Cricket": ["arun"]
}

python code:

students = {
    "kiran": {"sports": ["football", "basketball"]},
    "arun": {"sports": ["hockey", "CoCO", "Cricket"]},
    "santhosh": {"sports": ["basketball", "hockey"]}
}

sports = {}

# Iterate through each student
for student, details in students.items():
    for sport in details["sports"]:
        if sport not in sports:
            sports[sport] = []  # Initialize if not exists
        sports[sport].append(student)  # Add student to the respective sport

print(sports)

{
  'football': ['kiran'],
  'basketball': ['kiran', 'santhosh'],
  'hockey': ['arun', 'santhosh'],
  'CoCO': ['arun'],
  'Cricket': ['arun']
}


Explanation:
Iterate through each student in the students dictionary.
Loop over their sports list.
If the sport is not in the sports dictionary, initialize it as an empty list.
Append the student’s name to the respective sport.


To reduce the string "abbbcddeef" so that it has no duplicate characters, you can iterate through the string and 
keep only the first occurrence of each character while removing subsequent duplicates.

Here's how you can achieve that:

def remove_duplicates(s):
    result = []
    for char in s:
        if char not in result:
            result.append(char)
    return ''.join(result)

# Example usage
s = "abbbcddeef"
reduced_string = remove_duplicates(s)
print(reduced_string)  # Output: "abcdef"

Explanation:
Iterate through the string: Loop through each character in the input string.
Check for duplicates: For each character, check if it already exists in the result list.
Add unique characters: If the character is not in result, append it.
Return the result: After the loop, join the characters in result into a string and return it.


Output:
    abcdef


To achieve the output "bfq" from the string "aabbbcfffcg", you need to remove characters that are repeated more than
 once and then return the characters that appear exactly once in the order they first appear.

Here's the correct code:

def remove_duplicates_and_get_unique(s):
    # Count the occurrences of each character
    char_count = {}
    
    # Count each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Keep only characters that appear exactly once
    result = [char for char in s if char_count[char] == 1]
    
    # Return the string formed from unique characters
    return ''.join(result)

# Example usage
s = "aabbbcfffcg"
output = remove_duplicates_and_get_unique(s)
print(output)  # Output: "q"


Explanation:
Count occurrences: Use a dictionary char_count to count how many times each character appears in the string.
Filter characters: After counting, iterate through the string and keep only the characters that appear exactly once.
Join the result: Use ''.join(result) to convert the list of characters back into a string.
Output:
    q



def remove_duplicates_and_get_unique(s):
    # Initialize an empty list to store the result
    result = []
    
    # Track previously seen characters
    seen = set()
    
    # Iterate through the string
    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)
    
    # Return the string formed from unique characters
    return ''.join(result)

# Example usage
s = "aaabbbcffcg"
output = remove_duplicates_and_get_unique(s)
print(output)  # Output: "abcfg"



def remove_consecutive_duplicates(s):
    stack = []  # Stack to store characters along with their count
    
    for char in s:
        # If stack is not empty and the top of the stack has the same character
        if stack and stack[-1][0] == char:
            stack.pop()
        else:
            stack.append((char, 1))  # Push new character with count 1
    
    # Construct the result string by keeping only characters with count 1
    return ''.join(char for char, count in stack)

# Example usage
s1 = "aaabbbcffcg"
s2 = "aabbbdddafffdg"
output1 = remove_consecutive_duplicates(s1)
output2 = remove_consecutive_duplicates(s2)

print(output1)  # Expected: "abg"
print(output2)  # Expected: "bdafdg"


q)

def merge_two_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    # Merge two sorted arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append any remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

def merge_k_sorted_arrays(arrays):
    # If no arrays, return empty list
    if not arrays:
        return []
    
    # Start merging pairs of arrays
    while len(arrays) > 1:
        merged_arrays = []
        for i in range(0, len(arrays), 2):
            # Merge two arrays at a time
            if i + 1 < len(arrays):
                merged_arrays.append(merge_two_sorted_arrays(arrays[i], arrays[i + 1]))
            else:
                # If odd number of arrays, just add the last array
                merged_arrays.append(arrays[i])
        # Update arrays list with merged arrays
        arrays = merged_arrays
    
    return arrays[0]  # Final merged array

# Example Usage
k_sorted_arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(merge_k_sorted_arrays(k_sorted_arrays))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


Explanation:
merge_two_sorted_arrays:
This function merges two sorted arrays using a simple two-pointer technique. It compares elements from both arrays, appends the smaller element to the result, and advances the respective pointer.
Once one of the arrays is exhausted, it appends the remaining elements from the other array.
merge_k_sorted_arrays:
The function iteratively merges pairs of arrays until only one array remains.
It takes two consecutive arrays, merges them, and then moves on to the next pair. If there is an odd number of arrays, the last array is added without merging.
This continues until all arrays are merged into one sorted array.

Time Complexity:
O(N log K) where:
N is the total number of elements across all arrays.
K is the number of arrays.
Each merge operation takes linear time for each pair of arrays, and the merging reduces the number of arrays by half at each step, resulting in log K steps.
q)
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

{"bangalore": ["tushar", "sachin"], "gurgaon": ["sid"]}



employees = [
    {"name": "emp1", "skills": ["Python", "React"]},
    {"name": "emp2", "skills": ["Javascript", "React"]},
    {"name": "emp3", "skills": ["Java"]},
    {"name": "emp2", "skills": ["Python"]},
    {"name": "emp4", "skills": ["Javascript", "React"]}
]

from collections import defaultdict

skill_map = defaultdict(list)  # Use a defaultdict with list

for employee in employees:
    for skill in employee["skills"]:
        if employee["name"] not in skill_map[skill]:  # Ensure no duplicates
            skill_map[skill].append(employee["name"])

# Convert defaultdict to a standard dictionary
result = dict(skill_map)

print(result)

output:
    {'Python': ['emp1', 'emp2'], 'React': ['emp1', 'emp2', 'emp4'], 'Javascript': ['emp2', 'emp4'], 'Java': ['emp3']}




Q)merge k- sorted list:
 
 
 brute force:
 
 def merge_two_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged_array = []
    
    # Merge two sorted arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # Add remaining elements
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array

def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []
    
    merged_array = arrays[0]  # Start with the first array

    for i in range(1, len(arrays)):  # Merge one by one
        merged_array = merge_two_sorted_arrays(merged_array, arrays[i])
    
    return merged_array

# Example usage
arrays = [
    [2, 4, 7, 8],
    [3, 5, 9, 10],
    [1, 11, 12, 13]
]

print(merge_k_sorted_arrays(arrays))  # Output: [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13]


Another method:
    
def merge_two_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged_array = []
    
    # Merge two sorted arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # Add remaining elements
    merged_array.extend(arr1[i:])  # Extend with remaining elements in arr1
    merged_array.extend(arr2[j:])  # Extend with remaining elements in arr2

    return merged_array

def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []
    
    merged_array = arrays[0]  # Start with the first array

    for i in range(1, len(arrays)):  # Merge one by one
        merged_array = merge_two_sorted_arrays(merged_array, arrays[i])
    
    return merged_array

# Example usage
arrays = [
    [2, 4, 7, 8],
    [3, 5, 9, 10],
    [1, 11, 12, 13]
]

print(merge_k_sorted_arrays(arrays))  
# Output: [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13]


Time complexity:
    This now correctly merges k sorted arrays in O(k * n²) time complexity.
    
    
    
    
Definition of k and n in Time Complexity Analysis
In the context of merging k sorted arrays, the variables k and n represent:

k = Number of sorted arrays.
n = Average number of elements in each array.
For example, in the input:
    
arrays = [
    [2, 4, 7, 8],       # 4 elements
    [3, 5, 9, 10],      # 4 elements
    [1, 11, 12, 13]     # 4 elements
]

Here, k = 3 (because there are 3 sorted arrays) and n = 4 (since each array has 4 elements on average).



First Merge:

Merge arrays[0] (size n) with arrays[1] (size n) → O(n + n) = O(2n)
Second Merge:

Merge the result (size 2n) with arrays[2] (size n) → O(2n + n) = O(3n)
Third Merge:

Merge the result (size 3n) with arrays[3] (size n) → O(3n + n) = O(4n)
Continuing this process for k arrays → Total cost is:
    
    
    O(n)+O(2n)+O(3n)+⋯+O(kn)
    
    
    This forms an arithmetic series:
        
        O(n(1+2+3+...+k))=O(n.k(k+1)/2)
​

Since we ignore constants in Big-O notation, the dominant term is:
    O(k*k*n)



Optimize way:
 
 import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    # Insert the first element of each array into the heap
    for i, arr in enumerate(arrays):
        if arr:  # Ensure array is not empty
            heapq.heappush(min_heap, (arr[0], i, 0))  # (value, array index, element index)

    # Process the heap
    while min_heap:
        value, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(value)

        # Insert next element from the same array into the heap
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))

    return result

# Example usage
arrays = [
    [2, 4, 7, 8],
    [3, 5, 9, 10],
    [1, 11, 12, 13]
]

print(merge_k_sorted_arrays(arrays))  # Output: [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13]



Time Complexity Analysis
Pushing all first elements into the heap → O(k log k) (heap operations)
Processing all elements (nk elements in total)
Each insertion & deletion in the heap takes O(log k).
Since we process nk elements, this takes O(nk log k).
🔹 Final Complexity: O(nk log k)


In the given code, elements are pushed into the min-heap (heapq) as tuples containing three values:
    
(value, array index, element index)

The heap organizes itself based on the first value (the element value itself) because Python’s heapq is a min-heap by default.


How the Heap is Formed?
Each tuple has three values:

value → The actual number from the array (this determines the heap order).
array index → The index of the array from which the value was taken.
element index → The index of the value within its array.
When inserting elements into the heap, Python’s heapq maintains the heap order based on the first value (value itself).



Step-by-Step Execution (Dry Run)
Initial State
The input arrays:
    
arrays = [
    [1, 5, 9],  # Index 0
    [2, 6, 8],  # Index 1
    [3, 7, 10]  # Index 2
]


At the start, we push the first element of each array into the heap:
    
heapq.heappush(min_heap, (arr[0], i, 0))


So, min_heap becomes:
[(1, 0, 0), (2, 1, 0), (3, 2, 0)]

The heap structure (logically represented):

        1
       / \
      2   3

Since heapq is a min-heap, the root (smallest value) is 1.

Step 1: Extract Smallest Element (1)
Heap before extraction:
[(1, 0, 0), (2, 1, 0), (3, 2, 0)]


Extract (1, 0, 0) → Add 1 to the result list.
Push next element from the same array (5) → (5, 0, 1)

Updated min_heap:
[(2, 1, 0), (3, 2, 0), (5, 0, 1)]


Result list: [1]


Step 2: Extract Smallest Element (2)
Heap before extraction:
    [(2, 1, 0), (3, 2, 0), (5, 0, 1)]

Extract (2, 1, 0) → Add 2 to result.
Push next element from the same array (6) → (6, 1, 1)
Updated min_heap:
    [(3, 2, 0), (5, 0, 1), (6, 1, 1)]

Result list: [1, 2]

Step 3: Extract Smallest Element (3)
Heap before extraction:
    [(3, 2, 0), (5, 0, 1), (6, 1, 1)]


Extract (3, 2, 0) → Add 3 to result.
Push next element from the same array (7) → (7, 2, 1)
Updated min_heap:
    [(5, 0, 1), (6, 1, 1), (7, 2, 1)]


Result list: [1, 2, 3]

Step 4 to Final Step
Following the same process:

Extract 5 → Push 9.
Extract 6 → Push 8.
Extract 7 → Push 10.
Extract 8 → No more elements in that array.
Extract 9 → No more elements in that array.
Extract 10 → No more elements in that array.


Final heap operations sequence:
    
    
Extract 5 → [(6, 1, 1), (7, 2, 1), (9, 0, 2)]  → Result: [1, 2, 3, 5]
Extract 6 → [(7, 2, 1), (9, 0, 2), (8, 1, 2)]  → Result: [1, 2, 3, 5, 6]
Extract 7 → [(8, 1, 2), (9, 0, 2), (10, 2, 2)] → Result: [1, 2, 3, 5, 6, 7]
Extract 8 → [(9, 0, 2), (10, 2, 2)]          → Result: [1, 2, 3, 5, 6, 7, 8]
Extract 9 → [(10, 2, 2)]                      → Result: [1, 2, 3, 5, 6, 7, 8, 9]
Extract 10 → []                               → Result: [1, 2, 3, 5, 6, 7, 8, 9, 10]


Final Sorted Output:
    [1, 2, 3, 5, 6, 7, 8, 9, 10]

Key Takeaways
The heap is ordered by the first value in the tuple (value).
The array index and element index help track where the elements are from.
Using a min-heap ensures that the smallest available element is always extracted first.
Time Complexity: O(n log k) (where n is total elements and k is the number of arrays).
Space Complexity: O(k) (since at most k elements are in the heap at any time).


 


# Search in a rotated sorted array
def search_rotated_sorted_array(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid  # Return index if target is found

        # Check which part is sorted
        if array[low] <= array[mid]:  # Left half is sorted
            if array[low] <= target < array[mid]:  # Target is in left half
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half is sorted
            if array[mid] < target <= array[high]:  # Target is in right half
                low = mid + 1
            else:
                high = mid - 1

    return -1  # Target not found

# Example usage:
# array = [6, 7, 1, 2, 3, 4, 5]
# array = [6, 7, 1, 2, 3, 4]
array = [3, 4, 5,6,7,1,2]
target = 1

# Searching for the target element
print("Index of target:", search_rotated_sorted_array(array, target))



Understanding Rotated Sorted Arrays
A rotated sorted array is an array that was originally sorted in increasing order but then rotated at some pivot.
For example:

Sorted Array: [1, 2, 3, 4, 5, 6, 7]
Rotated Versions:
[6, 7, 1, 2, 3, 4, 5] (rotated at index 2)
[3, 4, 5, 6, 7, 1, 2] (rotated at index 5)
The key observation here is that one half of the array will always be sorted.


Algorithm Walkthrough
The function uses binary search to efficiently find the target.

Step 1: Initialize Pointers
low = 0
high = len(array) - 1

Step 2: Perform Binary Search

a)Find the middle index
mid = (low + high) // 2

b)Check if array[mid] is the target
If array[mid] == target, return mid

c)Determine which half is sorted
If array[low] <= array[mid]: Left half is sorted.
Else: Right half is sorted.

d)Check if the target lies in the sorted half
If yes, adjust low and high accordingly.

Example Walkthrough
Input:
    
array = [3, 4, 5, 6, 7, 1, 2]
target = 1

Execution Steps:
Iteration	low	 high	mid	array[mid]	Condition Checked	             Action
1	         0	 6	     3	       6	Left half [3,4,5,6] is sorted	 Move to right half (low = 4)
2	         4	 6	     5	       1	array[mid] == target	         Return 5

out:
    
Index of target: 5


The target 1 is found at index 5.
Time Complexity
Best Case: 
O(1) (if found in the first step)
Worst Case: 
O(logn) (Binary search)
Space Complexity
O(1) (Only a few variables are used)

Why Does This Work?
This approach works because:

A rotated sorted array always has one sorted half.
We leverage binary search to eliminate half the search space in each iteration.
This makes the search much faster compared to a linear search (
O(n)).

Summary
Identify the sorted half.
Check if the target is in the sorted half.
Discard half of the array in each iteration.
Repeat until target is found or search space is exhausted.


'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# print ('Hello World')

# Write a function to count the number of unique digits in a number - eg 111 -> 1 121 -> 2 123 -> 3

# def count_unique_digits(nums):
#     set1 = set()
#     for num in nums:
#         set1.add(num)
#     return len(set1)
        
        
    
# nums = '111'
# nums1 = '121'
# nums2 ='1441'
# print(count_unique_digits(nums2))



# Longest Even Length Word: Write a function to return the longest even length word in a sentence.
#  Sample input: "Be not afraid of greatness some are born great some achieve greatness
#  and some have greatness thrust upon them"
# Output: "afraid"



# def longest_even_length_word(sentence):
    
#     words = sentence.split()
#     # even_words = [ word for word in words if len(word) % 2 == 0]
#     max_lenth_word = ''
#     for word in words:
#         if len(word) % 2 ==0 and  len(word) > len(max_lenth_word):
#             max_lenth_word = word
#     return max_lenth_word
    
#     # print(even_words)
#     # if not even_words:
#     #     return None
#     # return max(even_words, key = len)
    


# input = "Be not afraid of greatness some are born great some achieve greatness and some have greatness thrust upon them"


# print(longest_even_length_word(input))



# Input: l1 = [1,[2,3, [4, 5]]] Output: l1 = [1,2,3,4,5]


# def extract_list(nested_list, result):
    
#     for item in nested_list:
#         if isinstance(item, list):
#             extract_list(item,result)
#         else:
#             result.append(item)
#     return result       

# result = []
# l1 = [1,[2,3, [4, 5]]] 

# print(extract_list(l1,result))



1. Count Unique Digits in a Number

def count_unique_digits(nums):
    return len(set(nums))

# Test cases
print(count_unique_digits('111'))   # Output: 1
print(count_unique_digits('121'))   # Output: 2
print(count_unique_digits('1441'))  # Output: 2


Improvements:
Instead of using a loop, we directly use set(nums), which removes duplicates.

This makes the code cleaner and more efficient.



2. Longest Even Length Word in a Sentence

def longest_even_length_word(sentence):
    words = sentence.split()
    max_length_word = max((word for word in words if len(word) % 2 == 0), key=len, default="")
    return max_length_word

# Test case
input_text = "Be not afraid of greatness some are born great some achieve greatness and some have greatness thrust upon them"
print(longest_even_length_word(input_text))  # Output: "afraid"



Improvements:
Used a generator expression inside max() to find the longest even-length word.


3. Flatten a Nested List


def flatten_list(nested_list):
    result = []
    def extract(nested):
        for item in nested:
            if isinstance(item, list):
                extract(item)
            else:
                result.append(item)
    extract(nested_list)
    return result

# Test case
l1 = [1, [2, 3, [4, 5]]]
print(flatten_list(l1))  # Output: [1, 2, 3, 4, 5]


Improvements:
Used recursion within an inner function for better readability.

Avoided passing result explicitly, making the function more concise.


Your SQL query has an error. Here’s the correct query to find authors who have written more than 10 books:
    
SELECT Author  
FROM BookAuthor  
GROUP BY Author  
HAVING COUNT(Book) > 10;


Explanation:
GROUP BY Author: Groups records by Author.

COUNT(Book): Counts the number of books each author has written.

HAVING COUNT(Book) > 10: Filters out only those authors who have written more than 10 books.


