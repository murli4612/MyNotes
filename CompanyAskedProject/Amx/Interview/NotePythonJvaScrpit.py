def move_spaces_to_front_swap(char_list):
    n = len(char_list)
    j = n - 1

    # Traverse from end and move non-space characters to end using swaps
    for i in range(n - 1, -1, -1):
        if char_list[i] != ' ':
            # Swap only if i != j to avoid unnecessary swaps
            char_list[i], char_list[j] = char_list[j], char_list[i]
            j -= 1

# Example usage
s = "move space front"
char_list = list(s)
move_spaces_to_front_swap(char_list)
print(''.join(char_list))


# ✅ Approach (Using Swapping):
# Convert the string into a list (since Python strings are immutable).

# Start from the end of the list and swap non-space characters towards the end.

# Whenever we find a space, we skip it.

# At the end, all non-space characters are at the end and spaces are at the front, due to swaps.
# output
#    movespacefront

# 📌 Key Points:
# No extra array or string used.

# Only uses swaps and a few integer variables.

# Works in-place.


function moveSpacesToFront(str) {
    // Convert string to array since strings are immutable
    let arr = str.split('');
    let j = arr.length - 1;

    // Traverse from end and swap non-space characters to the end
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i] !== ' ') {
            // Swap arr[i] and arr[j]
            let temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            j--;
        }
    }

    return arr.join('');
}

// Example usage
let str = "move space front";
let result = moveSpacesToFront(str);
console.log(result);

🐍 Python List Operations:
| Operation          | Syntax/Example       | Description                             |
| ------------------ | -------------------- | --------------------------------------- |
| Append             | `lst.append(10)`     | Adds an element at the end              |
| Insert             | `lst.insert(2, 99)`  | Inserts 99 at index 2                   |
| Remove (by value)  | `lst.remove(10)`     | Removes first occurrence of 10          |
| Pop (by index)     | `lst.pop(1)`         | Removes and returns item at index 1     |
| Index              | `lst.index(5)`       | Returns index of first occurrence of 5  |
| Count              | `lst.count(2)`       | Counts how many times 2 appears         |
| Sort               | `lst.sort()`         | Sorts the list in place                 |
| Reverse            | `lst.reverse()`      | Reverses the list in place              |
| Extend/Concatenate | `lst.extend([4, 5])` | Adds elements from another list         |
| Slicing            | `lst[1:4]`           | Sublist from index 1 to 3               |
| List comprehension | `[x*x for x in lst]` | Creates a new list with transformations |

🌐 JavaScript Array Operations:
    
| Operation | Syntax/Example           | Description                            |
| --------- | ------------------------ | -------------------------------------- |
| Push      | `arr.push(10)`           | Adds an element at the end             |
| Unshift   | `arr.unshift(99)`        | Adds an element at the start           |
| Pop       | `arr.pop()`              | Removes the last element               |
| Shift     | `arr.shift()`            | Removes the first element              |
| Splice    | `arr.splice(2, 0, 88)`   | Inserts 88 at index 2                  |
| Slice     | `arr.slice(1, 4)`        | Returns a shallow copy from 1 to 3     |
| IndexOf   | `arr.indexOf(5)`         | Returns index of first occurrence of 5 |
| Includes  | `arr.includes(5)`        | Checks if 5 is in the array            |
| Sort      | `arr.sort()`             | Sorts the array                        |
| Reverse   | `arr.reverse()`          | Reverses the array                     |
| Filter    | `arr.filter(x => x > 0)` | Filters elements                       |
| Map       | `arr.map(x => x * x)`    | Transforms elements                    |

🐍 Python List Operations with Code & Notes
1. Append
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

Time complexity: O(1) on average (amortized).

2. Insert
lst = [1, 2, 3]
lst.insert(1, 99)
print(lst)  # [1, 99, 2, 3]

Removes first occurrence. O(n) to find and shift.

4. Pop by Index

lst = [1, 2, 3]
x = lst.pop(1)
print(x, lst)  # 2 [1, 3]


Time complexity: O(n) in worst case (middle element)

5. Sort
lst = [3, 1, 2]
lst.sort()
print(lst)  # [1, 2, 3]

