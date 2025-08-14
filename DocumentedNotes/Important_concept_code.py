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


Bruete Force:
def remove_k_consecutive_duplicates_brute_force(s, k):
    while True:
        new_s = ""
        i = 0
        removed = False  # Flag to track if any removal occurred

        while i < len(s):
            count = 1
            # Count consecutive duplicates
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            
            # If `k` consecutive duplicates exist, skip them
            if count == k:
                removed = True
            else:
                new_s += s[i - count + 1: i + 1]
            
            i += 1  # Move to next character

        # If no removals were made, return the result
        if not removed:
            return new_s
        
        s = new_s  # Update string and repeat

# ✅ Example Usage
s = "deeedbbcccbdaa"
k = 3
print(remove_k_consecutive_duplicates_brute_force(s, k))  # Output: "aa"



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


def decorator(func):
    def wrapper(*args):
        # Check if all arguments are integers
        if not all(isinstance(arg, int) for arg in args):
            return "Error: All arguments must be integers"
        
        result = func(*args)
        print(result)
        return result
    return wrapper

@decorator
def sum_two(a, b):
    return a + b

# Testing
print(sum_two(1, "2"))  # Should return an error message
print(sum_two(3, 4))    # Should return 7


ERROR!
<class 'int'> 

<class 'str'> 

Error: All arguments must be integers
<class 'int'> 

<class 'int'> 

7




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

data = {"a": 10, "b": 60, "c": 30, "d": 80, "e": 90}

filtered_data = {key:value for key, value in data.items() if value > 50}
print(type(filtered_data))

<class 'dict'>


data = {"a": 10, "b": 60, "c": 30, "d": 80, "e": 90}

filtered_data = {key for key, value in data.items() if value > 50}
print(type(filtered_data))

<class 'set'>

data = {"a": 10, "b": 60, "c": 30, "d": 80, "e": 90}

filtered_data = [key for key, value in data.items() if value > 50]
print(type(filtered_data))



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



Here's the same logic in JavaScript to filter a nested dictionary (object of objects) — removing students who scored less than 50 in any subject:

const students = {
  Alice: { math: 80, science: 90 },
  Bob: { math: 45, science: 55 },
  Charlie: { math: 60, science: 40 },
};

const filteredStudents = Object.fromEntries(
  Object.entries(students).filter(([name, subjects]) =>
    Object.values(subjects).every(mark => mark >= 50)
  )
);

console.log(filteredStudents);



From the given students object, we want to remove students who scored less than 50 in any subject.
✅ Step 1: The input object
const students = {
  Alice:   { math: 80, science: 90 },
  Bob:     { math: 45, science: 55 },
  Charlie: { math: 60, science: 40 },
};


It’s an object where:

Keys are student names

Values are objects representing subject → marks.


✅ Step 2: Convert to entries (like Python's .items())

Object.entries(students)

This gives us an array of [key, value] pairs:
 [
  ["Alice",   { math: 80, science: 90 }],
  ["Bob",     { math: 45, science: 55 }],
  ["Charlie", { math: 60, science: 40 }]
]


Think of it like
students.items()  # Python equivalent

✅ Step 3: Filter the entries

.filter(([name, subjects]) =>
  Object.values(subjects).every(mark => mark >= 50)
)

Let’s break it down:

subjects is an object like { math: 80, science: 90 }

Object.values(subjects) gives [80, 90]

.every(mark => mark >= 50) returns true only if all marks are ≥ 50

So, the .filter() keeps only students where all subject marks are ≥ 50.

Example:
For "Alice" → [80, 90] → passes ✅

For "Bob" → [45, 55] → fails ❌

For "Charlie" → [60, 40] → fails ❌


✅ Step 4: Convert back to object
Object.fromEntries(...)

This takes filtered entries like:
    
[ ["Alice", { math: 80, science: 90 }] ]
And turns them back into a full object:
{
  Alice: { math: 80, science: 90 }
}



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


/**
 * Recursively remove all numeric values below a threshold
 * from a (possibly deeply‑nested) plain‑object tree.
 *
 * @param {Object} obj        An object whose leaves are either numbers or more objects
 * @param {number} threshold  Numbers < threshold are discarded (default 50)
 * @returns {Object}          A new object with the low values stripped out
 */
function filterNested(obj, threshold = 50) {
  // Treat only non‑null plain objects (skip arrays/functions)
  const isPlainObject =
    typeof obj === "object" && obj !== null && !Array.isArray(obj);

  if (!isPlainObject) {
    return obj; // primitive leaf: just hand it back (the caller decides)
  }

  const result = {};

  for (const [key, value] of Object.entries(obj)) {
    if (typeof value === "object" && value !== null && !Array.isArray(value)) {
      // Nested dictionary → recurse
      const cleaned = filterNested(value, threshold);
      if (Object.keys(cleaned).length) {
        result[key] = cleaned; // keep only if something survived
      }
    } else if (typeof value === "number" && value >= threshold) {
      // Numeric leaf and it passes the cut‑off → keep
      result[key] = value;
    }
    // All other cases (number < threshold, non‑number primitives) are skipped
  }

  return result;
}

/* ---------- Demo ---------- */
const data = {
  A: { math: 80, science: 90 },
  B: { math: 45, science: 55 },
  C: { math: 60, science: { physics: 40, chemistry: 85 } },
};

const filtered = filterNested(data, 50);
console.log(JSON.stringify(filtered, null, 2));

▶️ Console output
{
  "A": { "math": 80, "science": 90 },
  "B": { "science": 55 },
  "C": { "math": 60, "science": { "chemistry": 85 } }
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

/**
 * Merge overlapping intervals.
 *
 * @param {number[][]} intervals – Array of [start, end] pairs
 * @returns {number[][]}         – Merged, non‑overlapping intervals
 */
function mergeIntervals(intervals) {
  if (!Array.isArray(intervals) || intervals.length === 0) return [];

  // 1. Sort by start time
  intervals.sort((a, b) => a[0] - b[0]);

  const merged = [intervals[0].slice()];      // copy first interval

  // 2. Walk the rest
  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];
    const last = merged[merged.length - 1];

    if (start <= last[1]) {
      // Overlap → extend the last interval
      last[1] = Math.max(last[1], end);
    } else {
      // No overlap → push a new interval
      merged.push([start, end]);
    }
  }

  return merged;
}