Time complexity: O(n log n), in-place Timsort.

6. List Comprehension
lst = [1, 2, 3]
squares = [x*x for x in lst]
print(squares)  # [1, 4, 9]

Cleaner & faster than map + lambda

🌐 JavaScript Array Operations with Code & Notes
1. Push
let arr = [1, 2, 3];
arr.push(4);
console.log(arr); // [1, 2, 3, 4]

Time complexity: O(1)

2. Unshift (insert at beginning)
let arr = [2, 3];
arr.unshift(1);
console.log(arr); // [1, 2, 3]

Time complexity: O(n) — shifts all elements.

3. Splice (Insert/Remove at index)
let arr = [1, 3, 4];
arr.splice(1, 0, 2); // insert 2 at index 1
console.log(arr); // [1, 2, 3, 4]

Time complexity: O(n) for insert/delete.

let arr = [1, 3, 4];
arr.splice(1, 0, 2);
console.log(arr); // [1, 2, 3, 4]

What it does:
| Argument | Value             | Meaning               |
| -------- | ----------------- | --------------------- |
| `1`      | Start at index 1  | After element `1`     |
| `0`      | Delete 0 elements | No element is removed |
| `2`      | Insert `2`        | Insert at index 1     |

So you're telling JavaScript:

“Go to index 1, delete 0 elements, and insert the value 2 there.”

let arr = [1, 2, 3, 4];
arr.splice(1, 2, 9, 8);
console.log(arr); // [1, 9, 8, 4]

Start at index 1

Delete 2 elements → 2, 3 removed

Insert 9 and 8 at index 1

4. Slice (copy part of array)
let arr = [1, 2, 3, 4];
let sub = arr.slice(1, 3);
console.log(sub); // [2, 3]

Non-destructive. O(k) where k is slice length.

5. Map (transform elements)
let arr = [1, 2, 3];
let squares = arr.map(x => x * x);
console.log(squares); // [1, 4, 9]


Functional, clean. O(n)

6. Filter
let arr = [1, 2, 3, 4];
let even = arr.filter(x => x % 2 === 0);
console.log(even); // [2, 4]

Returns elements that match condition. O(n)
7. Sort
let arr = [3, 1, 2];
arr.sort((a, b) => a - b);
console.log(arr); // [1, 2, 3]

must provide comparator for numeric sort. O(n log n)

✅ 1. Mutation vs Non-Mutation Behavior
In both Python and JavaScript, some list/array methods mutate (change) the original data, 
while others return a new copy and leave the original unchanged.

| Method          | Mutates? | Description                       |
| --------------- | -------- | --------------------------------- |
| `append()`      | ✅ Yes    | Adds item to the end              |
| `insert()`      | ✅ Yes    | Inserts at index                  |
| `remove()`      | ✅ Yes    | Removes first matching value      |
| `pop()`         | ✅ Yes    | Removes item at index             |
| `sort()`        | ✅ Yes    | Sorts list in place               |
| `reverse()`     | ✅ Yes    | Reverses in place                 |
| `+`, `sorted()` | ❌ No     | Returns new list (concat or sort) |
| `list.copy()`   | ❌ No     | Returns a shallow copy            |
| List comp       | ❌ No     | Creates a new list                |

🌐 JavaScript:
| Method              | Mutates? | Description                       |
| ------------------- | -------- | --------------------------------- |
| `push()`            | ✅ Yes    | Adds item to end                  |
| `pop()`             | ✅ Yes    | Removes item from end             |
| `shift()`           | ✅ Yes    | Removes first item                |
| `unshift()`         | ✅ Yes    | Adds item to start                |
| `splice()`          | ✅ Yes    | Inserts/removes/replaces in place |
| `sort()`            | ✅ Yes    | Sorts in place                    |
| `reverse()`         | ✅ Yes    | Reverses in place                 |
| `slice()`           | ❌ No     | Returns shallow copy              |
| `map()`, `filter()` | ❌ No     | Returns a new array               |

✅ 2. Advanced Operations: reduce, zip, flatMap
🔁 reduce (Python & JS)
Used to reduce an array/list to a single value.