/* --- Demo --- */
const intervals = [[1, 3], [2, 4], [5, 6], [8, 10]];
console.log(mergeIntervals(intervals));
// → [ [1, 4], [5, 6], [8, 10] ]

How it works (quick recap)
Sort the intervals by their start time so potential overlaps are adjacent.

Initialize merged with the first interval.

Iterate through the rest:

If the current start ≤ the end of the last merged interval, merge them by extending the end.

Otherwise, append the current interval as non‑overlapping.

Time complexity is O(n log n) for sorting, and the scan is O(n).




In JavaScript: pitfalls with the default Array.prototype.sort()

intervals.sort();              // ⚠️ BAD

Default ordering is lexicographic on strings.
[2, 10] becomes "2,10"; [15, 20] becomes "15,20".
So you’ll get "15,20" < "2,10" because "1" < "2".

Resulting order is unpredictable for negative numbers or multi‑digit starts.
Correct comparator:

intervals.sort((a, b) => a[0] - b[0]);  // ✅ numeric ascending by start

That’s all the “in‑built” help you need; JavaScript does not ship a special interval‑sorting routine.

What could count as “any in‑built sort”?


| Library / Method                           | Works? | Why / When                                      |
| ------------------------------------------ | ------ | ----------------------------------------------- |
| **Native `Array.sort` with comparator**    | ✅      | Gives exact numeric order on `a[0]`.            |
| **Native `Array.sort` without comparator** | ❌      | Lexicographic, breaks for multi‑digit integers. |
| **Lodash `_.sortBy(intervals, 0)`**        | ✅      | Sorts by first element numerically.             |
| **Typed array sorts** (`Int32Array`)       | ❌      | You’d lose the pair structure; not suitable.    |

Any of these “works” if—after it’s done—the array is ordered strictly by start value ascending.


What about descending order or sorting by end?
Technically you could:

Sort descending by start, then scan backwards or flip the comparison logic.

Sort by end, but then you’d need a different merge algorithm that keeps track of the earliest start seen so far.

Both add complexity with no benefit, so the conventional approach is:
    
1. Sort ascending by start
2. Single left‑to‑right pass to merge


Time complexity remains O(n log n) overall (sort) plus O(n) (scan).
Key takeaway

Any sorting routine is acceptable only if it produces the exact ascending‐by‐start order.
In JavaScript, the simplest, reliable way is
intervals.sort((a, b) => a[0] - b[0]);




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




/**
 * Group active users' names by city.
 *
 * @param {Array<Object>} users – Array of user objects
 * @returns {Object}            – { city: [name1, name2, …], … }
 */
function filterValue(users) {
  const result = {};

  for (const user of users) {
    const profile = user.profile || {};          // fall back to empty object
    if (user.active && profile.city) {           // must be active & have a city
      const city = profile.city.toLowerCase();
      const name = (profile.name || '').toLowerCase();

      if (!result[city]) result[city] = [];      // create bucket if missing
      result[city].push(name);                   // add the name
    }
  }

  return result;
}