Python:
from functools import reduce
nums = [1, 2, 3, 4]
sum = reduce(lambda a, b: a + b, nums)
print(sum)  # 10

JavaScript:
const nums = [1, 2, 3, 4];
const sum = nums.reduce((a, b) => a + b, 0);
console.log(sum);  // 10

🔗 zip (Python)
Combines multiple lists element-wise.
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]

❌ No built-in zip() in JS, but you can emulate it:

function zip(a, b) {
  return a.map((k, i) => [k, b[i]]);
}
console.log(zip([1, 2, 3], ['a', 'b', 'c'])); // [[1, 'a'], [2, 'b'], [3, 'c']]

🌱 flatMap (JS only)
Maps and flattens the result (one level deep).

const arr = [1, 2, 3];
const result = arr.flatMap(x => [x, x * 2]);
console.log(result); // [1, 2, 2, 4, 3, 6]

Equivalent in Python (list comprehension):
arr = [1, 2, 3]
result = [y for x in arr for y in (x, x*2)]
print(result)  # [1, 2, 2, 4, 3, 6]

✅ 3. Performance Tips for Large Arrays/Lists
| Goal                         | Python Tip                                   | JavaScript Tip                          |
| ---------------------------- | -------------------------------------------- | --------------------------------------- |
| Avoid repeated `+` or `push` | Use `append()` or `extend()`                 | Use `push()`, pre-allocate if needed    |
| Avoid mutation in loops      | Prefer list comprehensions                   | Use `map()` or `reduce()`               |
| Fastest lookups              | Use `set` or `dict` for O(1) lookups         | Use `Set` or `Map`                      |
| Memory efficiency            | Use generators (`yield`) for large sequences | Use iterators where possible            |
| Parallel processing          | Use multiprocessing, NumPy, pandas           | Use Web Workers for CPU-intensive tasks |
| Avoid deeply nested arrays   | Flatten smartly (`itertools.chain`)          | Use `flat()` or `flatMap()`             |
| Sorting                      | Built-in sort is optimized                   | Avoid custom sorts unless needed        |

🐍 Python: join()
📘 Syntax:
'separator'.join(iterable)

✅ Example:
words = ['hello', 'world']
sentence = ' '.join(words)
print(sentence)  # Output: "hello world"

🔸 Notes:
The iterable must contain strings.

If not, you need to convert them:

nums = [1, 2, 3]
print(','.join(map(str, nums)))  # "1,2,3"

🌐 JavaScript: join()
📘 Syntax:

array.join(separator)

✅ Example:
const words = ['hello', 'world'];
const sentence = words.join(' ');
console.log(sentence);  // Output: "hello world"

🔸 Notes:
Works on arrays.

Converts all elements to strings automatically.
const nums = [1, 2, 3];
console.log(nums.join(','));  // "1,2,3"

⚖️ Summary Table
| Feature       | Python                                  | JavaScript          |
| ------------- | --------------------------------------- | ------------------- |
| Function name | `'sep'.join(list)`                      | `array.join('sep')` |
| Input type    | Iterable of strings (convert if needed) | Array of any type   |
| Output        | A single string                         | A single string     |

🧩 1. Join Nested Lists
🐍 Python Example:
Convert a 2D list into a string (e.g., CSV-style):
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

for row in data:
    line = ','.join(row)
    print(line)
📤 Output:
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles

🌐 JavaScript Example:
const data = [
  ['Name', 'Age', 'City'],
  ['Alice', '30', 'New York'],
  ['Bob', '25', 'Los Angeles']
];

data.forEach(row => {
  const line = row.join(',');
  console.log(line);
});

📤 Output:

Name,Age,City
Alice,30,New York
Bob,25,Los Angeles

📄 2. Create CSV File Content
🐍 Python: CSV string from nested list
data = [
    ['Name', 'Age'],
    ['Tom', '32'],
    ['Sara', '29']
]

csv_string = '\n'.join([','.join(row) for row in data])
print(csv_string)

📤 Output:
Name,Age
Tom,32
Sara,29

🌐 JavaScript: CSV string from nested array
const data = [
  ['Name', 'Age'],
  ['Tom', '32'],
  ['Sara', '29']
];

const csvString = data.map(row => row.join(',')).join('\n');
console.log(csvString);

📤 Output:
Name,Age
Tom,32
Sara,29

✨ Extras
✅ File Writing (Python):
with open('output.csv', 'w') as f:
    f.write(csv_string)

✅ Browser Download (JavaScript):
const blob = new Blob([csvString], { type: 'text/csv' });
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'output.csv';
a.click();

1. Quoting cells (handling commas, quotes, etc.)
When CSV cells contain commas, quotes, or newlines, these must be escaped properly by quoting the whole cell and doubling internal quotes.

🐍 Python: Using the built-in csv module
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York, NY'],    # comma inside cell
    ['Bob', '25', 'Los "Angeles"']      # quotes inside cell
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)

This automatically quotes and escapes cells with special characters.
🌐 JavaScript: Manually quoting CSV cells
function quoteCell(cell) {
  if (typeof cell === 'string' && (cell.includes(',') || cell.includes('"') || cell.includes('\n'))) {
    return '"' + cell.replace(/"/g, '""') + '"';
  }
  return cell;
}

const data = [
  ['Name', 'Age', 'City'],
  ['Alice', '30', 'New York, NY'],
  ['Bob', '25', 'Los "Angeles"']
];

const csvString = data
  .map(row => row.map(quoteCell).join(','))
  .join('\n');

console.log(csvString);



🔷 JavaScript: Map
A Map is a key-value data structure, similar to an object {},
but with better flexibility and some useful features.

✅ Key Features of Map:
| Feature           | `Map`                               | `Object`                  |
| ----------------- | ----------------------------------- | ------------------------- |
| Key types         | Any type (objects, functions, etc.) | Only strings/symbols      |
| Order preserved?  | ✅ Yes (insertion order)             | ❌ No guarantee            |
| Iteration methods | `.forEach()`, `.entries()`          | Harder without conversion |
| Size              | `.size` property                    | `Object.keys(obj).length` |

const map = new Map();

// Setting key-value pairs
map.set("name", "Alice");
map.set("age", 30);
map.set(42, "answer");
map.set({ key: "obj" }, "object value");

console.log(map.get("name"));      // Alice
console.log(map.has("age"));       // true
console.log(map.size);             // 4

// Iterating
for (const [key, value] of map) {
  console.log(`${key}: ${value}`);
}

// Deleting
map.delete("age");
map.clear();  // Removes all entries

🐍 Python: dict
Python's built-in dict is very similar to JavaScript’s Map.

🔹 Example in Python:
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

🔄 Common Operations (Comparison)
| Operation  | JavaScript (`Map`)    | Python (`dict`)            |
| ---------- | --------------------- | -------------------------- |
| Add / Set  | `map.set(key, value)` | `dict[key] = value`        |
| Get value  | `map.get(key)`        | `dict[key]`                |
| Check key  | `map.has(key)`        | `key in dict`              |
| Delete key | `map.delete(key)`     | `del dict[key]`            |
| Clear all  | `map.clear()`         | `dict.clear()`             |
| Size       | `map.size`            | `len(dict)`                |
| Iterate    | `for ([k, v] of map)` | `for k, v in dict.items()` |

🧠 Extra Note:
Python dict from version 3.7+ also preserves insertion order, just like JavaScript's Map.

JavaScript’s Map is more versatile if you need to use objects, arrays, or functions as keys.

🔹 2. defaultdict in Python (no direct JS equivalent)
✅ Use Case:
Automatically initializes values for new keys.

from collections import defaultdict

count = defaultdict(int)
count['a'] += 1
count['b'] += 1
print(count)  # {'a': 1, 'b': 1}

You can also use list, set, or custom lambdas:
group = defaultdict(list)
group['fruit'].append('apple')
group['fruit'].append('banana')


Key differences to note between the Python and JavaScript versions:

JavaScript uses const/let instead of Python's variable declarations

JavaScript uses for...of loops instead of Python's for...in

JavaScript uses {} for objects/dictionaries instead of Python's {}

JavaScript uses in operator to check for property existence, similar to Python

JavaScript uses join('') on arrays instead of Python's ''.join()

JavaScript uses console.log() instead of Python's print()