/* -------- Example usage -------- */
const users = [
  { profile: { name: 'Tushar',  email: 'tushar@datahash.com',  city: 'bangalore' }, active: true  },
  { profile: { name: 'Sachin',  email: 'sachin@datahash.com',  city: 'bangalore' }, active: true  },
  { profile: { name: 'Rahul',   email: 'rahul@datahash.com',   city: 'gurgaon'   }, active: false },
  { profile: { name: 'Sid',     email: 'sid@datahash.com',     city: 'gurgaon'   }, active: true  },
  { profile: { name: 'John',    email: 'john@datahash.com'                       }, active: true  }
];

console.log(filterValue(users));
// → { bangalore: ['tushar', 'sachin'], gurgaon: ['sid'] }


One‑liner with Array.reduce (same output)

const filterValue = users =>
  users.reduce((acc, { profile = {}, active }) => {
    const { city, name } = profile;
    if (active && city) {
      const key = city.toLowerCase();
      (acc[key] ??= []).push((name || '').toLowerCase());
    }
    return acc;
  }, {});


| #     | Code chunk                                 | What it does                                                                                                                                                                                              |                       |                                                                                                                                                                                                                                                                                                                                                            |
| ----- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | `users.reduce( … , {} )`                   | `Array.reduce` walks the `users` array once, building up an **accumulator** (`acc`). We start that accumulator as an empty object `{}`.                                                                   |                       |                                                                                                                                                                                                                                                                                                                                                            |
| **2** | `(acc, { profile = {}, active }) => { … }` | Arrow‑function callback for `reduce`.  <br>• **Destructuring**: each `user` object is unpacked into `profile` and `active`.  <br>• `profile = {}` sets a default empty object in case the key is missing. |                       |                                                                                                                                                                                                                                                                                                                                                            |
| **3** | `const { city, name } = profile;`          | A second destructuring step pulls `city` and `name` out of the `profile` object.                                                                                                                          |                       |                                                                                                                                                                                                                                                                                                                                                            |
| **4** | `if (active && city) { … }`                | Only proceed when the user is **active** *and* has a city.  (This matches your original Python condition.)                                                                                                |                       |                                                                                                                                                                                                                                                                                                                                                            |
| **5** | `const key = city.toLowerCase();`          | Normalize the city string to lowercase so `"Bangalore"` and `"bangalore"` end up in the same bucket.                                                                                                      |                       |                                                                                                                                                                                                                                                                                                                                                            |
| **6** | \`(acc\[key] ??= \[]).push((name           |                                                                                                                                                                                                           | '').toLowerCase());\` | This single line does two things:  <br>1. **Bucket creation** with the *nullish‑coalescing assignment* operator `??=`:  <br>  • If `acc[key]` is `null` or `undefined`, assign a new empty array `[]` to it.  <br>  • Otherwise leave it unchanged.  <br>2. **Push** the user’s name (lower‑cased, defaulting to empty string if missing) into that array. |
| **7** | `return acc;`                              | Each loop returns the updated accumulator so `reduce` can hand it to the next iteration.                                                                                                                  |                       |                                                                                                                                                                                                                                                                                                                                                            |
| **8** | Result                                     | After the final iteration, `reduce` returns the fully built object, which becomes the function’s output.                                                                                                  |                       |                                                                                                                                                                                                                                                                                                                                                            |


Same flow in plain English
Start with an empty result {}.

For each user:

If they’re active and have a city:

Lower‑case the city (becomes the key).

Make sure there’s an array for that key in the result (??=).

Push the lower‑cased name into that array.

Return the result after the loop ends.

Time complexity is O(n)—just one pass through users. Memory overhead is proportional to the number of unique cities that meet the criteria.


    
    
    
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



/* ---------- Input ---------- */
const data = [
  { hostname: "10.16.08.09", Candidate: "Rajat",  password: "asdadwf" },
  { hostname: "",            Candidate: "Rajat1", password: ""        },
  { hostname: "",            Candidate: "Rajat1", password: ""        },
  { hostname: "",            Candidate: "Rajat1", password: ""        },
];

/* ---------- Step 1 & 2: build the frequency map ---------- */
const candidateCounts = {};

for (const item of data) {
  // Get the candidate name, handle missing field, trim whitespace
  const candidate = (item.Candidate || "").trim();

  if (candidate) { // ignore empty names
    candidateCounts[candidate] = (candidateCounts[candidate] ?? 0) + 1;
  }
}

console.log(candidateCounts, "candidateCounts");

/* ---------- Step 3: find the most frequent candidate ---------- */
let mostFrequentCandidate = null;
let maxCount = 0;

for (const [candidate, count] of Object.entries(candidateCounts)) {
  if (count > maxCount) {
    maxCount = count;
    mostFrequentCandidate = candidate;
  }
}

/* ---------- Step 4: print the result ---------- */
console.log(
  "Most frequent candidate:",
  mostFrequentCandidate ?? "No candidates found"
);


What it prints
{ Rajat: 1, Rajat1: 3 } candidate_counts
Most frequent candidate: Rajat1





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


def first_last_index(Arr, target):
    first, last = -1, -1  # Default values if target is not found
    
    for i, num in enumerate(Arr):  
        if num == target:
            if first == -1:  
                first = i  # Set first occurrence
            last = i  # Update last occurrence
            
    return [first, last]

# Test Cases
Arr = [1, 2, 3, 4, 5, 6, 7, 6, 7, 4, 6, 3, 1, 5, 6, 7, 4, 1]
target = 6
print(first_last_index(Arr, target))  # Output: [5, 14]

target = 9
print(first_last_index(Arr, target))  # Output: [-1, -1]


/**
 * Return the first and last indices where `target` appears in `arr`.
 * If the target is not present, both indices are -1.
 *
 * @param {number[]} arr
 * @param {number}   target
 * @returns {[number, number]}
 */
function firstLastIndex(arr, target) {
  let first = -1;
  let last  = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) {
      if (first === -1) first = i; // first occurrence
      last = i;                    // keep updating last
    }
  }
  return [first, last];
}

/* ---------- Test cases ---------- */
const Arr = [1, 2, 3, 4, 5, 6, 7, 6, 7, 4, 6, 3, 1, 5, 6, 7, 4, 1];

console.log(firstLastIndex(Arr, 6)); // [5, 14]
console.log(firstLastIndex(Arr, 9)); // [-1, -1]



def find_the_value(A, target_key):
    if isinstance(A, list):
        for element in A:
            if isinstance(element, dict):
                result = find_the_value(element, target_key)
                if result is not None:
                    return result
    elif isinstance(A, dict):
        for key, value in A.items():
            if key == target_key:
                return value
            elif isinstance(value, dict) or isinstance(value, list):
                result = find_the_value(value, target_key)
                if result is not None:
                    return result
    return None  # If the key is not found

# Sample dictionary
A = {1: 1, 2: [1, 2, 3, {4: 4, 5: 5}], 6: {7: {8: 8}}}

# Test the function
print(find_the_value(A, 5))  # Output: 5
print(find_the_value(A, 8))  # Output: 8
print(find_the_value(A, 10)) # Output: None (Key not found)



/**
 * Recursively search a nested structure (objects + arrays)
 * for the first occurrence of a given key and return its value.
 *
 * @param {*} data          – the current node (object, array, or primitive)
 * @param {string|number} targetKey – key to look for
 * @returns {*}             – the value if found, otherwise undefined
 */
function findTheValue(data, targetKey) {
  // --- Case 1: Array --------------------------------------------------------
  if (Array.isArray(data)) {
    for (const element of data) {
      if (typeof element === "object" && element !== null) {
        const result = findTheValue(element, targetKey);
        if (result !== undefined) return result;      // early exit if found
      }
    }
  }

  // --- Case 2: Plain object -------------------------------------------------
  else if (typeof data === "object" && data !== null) {
    for (const [key, value] of Object.entries(data)) {
      // JS object keys are strings; loose equality lets 5 match "5"
      if (key == targetKey) return value;

      if (typeof value === "object" && value !== null) {
        const result = findTheValue(value, targetKey);
        if (result !== undefined) return result;      // propagate up
      }
    }
  }

  // --- Not found in this branch --------------------------------------------
  return undefined;
}

/* ---------- Demo ---------- */
const A = {
  1: 1,
  2: [1, 2, 3, { 4: 4, 5: 5 }],
  6: { 7: { 8: 8 } }
};

console.log(findTheValue(A, 5));   // → 5
console.log(findTheValue(A, 8));   // → 8
console.log(findTheValue(A, 10));  // → undefined


| Python concept              | JavaScript counterpart                                                                   |
| --------------------------- | ---------------------------------------------------------------------------------------- |
| `isinstance(x, list)`       | `Array.isArray(x)`                                                                       |
| `isinstance(x, dict)`       | `typeof x === "object" && x !== null` (and **not** an array)                             |
| Recursion and early returns | Identical logic: as soon as a value is found, bubble it up (`return result`)             |
| `None` when not found       | `undefined` when not found                                                               |
| Dict keys can be numbers    | Object keys are stored as strings; using loose equality (`==`) allows `5` to match `"5"` |




