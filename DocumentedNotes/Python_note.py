Beginner Level
What are Python’s key features?
How is Python an interpreted language?
What is the difference between list, tuple, and set?
What is the difference between deepcopy() and copy()?
What is the difference between is and ==?
What are Python’s built-in data types?
What are *args and **kwargs?
How does memory management work in Python?
What are Python’s scope rules (LEGB rule)?
What is the difference between staticmethod and classmethod?

1)What are Python’s key features?
Python has several key features that make it a popular programming language:

Easy to Learn and Use – Python has a simple syntax that makes it easy for beginners to learn and use.

Interpreted Language – Python is an interpreted language, meaning code is executed line by line without needing compilation.

Dynamically Typed – Variables do not need explicit declaration; their types are determined at runtime.

High-Level Language – Python allows developers to write programs with minimal concern about low-level details like memory management.

Object-Oriented and Functional – Python supports object-oriented programming (OOP) as well as functional programming paradigms.

Extensive Libraries – Python comes with a vast standard library and third-party modules for diverse functionalities, including web development, machine learning, and networking.

Platform-Independent – Python is cross-platform and runs on Windows, macOS, and Linux without modification.

Embeddable and Extensible – Python code can be embedded into other programming languages and extended using C/C++.

Automatic Memory Management – Python has built-in garbage collection that manages memory automatically.

Multi-Paradigm Support – Python supports different programming paradigms, including procedural, object-oriented, and functional programming.

Strong Community Support – Python has a large and active community that provides extensive documentation, tutorials, and third-party tools.

These features make Python versatile and suitable for various applications, including web development, data science, artificial intelligence, automation, and more.


2)How is Python an interpreted language?

Python is considered an interpreted language because its code is executed line by line by the Python interpreter rather than being compiled into machine code all at once.
 Here’s how it works:

1. Execution Process in Python
When you run a Python script, the following steps occur:

Source Code (.py file) → Written by the developer.
Compilation to Bytecode (.pyc file) → The Python interpreter first compiles the code into an intermediate form called bytecode (not machine code).
Interpretation by the Python Virtual Machine (PVM) → The bytecode is executed by the Python interpreter (PVM), which translates it into machine-specific instructions.

2. Why is Python Interpreted?

No need for explicit compilation: Unlike languages like C or Java, Python does not require separate compilation before execution.
Portability: Since the PVM interprets the bytecode, the same Python script can run on different platforms (Windows, macOS, Linux) without modification.
Dynamic Typing: Python determines variable types at runtime, which is possible due to interpretation.

3. Is Python Purely Interpreted?
Python is not purely interpreted because it first compiles the code to bytecode before interpretation. This makes it partially compiled and interpreted.


Python Execution Process: Compiled vs. Interpreted Languages
Python is often called an interpreted language, but in reality, it follows a hybrid approach where it is both
 compiled and interpreted. Let's break this down and compare it to fully compiled languages like C.
 
 
 1. How Python Executes Code
When you run a Python program, it follows these steps:

Step 1: Compilation to Bytecode
Python first compiles the .py (source code) file into an intermediate form called bytecode.
This bytecode is not machine code but a lower-level representation of your code that is platform-independent.
The compiled bytecode is stored in .pyc (Python compiled) files inside the __pycache__ folder.

🔹 Example: Running python my_script.py internally creates a my_script.pyc file.

Step 2: Interpretation by Python Virtual Machine (PVM)
The Python Virtual Machine (PVM) reads and executes the bytecode line by line.
The PVM translates the bytecode into machine instructions that the CPU understands.
This is where Python behaves as an interpreted language, since the execution happens dynamically at runtime.


2. How Python Differs from Fully Compiled Languages (C, C++)
Feature	Python (Interpreted + Compiled)                  	    C/C++ (Fully Compiled)
Compilation	   Compiles to bytecode (.pyc) before execution	    Compiles directly to machine code (.exe, .out)
Execution	   Bytecode is interpreted by PVM	                Runs directly on hardware
Speed	       Slower (due to interpretation)	                Faster (native execution)
Portability    High (bytecode runs on any OS with Python)	    Low (compiled binary depends on OS & CPU architecture)
Debugging      Easier (runtime errors can be caught quickly)	Harder (requires recompilation for each change)


3. Is Python Fully Interpreted?
🔹 No, because it has a compilation step.
🔹 Yes, because execution still happens via an interpreter (PVM).

So, Python is a hybrid language—it is compiled to bytecode and then interpreted at runtime.


3)What is the difference between is and ==?

difference Between is and == in Python
Both is and == are comparison operators, but they serve different purposes:
    
Operator	Purpose	             Compares	                            Example Usage
==	        Equality Operator	Values of objects	                    a == b checks if values are the same
is	        Identity Operator	Memory location (identity) of objects	a is b checks if both refer to the same object



1. == (Equality Operator) - Compares Values
The == operator checks if two objects have the same value, regardless of whether they are stored at the same memory location.
✅ Example: == checks value equality

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (Values are the same)
print(a is b)  # False (Different memory locations)

🔹 Even though a and b have the same contents ([1, 2, 3]), they are stored at different memory locations.

2. is (Identity Operator) - Checks Memory Location
The is operator checks whether two variables point to the same object in memory.
✅ Example: is checks object identity

x = [10, 20, 30]
y = x  # Both refer to the same object

print(x == y)  # True  (Values are the same)
print(x is y)  # True  (Same memory location)


🔹 Since y = x, both x and y point to the same memory address.

3. Special Case: is Works Differently for Immutable Objects
Python caches small integers (-5 to 256) and short strings for optimization. This can sometimes make is return True unexpectedly.

✅ Example with Small Integers (Immutable Objects)

a = 100
b = 100
print(a is b)  # True (Same cached object)

c = 1000
d = 1000
print(c is d)  # False (Different objects in memory)


🔹 Why does 1000 is 1000 return False?
Python only caches small integers (-5 to 256), but numbers beyond this range are stored separately.

✅ Example with Strings (Immutable Objects)

s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True (String interning)

s3 = "hello world!"
s4 = "hello world!"
print(s3 is s4)  # False (Not interned, different memory locations)


🔹 Why does "hello world!" is "hello world!" return False?

Short strings are interned (stored in a common memory location).
Longer strings are stored separately, so is may return False.


4. When to Use is vs ==
✅ Use == when checking values

Example: Comparing numbers, lists, strings, etc.
"Python" == "Python" ✅
[1, 2] == [1, 2] ✅
✅ Use is when checking if two variables point to the same object

Example: Checking None, singletons, or identity comparison
x is None ✅
a is b (only if you want to check if a and b are literally the same object) ✅



Python Memory Management and Garbage Collection

Python handles memory management automatically using dynamic memory allocation and a garbage collector. 
It relies on reference counting and a cyclic garbage collector to free unused memory. Let’s break it down:
    
1. Memory Management in Python
Python’s memory management involves:

Python Memory Manager → Manages memory allocation for objects.
Private Heap Space → Stores all Python objects and data structures.
Reference Counting → Tracks how many references exist for an object.
Garbage Collector → Removes unused objects to free memory.

2. Reference Counting in Python
Every object in Python has a reference count, which is the number of times the object is referenced. When an object’s reference count reaches zero, it is automatically deleted.

✅ Example: Reference Counting

import sys

x = [1, 2, 3]  # Create a list
print(sys.getrefcount(x))  # Output: 2 (one for x, one for getrefcount argument)

y = x  # Another reference to the same object
print(sys.getrefcount(x))  # Output: 3 (x, y, and getrefcount argument)

del x  # Delete one reference
print(sys.getrefcount(y))  # Output: 2 (y and getrefcount argument)

🔹 Issue: Reference counting cannot handle circular references, where objects reference each other.

3. Circular References and Garbage Collection
Circular references occur when two objects refer to each other, preventing their reference count from reaching zero.

✅ Example: Circular Reference

class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

a = Node(10)
b = Node(20)
a.ref = b  # a → b
b.ref = a  # b → a (circular reference)

del a
del b
# Memory leak! Reference counts never reach zero

🔹 Solution: Python’s garbage collector detects and removes cyclic references.

4. Python’s Garbage Collector (gc Module)
Python has a built-in garbage collector (GC) that:
✅ Detects cyclic references.
✅ Uses generational garbage collection (divides objects into "young", "middle-aged", "old" groups).
✅ Runs automatically, but can be manually controlled using the gc module.

✅ Example: Manually Running Garbage Collection

import gc

gc.collect()  # Forces garbage collection

🔹 gc module functions:

gc.get_count() → Returns number of objects in each generation.
gc.collect() → Forces garbage collection.
gc.set_threshold(700, 10, 10) → Adjusts GC sensitivity.


5. Generational Garbage Collection
Python divides objects into three generations:



Generation	         Objects	                    Collection Frequency
Gen 0 (Young)	     Newly created objects	        Frequent
Gen 1 (Middle-aged)	 Survived one GC cycle	        Less frequent
Gen 2 (Old)	         Survived multiple GC cycles	Least frequent

🔹 Why generational GC?

Most objects die young → Newly created objects are more likely to be garbage.
Efficient collection → Older objects are scanned less often, saving time.
✅ Example: Checking Object Generations

import gc

x = [1, 2, 3]
print(gc.get_count())  # Check object count in each generation

6. Memory Optimization Techniques in Python

1. Use del to Remove Unused Variables

x = [1, 2, 3]
del x  # Removes reference, allowing GC to reclaim memory

2. Use Weak References (weakref Module)

import weakref

class Example:
    pass

obj = Example()
weak_obj = weakref.ref(obj)  # Creates a weak reference (doesn't increase ref count)
print(weak_obj())  # Output: <__main__.Example object at 0x...>


3. Use slots to Reduce Memory Overhead
By default, Python objects use a dictionary (__dict__) for attributes, which consumes extra memory. Using __slots__ prevents this.

class Optimized:
    __slots__ = ['x', 'y']  # No dictionary, only allocated slots

obj = Optimized()
obj.x = 10
obj.y = 20


4. Use Generators Instead of Lists

def gen_numbers():
    for i in range(1000000):
        yield i  # Saves memory by generating values on demand

nums = gen_numbers()
print(next(nums))  # Output: 0


Conclusion
✔ Python uses reference counting and garbage collection for memory management.
✔ Generational garbage collection improves efficiency.
✔ Circular references are handled by the GC.
✔ Optimizing memory with del, weakref, __slots__, and generators helps reduce overhead.



1. Memory Profiling in Python
Using memory_profiler to Track Memory Usage
The memory_profiler module helps analyze memory consumption.

✅ Installation
pip install memory-profiler

✅ Example: Profiling a Function
Use the @profile decorator to track memory usage.

from memory_profiler import profile

@profile
def create_large_list():
    lst = [i for i in range(1000000)]  # Large list consuming memory
    return lst

create_large_list()

🔹 Run the script using:

python -m memory_profiler script.py

🔹 Output: Shows memory usage before and after function execution.

2. Debugging Memory Leaks in Python

Using objgraph to Detect Memory Leaks
The objgraph module helps track objects and memory leaks.

✅ Installation
pip install objgraph

✅ Example: Finding Objects Not Getting Collected
import objgraph

class LeakyClass:
    pass

def create_leak():
    a = LeakyClass()
    b = LeakyClass()
    a.ref = b  # Circular reference
    b.ref = a

create_leak()

# Find most common object types
objgraph.show_most_common_types()

🔹 Output: Shows objects consuming the most memory.

✅ Example: Visualizing Memory Leaks


import objgraph

objgraph.show_backrefs([LeakyClass()], filename="leak.png")

🔹 Generates a graph showing references that prevent garbage collection.

3. Manually Running Garbage Collection (gc Module)
If objects are not being collected, manually run the garbage collector.

import gc

gc.collect()  # Forces garbage collection
print(gc.get_stats())  # Shows statistics of collected objects


4. Using tracemalloc to Track Memory Usage Over Time
Python’s built-in tracemalloc module helps track memory allocations

✅ Example: Comparing Memory Usage Before and After a Function

import tracemalloc

tracemalloc.start()  # Start tracking memory

def memory_intensive_task():
    return [i for i in range(1000000)]  # Large memory usage

memory_intensive_task()

# Compare memory usage
print(tracemalloc.get_traced_memory())

tracemalloc.stop()


🔹 Output: (current_memory_usage, peak_memory_usage)


Conclusion
✔ Use memory_profiler for function-level memory tracking.
✔ Use objgraph to detect circular references and leaks.
✔ Use gc.collect() to manually trigger garbage collection.
✔ Use tracemalloc for tracking memory allocations over time.

q3) What is the difference between list, tuple, and set?

In Python, list, tuple, and set are all data structures used to store collections of elements, but they have key differences in mutability, order, and uniqueness.

1. List (list)
Mutable: Can be modified (elements can be added, removed, or changed).
Ordered: Maintains the order of elements as inserted.
Allows Duplicates: Can contain duplicate values.
Syntax: Created using square brackets [].
Example:


my_list = [1, 2, 3, 4, 2]  # Duplicates allowed
my_list.append(5)  # Modifiable
print(my_list)  # Output: [1, 2, 3, 4, 2, 5]


2. Tuple (tuple)
Immutable: Cannot be modified after creation (elements cannot be added, removed, or changed).
Ordered: Maintains insertion order.
Allows Duplicates: Can contain duplicate values.
Syntax: Created using parentheses ().
Example:

my_tuple = (1, 2, 3, 4, 2)  # Duplicates allowed
print(my_tuple[1])  # Output: 2


3. Set (set)
Mutable: Can add or remove elements, but individual elements are immutable.
Unordered: Does not maintain any specific order.
Unique Elements Only: Does not allow duplicate values.
Syntax: Created using curly braces {}.
Example:

my_set = {1, 2, 3, 4, 2}  # Duplicates are automatically removed
my_set.add(5)  # Can add elements
print(my_set)  # Output: {1, 2, 3, 4, 5}


Key Differences Summary

Feature	      List	              Tuple	               Set
Mutability	  Mutable	          Immutable	           Mutable (but unordered)
Order	      Ordered	          Ordered	           Unordered
Duplicates	  Allowed	          Allowed	           Not allowed
Syntax        []	              ()	               {}
Performance  Slower (modifiable)  Faster (fixed size)	Faster for lookups


Each data structure is useful in different scenarios. Use lists when you need an ordered, modifiable collection,
 tuples when immutability is required, and sets when uniqueness and fast lookups are important.
 
 
 q5)What is the difference between deepcopy() and copy()?
 
 In Python, both copy() and deepcopy() are used to create copies of objects, but they behave differently when dealing with nested objects 
 (objects containing other objects, like lists of lists).

1. copy.copy() (Shallow Copy)
Creates a new object, but does not create copies of nested objects.
Changes in the nested objects of the copied object will affect the original object.
Only copies the reference of nested objects, not their actual values.

Example of Shallow Copy:

import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)

shallow_copy[0][0] = 100  # Modifying nested list

print(original_list)  # Output: [[100, 2, 3], [4, 5, 6]]
print(shallow_copy)   # Output: [[100, 2, 3], [4, 5, 6]]

✅ The outer list is copied, but inner lists are still shared!


2. copy.deepcopy() (Deep Copy)
Creates a completely independent copy of the original object, including all nested objects.
Changes in the copied object's nested elements do not affect the original object.
Recursively copies all objects.

Example of Deep Copy:

import copy

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original_list)

deep_copy[0][0] = 100  # Modifying nested list

print(original_list)  # Output: [[1, 2, 3], [4, 5, 6]]
print(deep_copy)      # Output: [[100, 2, 3], [4, 5, 6]]


✅ The inner lists are also copied, preventing unwanted modifications to the original object.


Key Differences Summary
Feature	                copy.copy() (Shallow Copy)	                       copy.deepcopy() (Deep Copy)
Copy Level	            Only creates a new outer object	                   Creates a new object and copies all nested objects
Nested Objects	         References are shared	                            Fully copied and independent
Performance	             Faster                                         	Slower (more memory usage)
Modification Effect	    Changes in nested objects affect the original	    Changes in copied object do not affect the original



When to Use?
Use copy.copy() when your object does not contain nested mutable objects or when you want shared references.
Use copy.deepcopy() when you need a completely independent copy of an object.


q6)What are Python’s built-in data types?

1. Numeric Types

Data Type                   Description	                                           Example
int	                       Integer numbers	                                       x = 10
float	                   Floating-point numbers (decimal values)	                    y = 3.14
complex                 	Complex numbers (with real & imaginary parts)	          z = 2 + 3j


2. Sequence Types
Data Type            Description	                                    Example
list	Ordered, mutable collection of elements  	       my_list = [1, 2, 3]
tuple	Ordered, immutable collection of elements	      my_tuple = (1, 2, 3)
range	Generates a sequence of numbers	                r = range(5) # (0,1,2,3,4)



3. Text Type
Data Type	Description	Example
str	Sequence of characters (immutable)	text = "Hello"


4. Set Types
Data Type	Description	Example
set	Unordered collection of unique elements	my_set = {1, 2, 3}
frozenset	Immutable version of a set	frozen = frozenset({1, 2, 3})


5. Mapping Type
Data Type	Description	Example
dict	Key-value pairs (mutable)	my_dict = {"name": "John", "age": 25}

6. Boolean Type
Data Type	Description	Example
bool	Represents True or False values	status = True


7. Binary Types
Data Type	Description	Example
bytes	Immutable sequence of bytes	b = b"Hello"
bytearray	Mutable sequence of bytes	ba = bytearray(5)
memoryview	Memory-efficient view of bytes	mv = memoryview(b"Hello")

8. None Type
Data Type	Description	Example
NoneType	Represents the absence of a value	x = None



What are *args and **kwargs?

*args and **kwargs in Python
*args and **kwargs allow flexible function arguments, enabling a function to accept any number of arguments.


1. *args (Non-Keyword Arguments)
*args allows a function to accept any number of positional arguments.
Inside the function, args is treated as a tuple.

def add_numbers(*args):
    return sum(args)  # args is a tuple of numbers

print(add_numbers(1, 2, 3))      # Output: 6
print(add_numbers(10, 20, 30, 40))  # Output: 100


✅ *args lets you pass any number of arguments without defining them individually.

2. **kwargs (Keyword Arguments)
**kwargs allows a function to accept any number of keyword arguments.
Inside the function, kwargs is treated as a dictionary where keys are argument names.
Example:
    
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")

Output:
 name: Alice
age: 25
city: New York


✅ **kwargs lets you pass named arguments dynamically.


3. Using *args and **kwargs Together
You can combine *args and **kwargs in a function:
 
 def person_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

person_info(1, 2, 3, name="Bob", age=30)

Output:
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Bob', 'age': 30}


4. Unpacking with *args and **kwargs
Using * to Unpack Lists/Tuples

numbers = [1, 2, 3]
print(add_numbers(*numbers))  # Equivalent to add_numbers(1, 2, 3)


Using ** to Unpack Dictionaries

person = {"name": "Charlie", "age": 28}
display_info(**person)  # Equivalent to display_info(name="Charlie", age=28)


Key Differences:
Feature	*args	**kwargs
Accepts	Any number of positional arguments	Any number of keyword arguments
Data Type	Tuple	Dictionary
Use Case	When arguments don’t have names	When arguments have names (key-value pairs)



Memory Management in Python
Python uses automatic memory management with garbage collection, reference counting, 
and memory pools to efficiently allocate and free memory. Below are the key concepts:
    


1. Memory Allocation in Python
Python divides memory into different segments:

Stack Memory:

Stores function calls, local variables, and references to objects.
It follows a Last-In-First-Out (LIFO) structure.
Automatically cleaned up when a function ends.


Heap Memory:
Stores objects and dynamically allocated variables.
Managed by Python’s Memory Manager (PyMalloc).


Object-Specific Allocators:
Python has specialized memory pools for different types of objects (integers, strings, lists, etc.), reducing fragmentation and improving performance.


2. Reference Counting
Python keeps track of the number of references to an object using reference counting.
When an object’s reference count reaches zero, it is automatically deallocated.
Example of Reference Counting

import sys

x = [1, 2, 3]  # A list is created
y = x  # Reference count increases
print(sys.getrefcount(x))  # Output: 3 (x, y, and function argument)

del y  # Reference count decreases
print(sys.getrefcount(x))  # Output: 2

🔴 Problem: Circular references (e.g., two objects referring to each other) can prevent memory from being freed.



3. Garbage Collection (GC)
Python has an automatic Garbage Collector (GC) to handle memory that reference counting cannot free, such as circular references.

Python uses generational garbage collection (objects are divided into three generations: young, middle-aged, and old).
Objects that survive multiple collections are moved to older generations.


Forcing Garbage Collection
import gc

gc.collect()  # Manually trigger garbage collection



Summary of Python Memory Management
Feature	Description
Reference Counting	Tracks the number of references to an object.
Garbage Collector	Handles circular references using generational GC.
Memory Pools	Python uses object-specific allocators to reduce fragmentation.
Stack vs Heap	Stack stores local variables; heap stores dynamically allocated objects.


q9) What are Python’s scope rules (LEGB rule)?

Python’s Scope Rules: The LEGB Rule
Python follows the LEGB rule to determine the scope of variables when searching for a name.

🔹 LEGB stands for:

L → Local (Innermost)
E → Enclosing (Nonlocal)
G → Global
B → Built-in (Outermost)
When a variable is referenced inside a function, Python searches in this order:
    


1. Local Scope (L)
The innermost scope: variables inside a function.
These variables exist only within the function.
Python first looks for a variable in this scope.

def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  # ❌ Error: 'x' is not defined outside the function



2. Enclosing Scope (E)
If a variable is not found in the local scope, Python looks in the enclosing scope (outer functions).
Used in nested functions.
Use the nonlocal keyword to modify a variable in an enclosing scope.

Example:

def outer():
    x = "Enclosing"

    def inner():
        nonlocal x
        x = "Modified"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()


Output:
    Inner: Modified
    Outer: Modified
    
 🔹 Without nonlocal, the inner function would create a new local variable instead of modifying the enclosing one.
 
 def outer():
    x = "Enclosing"

    def inner():
        # nonlocal x
        x = "Modified"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
out:
    Inner: Modified
    Outer: Enclosing  
 
 
 3. Global Scope (G)
If Python doesn’t find a variable in local or enclosing scopes, it looks in the global scope.
Global variables are defined outside functions and are accessible everywhere.
Use global to modify a global variable inside a function.
Example:
    
x = "Global"

def my_function():
    global x
    x = "Modified in function"

my_function()
print(x)  # Output: Modified in function


🔹 Without global, the function would create a new local variable, leaving the global x unchanged.



4. Built-in Scope (B)
If Python doesn’t find the variable in L, E, or G, it checks the built-in scope (Python’s predefined functions & modules).
Includes built-in functions like print(), len(), range(), etc.
Example:
    
    print(len("Hello"))  # 'len' is a built-in function


LEGB Rule in Action

x = "Global"  # Global variable

def outer():
    x = "Enclosing"  # Enclosing variable

    def inner():
        x = "Local"  # Local variable
        print(x)  # Searches: Local → Enclosing → Global → Built-in

    inner()

outer()  # Output: Local


🔹 The function inner() first finds x = "Local" and stops searching further.


Key Takeaways
Scope	Description	Modifiable?	Example
Local (L)	Inside the current function	✅ Yes	x inside inner()
Enclosing (E)	In an outer function	✅ With nonlocal	x inside outer()
Global (G)	At the script level	✅ With global	x = "Global"
Built-in (B)	Predefined Python functions	❌ No	len(), print()

q10)What is the difference between staticmethod and classmethod?

Difference Between @staticmethod and @classmethod in Python
Both @staticmethod and @classmethod define methods that don’t operate on an instance of a class. However, they have key differences:


1. @staticmethod (Static Method)
Does not receive self (instance) or cls (class).
Acts like a regular function but inside a class.
It does not modify or access class/instance attributes.
Used for utility functions related to a class but independent of class instances.
Example:
    
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y  # No access to class or instance attributes

print(MathOperations.add(5, 3))  # Output: 8

🔹 No self or cls → Pure function inside the class.


Example of @staticmethod with a Static Variable
Static variables (class variables) belong to the class and are shared across all instances. 
A @staticmethod can read static variables but cannot modify them (since it does not have access to cls or self).

Example 1: Using a Static Method with a Static Variable

class Counter:
    count = 0  # Static (class) variable

    @staticmethod
    def show_count():
        """Static method to access the static variable"""
        return f"Current count: {Counter.count}"

# Access static method without creating an instance
print(Counter.show_count())  # Output: Current count: 0

# Modify static variable
Counter.count += 5
print(Counter.show_count())  # Output: Current count: 5


🔹 show_count() can access Counter.count but cannot modify it.


Example 2: Using a Static Method for Utility Computations with Static Variables

class TemperatureConverter:
    conversion_factor = 1.8  # Static variable

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit using a static variable"""
        return (celsius * TemperatureConverter.conversion_factor) + 32

# Calling the static method without an instance
print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0


🔹 celsius_to_fahrenheit() accesses conversion_factor, but cannot change it.

Example 3: Preventing Modification of Static Variables Inside Static Methods

class Config:
    max_connections = 100  # Static variable

    @staticmethod
    def update_max_connections(new_value):
        """Trying to modify the static variable (but this won't work)"""
        # Config.max_connections = new_value  ❌ Not recommended (modification is not expected)
        print("Cannot modify class variables inside a static method!")

# Calling the static method
Config.update_max_connections(200)  # Output: Cannot modify class variables inside a static method!

# Directly modifying the static variable
Config.max_connections = 200
print(Config.max_connections)  # Output: 200


🔹 Static methods are meant for utility functions, not for modifying class variables.

When to Use Static Methods with Static Variables?
✅ When you need a helper function that only reads class-level data.
✅ When you want to avoid modifying shared data inside methods.
✅ When a method logically belongs to a class but doesn’t require instance/class references.


Advanced Examples of @staticmethod with Static Variables
Here are some real-world scenarios where @staticmethod works with static variables efficiently.


Example 1: Logger Class for Event Tracking
🔹 A logger system where all logs are stored in a static list.
🔹 @staticmethod is used to retrieve logs without modifying them.

class Logger:
    logs = []  # Static variable (shared by all instances)

    @staticmethod
    def show_logs():
        """Static method to read logs without modifying"""
        return Logger.logs

# Adding logs (modifying the static variable directly)
Logger.logs.append("System started")
Logger.logs.append("User logged in")

# Using static method to retrieve logs
print(Logger.show_logs())  
# Output: ['System started', 'User logged in']


🔹 show_logs() can access the logs variable but does not modify it.


Example 2: Database Connection Pool Management
🔹 Static variable keeps track of maximum connections allowed.
🔹 @staticmethod helps in checking available slots.

class Database:
    max_connections = 5  # Static variable
    active_connections = 0  # Static variable

    @staticmethod
    def can_connect():
        """Checks if a new connection can be created"""
        return Database.active_connections < Database.max_connections

# Checking connection availability
print(Database.can_connect())  # Output: True

# Modifying static variable (outside static method)
Database.active_connections = 5  # All slots are filled
print(Database.can_connect())  # Output: False



🔹 can_connect() reads the static variable but does not modify it.

Example 3: Generating Unique Order IDs
🔹 A class to generate order IDs using a static variable.
🔹 @staticmethod is used for reading the last assigned ID.


class Order:
    last_order_id = 1000  # Static variable

    @staticmethod
    def get_last_order_id():
        """Returns the last assigned order ID"""
        return Order.last_order_id

    @classmethod
    def create_new_order(cls):
        """Increments and returns a new order ID"""
        cls.last_order_id += 1
        return cls.last_order_id

# Using static method to check last order ID
print(Order.get_last_order_id())  # Output: 1000

# Creating new orders (using class method)
print(Order.create_new_order())  # Output: 1001
print(Order.create_new_order())  # Output: 1002

# Checking last order ID again
print(Order.get_last_order_id())  # Output: 1002


🔹 get_last_order_id() only reads last_order_id.
🔹 create_new_order() modifies last_order_id (hence, it's a class method).


Example 4: Game Scoreboard (Leaderboard)
🔹 A game where a static leaderboard tracks the highest scores.
🔹 @staticmethod is used to retrieve leaderboard data.


class Game:
    leaderboard = {"Alice": 100, "Bob": 90}  # Static variable

    @staticmethod
    def get_leaderboard():
        """Returns the leaderboard"""
        return Game.leaderboard

# Fetching leaderboard using static method
print(Game.get_leaderboard())  # Output: {'Alice': 100, 'Bob': 90}

# Directly modifying static variable
Game.leaderboard["Charlie"] = 95
print(Game.get_leaderboard())  # Output: {'Alice': 100, 'Bob': 90, 'Charlie': 95}



🔹 get_leaderboard() only retrieves data, modification happens outside the static method.



Example 5: E-commerce Discount System
🔹 A class where static variables store discount percentages.
🔹 @staticmethod is used to fetch discount without modifying it.



class Discount:
    discount_rate = 10  # Static variable (10% discount)

    @staticmethod
    def get_discount_rate():
        """Returns the current discount rate"""
        return f"Current discount: {Discount.discount_rate}%"

# Retrieving discount rate
print(Discount.get_discount_rate())  # Output: Current discount: 10%

# Modifying static variable (outside static method)
Discount.discount_rate = 15
print(Discount.get_discount_rate())  # Output: Current discount: 15%




🔹 get_discount_rate() reads the discount rate but does not modify it.

Key Takeaways
✅ Use @staticmethod when a method does not modify the static variable.
✅ Use @classmethod when a method needs to modify static variables.
✅ Use static variables for shared state among all instances.



Real-World Example: Car Rental System using Static Methods and Static Variables 🚗💨
🔹 Scenario: A car rental service tracks available cars and allows customers to rent them.
🔹 Static Variables:

total_cars → The total number of cars available.
rented_cars → The number of currently rented cars.
🔹 Static Method:
can_rent() → Checks if a car is available for rent (does not modify instance attributes).



Implementation:


class CarRental:
    total_cars = 10  # Static variable (total fleet)
    rented_cars = 0  # Static variable (cars currently rented)

    def __init__(self, customer_name):
        self.customer_name = customer_name  # Instance attribute

    @staticmethod
    def can_rent():
        """Checks if a car is available for rent."""
        return CarRental.rented_cars < CarRental.total_cars

    def rent_car(self):
        """Rents a car if available and updates the static variable."""
        if CarRental.can_rent():
            CarRental.rented_cars += 1
            print(f"{self.customer_name} rented a car. Cars left: {CarRental.total_cars - CarRental.rented_cars}")
        else:
            print("No cars available for rent.")

    def return_car(self):
        """Returns a rented car and updates the static variable."""
        if CarRental.rented_cars > 0:
            CarRental.rented_cars -= 1
            print(f"{self.customer_name} returned a car. Cars left: {CarRental.total_cars - CarRental.rented_cars}")
        else:
            print("No cars to return.")

# Customers renting cars
customer1 = CarRental("Alice")
customer2 = CarRental("Bob")

customer1.rent_car()  # Alice rents a car
customer2.rent_car()  # Bob rents a car
print(CarRental.can_rent())  # Checks if more cars are available

customer1.return_car()  # Alice returns a car
print(CarRental.can_rent())  # Checks again


How It Works:
Static Variables (total_cars, rented_cars) → Keep track of available/rented cars.
Static Method (can_rent()) → Checks availability without modifying attributes.
Instance Methods (rent_car(), return_car()) → Modify static variables when renting/returning.

📌 Output Example:
Alice rented a car. Cars left: 9
Bob rented a car. Cars left: 8
True
Alice returned a car. Cars left: 9
True

Why Use Static Methods and Static Variables Here?
✅ @staticmethod ensures availability checks are independent of instances (no self needed).
✅ Static variables allow tracking across all instances (shared state for all customers).
✅ Encapsulation → Business logic (rental rules) remains inside the class.



Example 3: Product Discount Calculation (Static Method with Instance Attributes)
🔹 Each Product has a name and price (instance attributes).
🔹 A @staticmethod applies a static discount rate to compute the final price.


class Product:
    discount_rate = 0.2  # Static variable (20% discount)

    def __init__(self, name, price):
        self.name = name  # Instance attribute
        self.price = price  # Instance attribute

    @staticmethod
    def apply_discount(product):
        """Applies discount to the product price"""
        return product.price - (product.price * Product.discount_rate)

# Creating product instances
p1 = Product("Laptop", 1000)
p2 = Product("Phone", 800)

# Using static method to apply discount
print(f"{p1.name} Final Price: ${Product.apply_discount(p1)}")  # Output: $800.0
print(f"{p2.name} Final Price: ${Product.apply_discount(p2)}")  # Output: $640.0



🔹 The static method does not modify the instance but calculates a result based on instance attributes.

Key Takeaways
✅ @staticmethod cannot use self but can work with instance attributes if passed explicitly.
✅ Use static methods when the logic is independent of instance behavior but still needs instance data.
✅ This technique helps encapsulate business logic inside the class while keeping the method independent.


2. @classmethod (Class Method)
Receives cls as the first argument (not self).
Can modify class-level attributes but not instance attributes.
Used when a method needs to work at the class level.


Example:

class Person:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Person.count += 1  # Modify class variable

    @classmethod
    def get_count(cls):
        return cls.count  # Access class variable

print(Person.get_count())  # Output: 0
p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())  # Output: 2


🔹 Uses cls, so it can modify class attributes.


Key Differences
Feature	@staticmethod	@classmethod
First Argument	No self or cls	cls (class reference)
Access Instance Attributes?	❌ No	❌ No
Access Class Attributes?	❌ No	✅ Yes
Used For	Independent utility functions inside a class	Class-level operations

When to Use?
✅ Use @staticmethod for helper functions that don’t depend on class attributes.
✅ Use @classmethod to modify or interact with class variables.



Real-World Example: E-Commerce Order Management Using Static Methods, Class Methods, and Class Variables 🛒📦

Scenario:
🔹 A company manages online orders with:

Class Variable (company_name) → Shared across all orders.
Static Variables (total_orders, total_revenue) → Track global order stats.
Static Method (order_stats()) → Displays global order statistics.
Class Method (update_company_name()) → Updates the company's name for all orders.
Instance Attributes (customer_name, order_amount) → Order details for individual customers.

Implementation:

class Order:
    company_name = "ShopEase"  # Class variable (shared by all instances)
    
    total_orders = 0  # Static variable (tracks total orders)
    total_revenue = 0  # Static variable (tracks total revenue)

    def __init__(self, customer_name, order_amount):
        self.customer_name = customer_name  # Instance attribute
        self.order_amount = order_amount  # Instance attribute
        Order.total_orders += 1  # Increment total orders
        Order.total_revenue += order_amount  # Add order amount to total revenue

    def process_order(self):
        """Instance method to process an order"""
        print(f"Order processed for {self.customer_name} - Amount: ${self.order_amount}")

    @staticmethod
    def order_stats():
        """Static method to display order statistics"""
        print(f"Total Orders: {Order.total_orders}")
        print(f"Total Revenue: ${Order.total_revenue}")

    @classmethod
    def update_company_name(cls, new_name):
        """Class method to update the company name for all orders"""
        cls.company_name = new_name
        print(f"Company name updated to: {cls.company_name}")

# Creating orders
order1 = Order("Alice", 250)
order2 = Order("Bob", 400)

# Processing orders
order1.process_order()
order2.process_order()

# Displaying order statistics
Order.order_stats()

# Updating company name using class method
Order.update_company_name("QuickShop")

# Checking updated company name
print(f"Order1 Company: {order1.company_name}")
print(f"Order2 Company: {order2.company_name}")


How It Works:
Class Variable (company_name) → Shared across all instances.
Static Variables (total_orders, total_revenue) → Track company-wide order stats.
Static Method (order_stats()) → Provides order statistics without modifying instance attributes.
Class Method (update_company_name()) → Modifies the class variable for all orders.
Instance Method (process_order()) → Handles individual order processing.
📌 Example Output:
    
 
 Order processed for Alice - Amount: $250
Order processed for Bob - Amount: $400
Total Orders: 2
Total Revenue: $650
Company name updated to: QuickShop
Order1 Company: QuickShop
Order2 Company: QuickShop


Key Takeaways:
✅ Class Methods (@classmethod) modify class variables across all instances.
✅ Static Methods (@staticmethod) operate independently of instance attributes.
✅ Class Variables (company_name) remain consistent across all instances unless updated via @classmethod.
✅ Static Variables (total_orders, total_revenue) track company-wide data, updated by instances.


No, you don't need to create an object of a class to call a @classmethod or @staticmethod.
Both class methods (@classmethod) and static methods (@staticmethod) can be called directly using the class name.


1️⃣ Calling a classmethod Without Creating an Object

class Demo:
    class_var = "Initial Value"

    @classmethod
    def update_class_var(cls, new_value):
        cls.class_var = new_value
        print(f"Updated class_var: {cls.class_var}")

# Calling class method directly using the class name (No object needed)
Demo.update_class_var("New Value")  

# Output:
# Updated class_var: New Value



✅ No object (Demo()) was created, yet update_class_var() was called successfully.

2️⃣ Calling a staticmethod Without Creating an Object


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling static method directly using the class name
result = MathUtils.add(5, 10)  
print(result)  

# Output:
# 15


✅ No object (MathUtils()) was created, yet add() was called successfully.


🔍 When Do You Need an Object?
Instance Methods (self required) → Need an object to access instance attributes.
Class Methods (cls required) → Can be called using either the class or an object.
Static Methods (No self or cls) → Can be called using either the class or an object.



Example Comparing All Three Methods

class Example:
    class_var = "Shared Value"

    def __init__(self, value):
        self.instance_var = value

    def instance_method(self):  
        print(f"Instance Method: {self.instance_var}")  # Needs self

    @classmethod
    def class_method(cls):  
        print(f"Class Method: {cls.class_var}")  # Uses cls

    @staticmethod
    def static_method():  
        print("Static Method: No self or cls required")

# Calling methods
obj = Example("Instance Value")

obj.instance_method()  # ✅ Needs an object
Example.class_method()  # ✅ No object needed
Example.static_method()  # ✅ No object needed



✅ Instance Method Requires an Object
✅ Class Method and Static Method Do Not Require an Object


📌 Key Takeaways
✅ Instance Methods (self) → Require an object (obj.method()).
✅ Class Methods (@classmethod) → Can be called with both class and object.
✅ Static Methods (@staticmethod) → Can be called with both class and object but don't modify class or instance attribute

q12) What is a Python decorator? Provide an example.
What is a Python Decorator?
A decorator in Python is a higher-order function that allows you to modify or enhance the behavior of another function without changing its actual code.

💡 Key Features:
✅ Used to add functionality to existing functions or methods.
✅ Implemented using the @decorator_name syntax.
✅ Functions in Python are first-class objects, which means they can be passed as arguments to other functions.

Basic Example of a Decorator
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()  # Call the original function
        print("After function execution")
    return wrapper

@my_decorator  # Applying the decorator
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()


🔹 Output:

Before function execution
Hello, World!
After function execution


Explanation:
my_decorator(func) is a decorator that wraps the function with additional functionality.
@my_decorator applies the decorator to say_hello().
When say_hello() is called, it runs inside wrapper(), adding extra behavior before and after the function execution.


Real-World Example: Logging Function Calls

import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # Execute the original function
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper

@log_time
def compute_square(n):
    time.sleep(1)  # Simulating a delay
    return n * n

print(compute_square(5))


🔹 Output:
Function 'compute_square' executed in 1.0002 seconds
25

Key Takeaways:
✅ Decorators are used for cross-cutting concerns like logging, authentication, timing, and caching.
✅ They work without modifying the original function's logic.
✅ Can take arguments (*args, **kwargs) to handle different function signatures.

Parameterized Decorator in Python
If you want a decorator to accept parameters, you need to add an extra layer of function nesting. This allows passing arguments to the decorator itself.

Example: Custom Logging Level in a Decorator
Here, we modify the @log_time decorator to accept a log level (e.g., "INFO", "DEBUG", "WARNING").

import time

def log_time(level="INFO"):  # Outer function takes a parameter
    def decorator(func):  # Actual decorator
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)  # Execute the original function
            end = time.time()
            print(f"[{level}] Function '{func.__name__}' executed in {end - start:.4f} seconds")
            return result
        return wrapper
    return decorator  # Return the decorator function

# Applying the decorator with a parameter
@log_time(level="DEBUG")
def compute_square(n):
    time.sleep(1)  # Simulating delay
    return n * n

print(compute_square(5))


🔹 Output:
 [DEBUG] Function 'compute_square' executed in 1.0002 seconds
25


How It Works:
1️⃣ log_time(level) → Accepts an argument (level).
2️⃣ Returns decorator(func) → Standard decorator structure.
3️⃣ Inside decorator(func), we return wrapper() which wraps the original function.
4️⃣ @log_time(level="DEBUG") → Calls log_time("DEBUG"), which returns decorator.
5️⃣ When compute_square(5) runs, wrapper() executes with the extra logging behavior.

📌 Key Takeaways for Parameterized Decorators
✅ Use three nested functions (decorator with args → actual decorator → wrapper).
✅ The outer function receives the decorator parameter (level).
✅ The middle function decorates the target function (func).
✅ The inner function (wrapper) wraps and modifies function behavior.


Real-World Use Case: Authentication with a Decorator
Let’s create a decorator for authentication that checks if a user has the required role before allowing access to a function.


Example: Role-Based Access Control (RBAC) Decorator

def requires_role(required_role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                print(f"Access Denied: '{user_role}' role cannot access this function.")
                return None
            print(f"Access Granted: '{user_role}' role allowed.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Applying the decorator with a required role
@requires_role("admin")
def delete_user(user_id):
    print(f"User {user_id} has been deleted.")

# Testing with different roles
delete_user("admin", 101)  # ✅ Access granted
delete_user("guest", 102)  # ❌ Access denied


🔹 Output:
 Access Granted: 'admin' role allowed.
User 101 has been deleted.

Access Denied: 'guest' role cannot access this function.


🚀 How It Works:
1️⃣ requires_role(required_role) → Takes a role as a parameter.
2️⃣ Returns decorator(func), which acts as the actual decorator.
3️⃣ Inside wrapper(), we check if the user's role matches required_role:

✅ If it matches, the function executes.
❌ If it doesn’t match, access is denied.
4️⃣ Applying @requires_role("admin") → Restricts access to only users with the "admin" role.
5️⃣ Calling delete_user("guest", 102) → Access is denied because "guest" is not "admin".
🔹 Where Is This Used in Real Applications?
✅ Django & Flask Authentication – Restricting API endpoints based on user roles.
✅ Admin Panel Restrictions – Ensuring only authorized users can modify settings.
✅ Logging & Auditing – Adding access logs for sensitive operations.

Class-Based Decorator in Python
A class-based decorator allows state persistence and more structured logic than function-based decorators.
 Instead of using nested functions, we use a class with the __call__ method.
 
 
 🔹 Example 1: Logging Decorator (Class-Based)
Here’s how you can implement a class-based decorator to log function execution time.

import time

class LogTime:
    def __init__(self, level="INFO"):  # Accepts parameters like a function decorator
        self.level = level  # Stores state (e.g., log level)

    def __call__(self, func):  # Makes the class instance callable
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"[{self.level}] Function '{func.__name__}' executed in {end - start:.4f} seconds")
            return result
        return wrapper  # Returns the modified function

# Applying the class-based decorator
@LogTime(level="DEBUG")
def compute_square(n):
    time.sleep(1)  # Simulating delay
    return n * n

print(compute_square(5))



🔹 Output:
    
 [DEBUG] Function 'compute_square' executed in 1.0002 seconds
25

🚀 How It Works
1️⃣ __init__(self, level) → Accepts decorator parameters (level).
2️⃣ __call__(self, func) → Makes the class behave like a function decorator.
3️⃣ The wrapper function executes before and after func runs, adding logging.
4️⃣ When we do @LogTime(level="DEBUG"), Python executes:

compute_square = LogTime(level="DEBUG")(compute_square)

Which translates to:
    
compute_square = wrapper  # The function is replaced by wrapper


5️⃣ Now compute_square(5) actually runs wrapper(5).


🔹 Example 2: Role-Based Access Control (RBAC) Using Class-Based Decorator

This example checks whether a user has the required role before executing a function.

class RequiresRole:
    def __init__(self, required_role):
        self.required_role = required_role  # Stores required role
    
    def __call__(self, func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != self.required_role:
                print(f"Access Denied: '{user_role}' role cannot access this function.")
                return None
            print(f"Access Granted: '{user_role}' role allowed.")
            return func(*args, **kwargs)
        return wrapper

# Applying the class-based decorator
@RequiresRole("admin")
def delete_user(user_id):
    print(f"User {user_id} has been deleted.")

# Testing with different roles
delete_user("admin", 101)  # ✅ Access granted
delete_user("guest", 102)  # ❌ Access denied


🔹 Output:
Access Granted: 'admin' role allowed.
User 101 has been deleted.

Access Denied: 'guest' role cannot access this function.

🔹 Key Benefits of Class-Based Decorators
✅ State Persistence: Unlike function-based decorators, class-based decorators can maintain state across multiple function calls.
✅ Flexibility: Easier to extend and modify (e.g., add logging, different behaviors).
✅ Better Readability: More structured than deeply nested function decorators.


🔹 Class-Based Caching (Memoization) Decorator in Python

A caching (memoization) decorator stores the results of expensive function calls and returns the cached 
result when the same inputs occur again. This is useful for improving performance in recursive functions or computationally heavy operations.

🔹 Example: Fibonacci with Memoization using a Class-Based Decorator

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}  # Dictionary to store computed results

    def __call__(self, *args):
        if args in self.cache:  # Check if result exists in cache
            print(f"Fetching from cache: {args} → {self.cache[args]}")
            return self.cache[args]
        
        print(f"Computing result for: {args}")
        result = self.func(*args)  # Compute the result
        self.cache[args] = result  # Store in cache
        return result

# Applying the memoization decorator
@Memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the memoized Fibonacci function
print(fibonacci(10))

🔹 Output (Demonstrating Caching)

Computing result for: (10,)
Computing result for: (9,)
Computing result for: (8,)
Computing result for: (7,)
Computing result for: (6,)
Computing result for: (5,)
Computing result for: (4,)
Computing result for: (3,)
Computing result for: (2,)
Computing result for: (1,)
Computing result for: (0,)
Fetching from cache: (1,) → 1
Fetching from cache: (2,) → 1
Fetching from cache: (3,) → 2
Fetching from cache: (4,) → 3
Fetching from cache: (5,) → 5
Fetching from cache: (6,) → 8
Fetching from cache: (7,) → 13
Fetching from cache: (8,) → 21
Fetching from cache: (9,) → 34
55


🔹 Example: TTL-Based Caching Decorator

import time

class TTLCache:
    def __init__(self, ttl=5):  # Default TTL is 5 seconds
        self.ttl = ttl
        self.cache = {}  # Stores cached results
        self.timestamps = {}  # Stores cache timestamps

    def __call__(self, func):
        def wrapper(*args):
            current_time = time.time()

            # Check if result exists and has not expired
            if args in self.cache and (current_time - self.timestamps[args]) < self.ttl:
                print(f"Fetching from cache: {args} → {self.cache[args]}")
                return self.cache[args]

            # Compute and cache the result
            print(f"Computing result for: {args}")
            result = func(*args)
            self.cache[args] = result
            self.timestamps[args] = current_time  # Store current time
            return result

        return wrapper

# Applying the TTLCache decorator
@TTLCache(ttl=10)  # Cache expires after 10 seconds
def expensive_function(x):
    time.sleep(2)  # Simulating a slow computation
    return x * x

# Testing the TTL caching function
print(expensive_function(5))  # Computes and stores in cache
print(expensive_function(5))  # Fetches from cache
time.sleep(11)  # Wait for TTL to expire
print(expensive_function(5))  # Recomputes since cache expired



🔹 Output

Computing result for: (5,)
25
Fetching from cache: (5,) → 25
25
Computing result for: (5,)
25



A function-based decorator uses nested functions to add caching functionality to Fibonacci calculations.

from functools import wraps

def memoize(func):
    cache = {}  # Dictionary to store computed results
    
    @wraps(func)  # Preserves function metadata
    def wrapper(n):
        if n in cache:  # Check if result exists in cache
            print(f"Fetching from cache: {n} → {cache[n]}")
            return cache[n]

        print(f"Computing result for: {n}")
        result = func(n)  # Compute the Fibonacci number
        cache[n] = result  # Store result in cache
        return result
    
    return wrapper  # Returns the decorated function

# Applying the memoization decorator
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the memoized Fibonacci function
print(fibonacci(10))


out:
Computing result for: 10
Computing result for: 9
Computing result for: 8
Computing result for: 7
Computing result for: 6
Computing result for: 5
Computing result for: 4
Computing result for: 3
Computing result for: 2
Computing result for: 1
Computing result for: 0
Fetching from cache: 1 → 1
Fetching from cache: 2 → 1
Fetching from cache: 3 → 2
Fetching from cache: 4 → 3
Fetching from cache: 5 → 5
Fetching from cache: 6 → 8
Fetching from cache: 7 → 13
Fetching from cache: 8 → 21
Fetching from cache: 9 → 34
55

q13)
 Difference Between Generator and Iterator in Python
 
 Feature	                           Iterator	                                                                   Generator
Definition	                         An object that implements __iter__() and __next__() methods	   A function that yields values instead of returning them
How It’s Created?	         Defined using a class that implements __iter__() and __next__()	        Defined using a function with yield
Memory Efficiency	          Stores all values in memory	                                       Generates values on demand (lazy evaluation)
State Retention	              Does not maintain state internally	                                     Maintains state automatically between yield calls
Usage	                            Need to manually implement iteration logic	                    Uses yield, making it simpler and more readable
Performance	                            May require more memory for large datasets	                More memory-efficient for large datasets

🔹 Example of an Iterator
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self  # Iterator must return itself

    def __next__(self):
        if self.count < self.limit:
            value = self.count
            self.count += 1
            return value
        else:
            raise StopIteration  # End of iteration

# Using the iterator
obj = MyIterator(5)
for num in obj:
    print(num)


🔹 Output:
 
 0
1
2
3
4


🔹 Explanation:

Implements __iter__() → Returns self
Implements __next__() → Increments count, stops when limit is reached
Manually handles iteration logic


🔹 Example of a Generator

def my_generator(limit):
    count = 0
    while count < limit:
        yield count  # Yield instead of return
        count += 1

# Using the generator
for num in my_generator(5):
    print(num)


🔹 Output:
 0
1
2
3
4

🔹 Explanation:

Uses yield → Automatically remembers state
No need for __iter__() or __next__()
More concise and memory-efficient

🔹 Key Takeaways
✅ Use Iterators when you need more control over the iteration process.
✅ Use Generators when dealing with large datasets to save memory.


Scenario:
Imagine you need to process a 10GB log file. Loading the entire file into memory with an iterator would be inefficient.
 Instead, a generator can process it line-by-line without consuming excessive memory.
 
 🔹 Using an Iterator (Memory-Heavy)
 
 class FileIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')  # Open file
        self.lines = self.file.readlines()  # Loads ALL lines into memory
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lines):
            self.file.close()
            raise StopIteration
        line = self.lines[self.index]
        self.index += 1
        return line

# Using the iterator (Consumes high memory for large files)
for line in FileIterator("large_log.txt"):
    print(line.strip())  # Processing each line


🔹 Problem: readlines() loads the entire file into memory, causing high memory usage for large files.

🔹 Using a Generator (Memory-Efficient)
def file_generator(filename):
    with open(filename, 'r') as file:  # Open file
        for line in file:  # Reads line-by-line
            yield line.strip()  # Yield instead of return

# Using the generator (Consumes very little memory)
for line in file_generator("large_log.txt"):
    print(line)  # Processing each line

🔹 Advantage: Only one line is kept in memory at a time, making it suitable for very large files.

🔹 Why Generators Are Better Here?

Feature	Iterator (Memory-Heavy)	Generator (Memory-Efficient)
Memory Usage	Loads entire file into memory	Loads one line at a time
Performance	Slow for large files	Fast & scalable
Best for	Small to medium datasets	Large datasets, streaming


🔹 Key Takeaways
✅ Use Iterators when you need random access or repeated iteration over data.
✅ Use Generators for large data processing (e.g., reading big files, streaming APIs, or real-time data).


Why Do We Need Iterators & Generators When range() Exists?

The built-in range() function generates a sequence of numbers on demand without storing them in memory. 
However, it only works for numerical sequences and lacks flexibility for handling real-world streaming data, large files, or infinite sequences.

🔹 When range() Is Enough

for num in range(1, 5):
    print(num)


1
2
3
4

✅ Efficient for small integer sequences.
❌ Cannot handle real-time data streams, large files, or non-numeric sequences.

🔹 When Iterators & Generators Are Necessary?
1️⃣ Processing Large Files Without Loading Them Into Memory
🚀 Use Case: Suppose you have a 10GB log file. You can’t use range() to process its lines because range() only handles numbers. Instead, a generator processes it line by line.


def read_large_file(filename):
    """Reads a large file line by line using a generator."""
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()  # Yielding each line without storing in memory

# Process the file efficiently
for line in read_large_file("huge_log.txt"):
    print(line)


✅ Does not load the entire file into memory
✅ Can handle massive files efficiently

2️⃣ Generating Infinite Sequences (e.g., Fibonacci)
🚀 Use Case: range() requires a start and stop, but what if we need an infinite sequence?
A generator creates numbers on demand without defining an end.

def fibonacci():
    """Generates an infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # Fibonacci logic

# Printing the first 10 Fibonacci numbers
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))

✅ Does not store all numbers in memory
✅ Works for infinite sequences (range() has an upper limit)


✅ Does not store all numbers in memory
✅ Works for infinite sequences (range() has an upper limit)

import random
import time

def temperature_sensor():
    """Simulates real-time temperature sensor readings."""
    while True:
        yield f"Temperature: {random.uniform(20, 35):.2f}°C"
        time.sleep(2)  # Simulating delay

# Continuously process live sensor data
for temp in temperature_sensor():
    print(temp)


✅ Processes data as it arrives
✅ Efficient for IoT & streaming applications


🔹 Key Takeaways
Feature	range() (Numbers Only)	Iterator/Generator (Flexible)
Memory Usage	✅ Efficient (stores only start, stop, step)	✅ Efficient (lazy evaluation, doesn’t store values)
Handles Large Data?	❌ No	✅ Yes (Large files, APIs, logs, etc.)
Handles Infinite Sequences?	❌ No	✅ Yes (Fibonacci, streaming data, etc.)
Handles Real-Time Data?	❌ No	✅ Yes (Live stock prices, IoT sensors, etc.)
Handles Non-Numeric Data?	❌ No	✅ Yes (Strings, files, objects, etc.)
📌 Use range() for simple numeric sequences.
📌 Use generators for memory-efficient processing, large data, and real-time streaming.

q14)Explain the Global Interpreter Lock (GIL) in Python.


🔹 What is the Global Interpreter Lock (GIL) in Python?
The Global Interpreter Lock (GIL) is a mutex (lock) that allows only one thread to execute Python bytecode at a time, even on multi-core processors.

🛑 Key Limitation:

Even if you create multiple threads, the GIL ensures only one thread runs at a time, making CPU-bound tasks inefficient in multi-threading.
✅ However, GIL does not affect multi-processing.


🔹 Why Does Python Have a GIL?
Python’s memory management uses automatic garbage collection (reference counting). The GIL ensures:

Thread-Safe Memory Management – Prevents race conditions when multiple threads modify objects.
Simplicity – Python’s interpreter remains simple and easy to implement.


🔹 When is GIL a Problem?
🔴 GIL is a performance bottleneck for CPU-bound tasks (tasks that need intensive computation).

Example: Image processing, matrix computations, number crunching, cryptography.


🔹 Example: Python Threads vs. Processes
(1) Using Threads (GIL Blocks CPU Efficiency)

import threading
import time

def cpu_task():
    print("Starting task...")
    for _ in range(10**7):
        _ = _ * 2  # CPU-intensive task
    print("Task completed.")

# Run two threads
start_time = time.time()
t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Time taken: {time.time() - start_time:.2f} sec")


❌ Even with two threads, execution is not twice as fast due to GIL blocking CPU-bound tasks.

(2) Using Multiprocessing (Bypassing GIL)

import multiprocessing
import time

def cpu_task():
    print("Starting task...")
    for _ in range(10**7):
        _ = _ * 2  # CPU-intensive task
    print("Task completed.")

# Run two processes
start_time = time.time()
p1 = multiprocessing.Process(target=cpu_task)
p2 = multiprocessing.Process(target=cpu_task)
p1.start()
p2.start()
p1.join()
p2.join()
print(f"Time taken: {time.time() - start_time:.2f} sec")

✅ Here, Python creates separate processes, bypassing the GIL, leading to better CPU utilization.

🔹 When GIL is NOT a Problem?
✅ I/O-Bound Tasks (Waiting for External Resources)

File I/O, Network Requests, Database Queries benefit from threading, as they don’t need CPU all the time.

import threading
import time

def io_task():
    print("Downloading file...")
    time.sleep(3)  # Simulate waiting for network
    print("Download complete.")

# Using multiple threads for I/O tasks
start_time = time.time()
t1 = threading.Thread(target=io_task)
t2 = threading.Thread(target=io_task)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Time taken: {time.time() - start_time:.2f} sec")


✅ Threads work efficiently here because GIL releases the lock during I/O wait times.


🔹 How to Overcome GIL for CPU-Intensive Tasks?
Use multiprocessing instead of threading
Each process runs in a separate memory space, bypassing GIL.
Use JIT Compilers like PyPy
PyPy reduces GIL impact by optimizing execution.
Use Python Libraries Written in C
NumPy, Pandas, TensorFlow use C extensions that release the GIL during execution.
Use Cython (nogil mode)
Allows Python code to run without GIL by compiling to C.

🔹 Key Takeaways
✅ GIL ensures thread safety but limits true parallel execution in multi-threading.
✅ For CPU-bound tasks (like image processing, ML, cryptography), use multiprocessing.
✅ For I/O-bound tasks (like web scraping, database access), threading works well.
✅ Libraries like NumPy and TensorFlow optimize performance by releasing GIL.

q15)How does Python’s with statement work?

🔹 How Does Python’s with Statement Work?

The with statement in Python is used for resource management and exception handling. 
It ensures that resources (like files, sockets, database connections) are properly cleaned up after use, even if an error occurs.

✅ Automatically closes resources
✅ Reduces the risk of resource leaks
✅ Makes code cleaner and more readable

🔹 Example: Opening a File Without with (Risky)

file = open("example.txt", "r")
content = file.read()
file.close()  # Must manually close the file


❌ Problem: If an exception occurs before file.close(), the file remains open, causing resource leaks.

🔹 Example: Using with (Best Practice)

with open("example.txt", "r") as file:
    content = file.read()

✅ No need to manually call file.close()—it’s automatically closed when the block ends.


🔹 How with Works Internally? (__enter__ and __exit__)
The with statement relies on the context manager protocol, which includes:

__enter__() → Runs at the start of the block
__exit__() → Runs when the block exits (even if an error occurs)


Example: Custom Context Manager

class CustomFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file  # This value is assigned to `as file`

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()  # Ensures cleanup even if an error occurs

# Using the custom context manager
with CustomFile("example.txt", "r") as file:
    content = file.read()


✅ Ensures proper resource management
✅ Handles exceptions gracefully


🔹 Other Use Cases of with
1️⃣ Managing Database Connections


import sqlite3

with sqlite3.connect("mydb.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")

✅ Ensures database connection is closed properly.



2️⃣ Handling Locks in Multithreading

import threading

lock = threading.Lock()

with lock:  # Ensures lock is released after use
    print("Thread-safe operation")


✅ Ensures locks are released safely in multithreading.


3️⃣ Temporary Directory (Auto Cleanup)

import tempfile

with tempfile.TemporaryFile(mode="w+") as temp:
    temp.write("Temporary data")
    temp.seek(0)
    print(temp.read())  # Reads back the data


✅ Automatically deletes the temp file after use.

🔹 Key Takeaways
✅ Ensures proper resource cleanup (files, database connections, locks)
✅ Prevents resource leaks, even if an exception occurs
✅ Uses the context manager protocol (__enter__() & __exit__())


Note: q16)What are metaclasses in Python?


🔹 What is a Metaclass in Python?
A metaclass is a class that defines how other classes are created.
While a class defines objects, a metaclass defines classes.

🔹 Understanding Metaclasses
Classes create objects.
Metaclasses create classes.
By default, Python’s metaclass is type, meaning all classes in Python are instances of type.

class MyClass:
    pass

print(type(MyClass))  # ✅ Output: <class 'type'>

Here, MyClass is an instance of type, meaning type is its metaclass.


🔹 Creating a Custom Metaclass
A metaclass is simply a class that inherits from type

# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

# Define a class using this metaclass
class MyClass(metaclass=MyMeta):
    pass



✔ When MyClass is created, MyMeta.__new__() is executed before MyClass exists.


🔹 Why Use Metaclasses?
1️⃣ Modify class attributes before the class is created
2️⃣ Automatically add methods or properties
3️⃣ Enforce rules on class definitions (e.g., requiring certain methods)
4️⃣ Implement design patterns (like Singletons)

Would you like a real-world example, such as metaclasses in ORMs (like Django)?



🔹 All classes using this metaclass must have a save() method (useful for ORM models).




✅ Example: Enforcing a save() Method in ORM-like Classes
# Define a metaclass that enforces a rule
class RequireSaveMeta(type):
    def __new__(cls, name, bases, dct):
        if "save" not in dct:
            raise TypeError(f"Class '{name}' must define a 'save()' method")
        return super().__new__(cls, name, bases, dct)

# Correct class (✅ Works fine)
class UserModel(metaclass=RequireSaveMeta):
    def save(self):
        print("Saving user data to the database")

# Incorrect class (❌ Raises an error)
class ProductModel(metaclass=RequireSaveMeta):
    pass  # ❌ No 'save()' method → Raises TypeError

# ✅ Creating an instance of UserModel works fine
user = UserModel()
user.save()

# ❌ Uncommenting the following line will raise an error
# product = ProductModel()  # TypeError: Class 'ProductModel' must define a 'save()' method

🔹 How This Works
✔ The metaclass (RequireSaveMeta) checks if save() is in the class definition.
✔ If missing, it raises a TypeError, preventing the class from being created.
✔ This ensures all models follow the same structure, making them consistent and maintainable.


🔹 Where Are Metaclasses Used in the Real World?
1️⃣ Django ORM: Django models use metaclasses to define database tables dynamically.
2️⃣ Logging Frameworks: Metaclasses auto-wrap methods for logging (e.g., API calls).
3️⃣ Security Systems: Enforce role-based access control dynamically.
 



q17) 🔹 Difference Between __new__ and __init__ in Python Classes

Both __new__ and __init__ are special methods used during object creation, but they serve different purposes.


Method	When It Runs	Purpose
__new__	Before an object is created	Creates and returns a new instance of the class.
__init__	After an object is created	Initializes the object with data.


1️⃣ __new__ – Responsible for Object Creation
It is a static method.
It is called before the object is created.
It must return an instance of the class (cls).
Used in metaclasses and singleton patterns.



2️⃣ __init__ – Responsible for Initialization
It is an instance method.
It is called after the object is created.
It initializes instance attributes but doesn’t return anything (None).


🔹 Example: Understanding __new__ and __init__

class MyClass:
    def __new__(cls, *args, **kwargs):
        print("__new__ method is called")
        instance = super().__new__(cls)
        return instance  # Must return an instance

    def __init__(self, value):
        print("__init__ method is called")
        self.value = value

# Creating an object
obj = MyClass(10)

✅ Output:
    
__new__ method is called
__init__ method is called


🚀 Flow Explanation:
1️⃣ __new__() is called first → Creates the object.
2️⃣ __init__() is called next → Initializes the object.


🔹 When Do We Use __new__()?


✅ 1️⃣ Singleton Pattern (Ensuring Only One Instance)


class Singleton:
    _instance = None  # Stores the single instance
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

# Creating multiple objects
obj1 = Singleton(10)
obj2 = Singleton(20)

print(obj1 is obj2)  # ✅ True (Both are same instance)
print(obj1.value)    # ✅ 20 (Only one instance exists)

✔ Only one instance is created, even when called multiple times.



✅ 2️⃣ Controlling Immutable Types (e.g., tuple)

Since immutable objects (like tuple, str) can’t be modified, __new__() is used for modifications.

class MyTuple(tuple):
    def __new__(cls, values):
        return super().__new__(cls, map(abs, values))

t = MyTuple([-1, -2, -3])
print(t)  # ✅ (1, 2, 3)



✔ __new__() ensures tuples are always positive before creation.


🔹 Key Takeaways


Feature	__new__()	__init__()
When is it called?	Before object creation	After object creation
Return value	A new instance (cls)	Always None
Used for?	Controlling object creation	Initializing instance attributes
Required?	Only for special cases (e.g., Singleton, Immutable types)	Always runs in normal object creation



🔹 Metaclass Example Using __new__()
A metaclass defines how a class itself behaves. Using __new__() in a metaclass allows us to control how classes are created.


✅ Example: Automatically Adding Methods to a Class
We’ll use __new__() in a metaclass to automatically add a hello() method to any class that uses this metaclass.


# Define a custom metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")

        # Add a new method dynamically
        dct['hello'] = lambda self: f"Hello from {self.__class__.__name__}"

        return super().__new__(cls, name, bases, dct)

# Define a class using the custom metaclass
class MyClass(metaclass=MyMeta):
    pass

# Create an instance and call the dynamically added method
obj = MyClass()
print(obj.hello())  # ✅ Output: Hello from MyClass


✔ How it works:
1️⃣ __new__() runs when MyClass is created.
2️⃣ It adds the hello() method dynamically to MyClass.
3️⃣ Now, any instance of MyClass has hello() available.

✅ Example: Enforcing Naming Conventions with a Metaclass
Let’s use __new__() to ensure all class attributes are uppercase.

class UpperCaseMeta(type):
    def __new__(cls, name, bases, dct):
        for key in dct:
            if not key.isupper() and not key.startswith('__'):
                raise TypeError(f"Attribute '{key}' must be uppercase!")
        return super().__new__(cls, name, bases, dct)

# This class will work fine
class ValidClass(metaclass=UpperCaseMeta):
    VALUE = 10  # ✅ Allowed

# This will raise an error because 'value' is not uppercase
class InvalidClass(metaclass=UpperCaseMeta):
    value = 20  # ❌ Raises TypeError

✅ This ensures all class attributes are defined in uppercase.

🔹 When Should You Use __new__() in a Metaclass?
✔ Enforcing class structure (e.g., naming conventions).
✔ Dynamically modifying class behavior (e.g., adding methods automatically).
✔ Creating Singleton classes (ensuring only one instance of a class exists).
✔ Overriding class creation logic (e.g., preventing certain class creations).


q18)How do you implement method overloading and overriding in Python?
🔹 Method Overloading vs. Method Overriding in Python
Python does not support traditional method overloading (same method name, different parameters), but we can achieve it using default arguments or *args/**kwargs.
Method overriding, on the other hand, is fully supported using inheritance.

✅ 1. Method Overloading (Same Method Name, Different Parameters)
Python doesn’t support method overloading like Java or C++. However, we can achieve similar behavior using: ✔ Default arguments
✔ *args and **kwargs

Example 1: Using Default Arguments
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# ✅ Works with different argument counts
obj = MathOperations()
print(obj.add(5))        # Output: 5
print(obj.add(5, 10))    # Output: 15
print(obj.add(5, 10, 15)) # Output: 30

Example 2: Using *args for Dynamic Parameters
class MathOperations:
    def add(self, *args):
        return sum(args)

obj = MathOperations()
print(obj.add(5))           # Output: 5
print(obj.add(5, 10))       # Output: 15
print(obj.add(5, 10, 15))   # Output: 30

✔ Why use *args? It allows us to pass any number of arguments dynamically.

✅ 2. Method Overriding (Child Class Redefining Parent’s Method)
✔ Occurs when a subclass provides a specific implementation of a method already defined in its parent class.
✔ The child class method must have the same name and parameters as the parent method.

Example: Overriding in Inheritance
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class (Overridden Method)")

obj = Child()
obj.show()  # Output: This is Child class (Overridden Method)


✅ Calling Parent Method from Overridden Method (super())
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        super().show()  # Calls Parent's method
        print("Child class method")

obj = Child()
obj.show()

# Output:
# Parent class method
# Child class method

✔ Using super() ensures the parent method is executed before the child method.

🔹 Summary
Feature	Method Overloading	Method Overriding
Definition	Same method name, different parameters	Child class redefines parent method
Support in Python	❌ (Can be simulated using *args or default parameters)	✅ Fully supported
Use Case	Handle multiple argument types	Modify parent class behavior


✅ 1. Method Overloading in a Real-World API Scenario
Imagine we are designing an API client that allows sending requests with different parameters:

If only a URL is provided → perform a GET request.
If URL and data are provided → perform a POST request.
If URL, data, and headers are provided → perform a custom request.
Example: Overloading Using Default Arguments

class APIClient:
    def request(self, url, data=None, headers=None):
        if data is None:
            print(f"GET request sent to {url}")
        elif headers is None:
            print(f"POST request sent to {url} with data {data}")
        else:
            print(f"Custom request to {url} with data {data} and headers {headers}")

# ✅ Overloading behavior based on arguments
client = APIClient()
client.request("https://api.example.com")  
# Output: GET request sent to https://api.example.com

client.request("https://api.example.com", {"name": "John"})  
# Output: POST request sent to https://api.example.com with data {'name': 'John'}

client.request("https://api.example.com", {"name": "John"}, {"Auth": "Bearer token"})  
# Output: Custom request to https://api.example.com with data {'name': 'John'} and headers {'Auth': 'Bearer token'}


✔ No need to define multiple request() methods; we handle overloading with optional arguments.

✅ 2. Method Overriding in a Logging System
A real-world example of method overriding is a logging system, where:
✔ The base class provides a generic log() method.
✔ The subclass overrides it to add a timestamp.
Example: Overriding to Extend Functionality

from datetime import datetime

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")  # ✅ Overridden method

# ✅ Parent class behavior
logger = Logger()
logger.log("System started")  
# Output: [LOG] System started

# ✅ Child class behavior (Overridden method with timestamp)
timestamp_logger = TimestampLogger()
timestamp_logger.log("System started")  
# Output: [2025-02-19 14:30:00] System started

✔ The child class modifies the parent’s behavior by adding a timestamp.
✔ This is a common pattern in logging frameworks.


✅ 3. Overriding with super(): API Response Handling
Another real-world case is modifying an API response format:
✔ The base class retrieves data from an API.
✔ The child class processes the response before returning it.

Example: Overriding with super()

class APIClient:
    def get_data(self):
        return {"status": "success", "data": {"name": "John", "age": 30}}

class ProcessedAPIClient(APIClient):
    def get_data(self):
        raw_data = super().get_data()  # ✅ Call parent method
        return raw_data["data"]  # ✅ Process response before returning

# ✅ Using the base class
api_client = APIClient()
print(api_client.get_data())  
# Output: {'status': 'success', 'data': {'name': 'John', 'age': 30}}

# ✅ Using the overridden method
processed_client = ProcessedAPIClient()
print(processed_client.get_data())  
# Output: {'name': 'John', 'age': 30}

✔ The child class modifies the parent’s behavior to return only the relevant part of the response.

🔹 Summary
Feature	Real-World Example
Method Overloading	API client handling GET/POST/custom requests based on parameters
Method Overriding	Logging system where the child class adds a timestamp
Overriding with super()	API response processing in a child class



q19)How does Python’s asyncio library work?

🔹 Understanding Python’s asyncio Library (Asynchronous Programming)
Python’s asyncio library enables concurrent, asynchronous, and non-blocking programming. It is used for I/O-bound tasks like:
✔ Networking (HTTP requests, WebSockets)
✔ Database calls
✔ File I/O
✔ Async APIs (e.g., FastAPI, Aiohttp)

🔹 Key Concepts in asyncio

✅ 1. Event Loop
The core of asyncio, handling multiple tasks concurrently.
Runs async functions without blocking the main thread.
✅ 2. Coroutines (async functions)
Declared using async def
Must be awaited with await
✅ 3. Tasks (asyncio.create_task())
Runs coroutines concurrently.
✅ 4. Future & Awaitable
await is used to pause execution until a coroutine completes.


🔹 Example: Synchronous vs Asynchronous
📌 Synchronous Code (Blocking)

import time

def task(n):
    print(f"Task {n} started")
    time.sleep(3)  # Blocking call
    print(f"Task {n} completed")

def main():
    task(1)
    task(2)

main()



⏳ Output:
Task 1 started  
Task 1 completed  
Task 2 started  
Task 2 completed  

📌 Total Time Taken: 6s (Sequential Execution)

📌 Asynchronous Code (Non-Blocking)
Takes ~3 seconds because tasks run concurrently.

import asyncio

async def task(n):
    print(f"Task {n} started")
    await asyncio.sleep(3)  # ✅ Non-blocking
    print(f"Task {n} completed")

async def main():
    await asyncio.gather(task(1), task(2))  # ✅ Run concurrently

asyncio.run(main())  # ✅ Starts event loop


Task 1 started  
Task 2 started  
Task 1 completed  
Task 2 completed 

📌 Total Time Taken: ~3s (Concurrent Execution)


🔹 Using asyncio.create_task() for Parallel Execution


📌 Running Tasks in Background
async def task(n):
    print(f"Task {n} started")
    await asyncio.sleep(3)  # ✅ Non-blocking
    print(f"Task {n} completed")

async def main():
    t1 = asyncio.create_task(task(1))  # ✅ Task runs in background
    t2 = asyncio.create_task(task(2))
    await t1  # Wait for completion
    await t2

asyncio.run(main())

📌 Similar to gather(), but allows better control over tasks.

🔹 Real-World Example: Fetching URLs Concurrently
import asyncio
import aiohttp  # ✅ Async HTTP requests

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://example.com", "https://python.org"]
    tasks = [fetch_url(url) for url in urls]
    await asyncio.gather(*tasks)  # ✅ Run HTTP requests in parallel

asyncio.run(main())

📌 Optimized for I/O-bound operations like HTTP requests.

🔹 When to Use asyncio?
✅ Best for:
✔ High-performance web applications (FastAPI)
✔ Web scraping (aiohttp, Scrapy)
✔ Database interactions (asyncpg, Tortoise ORM)
✔ Network services (WebSockets, IoT)

❌ Not ideal for:
⛔ CPU-bound tasks (Use multiprocessing)
⛔ Simple scripts (No I/O operations)

q20)Explain the difference between @staticmethod, @classmethod, and instance methods.
🔹 Difference Between @staticmethod, @classmethod, and Instance Methods in Python
Python provides three types of methods in classes:
✔ Instance Methods (default)
✔ Class Methods (@classmethod)
✔ Static Methods (@staticmethod)

Each has a different purpose and behavior.

1️⃣ Instance Method (Default)
Defined without @staticmethod or @classmethod.
First parameter: self (instance reference).
Can modify object state (instance variables).
📌 Example

class Example:
    def __init__(self, value):
        self.value = value  # ✅ Instance variable

    def instance_method(self):  # ✅ Instance method
        return f"Instance Method: {self.value}"

obj = Example(42)
print(obj.instance_method())  # ✅ Call using an object


Instance Method: 42

🔹 Key Points:
✔ Can modify instance attributes (self.value).
✔ Needs an instance to be called (obj.instance_method()).

2️⃣ Class Method (@classmethod)
Defined using @classmethod.
First parameter: cls (class reference).
Can modify class variables (shared among all instances).
📌 Example


class Example:
    class_variable = "Hello"

    @classmethod
    def class_method(cls):
        return f"Class Method: {cls.class_variable}"

print(Example.class_method())  # ✅ Call using class


✅ Output:
 Class Method: Hello

🔹 Key Points:
✔ Accesses class variables (cls.class_variable).
✔ Can be called using class or instance (Example.class_method()).
✔ Cannot access instance variables (self.value).

3️⃣ Static Method (@staticmethod)
Defined using @staticmethod.
No self or cls parameter (works independently).
Used for utility functions inside a class.
📌 Example

class Example:
    @staticmethod
    def static_method():
        return "Static Method: No self or cls"

print(Example.static_method())  # ✅ Call using class



✅ Output:
 Static Method: No self or cls



🔹 Key Points:
✔ No access to instance (self) or class (cls) attributes.
✔ Can be called using class or instance (Example.static_method()).
✔ Used for helper methods (e.g., math operations, format conversions).


🔹 Full Example: Difference in Action
class Car:
    brand = "Toyota"  # ✅ Class variable

    def __init__(self, model):
        self.model = model  # ✅ Instance variable

    def instance_method(self):
        return f"Car Model: {self.model}"  # ✅ Uses instance variable

    @classmethod
    def class_method(cls):
        return f"Car Brand: {cls.brand}"  # ✅ Uses class variable

    @staticmethod
    def static_method():
        return "Cars have four wheels"  # ✅ No self or cls

# Creating an instance
car = Car("Corolla")

# Calling methods
print(car.instance_method())  # ✅ Needs instance
print(Car.class_method())  # ✅ Can be called via class
print(Car.static_method())  # ✅ Can be called via class


✅ Output:
    
 Car Model: Corolla
Car Brand: Toyota
Cars have four wheels



🔹 When to Use Which?

Method Type	Needs self?	Needs cls?	Accesses Instance Variables?	Accesses Class Variables?	Typical Use Case
Instance Method	✅ Yes	❌ No	✅ Yes	❌ No	Modify object state
Class Method	❌ No	✅ Yes	❌ No	✅ Yes	Modify class state
Static Method	❌ No	❌ No	❌ No	❌ No	Utility/helper functions



Advanced Level
What are weak references in Python?
How does Python handle multiple inheritance?
What is monkey patching in Python?
What is the difference between multiprocessing and multithreading?
Explain Python’s dataclass and how it differs from a regular class.
How do you handle circular imports in Python?
What are Python's built-in functions for functional programming (e.g., map(), reduce(), filter())?
How do you optimize a Python application for performance?
Explain the difference between synchronous and asynchronous programming in Python.
How do you implement dependency injection in Python?


q21)What are weak references in Python?

🔹 Weak References in Python (weakref Module)
In Python, a weak reference is a special type of reference that does not prevent an object from being garbage collected.
 It is useful when you want to reference an object without increasing its reference count, allowing Python's garbage collector (GC) to free memory when needed.

📌 By default, Python uses strong references, meaning an object remains in memory as long as at least one reference exists.

🔹 Key Use Cases: ✔ Caching mechanisms
✔ Avoiding memory leaks
✔ Implementing observer patterns

✅ Example: Normal (Strong) Reference vs Weak Reference

📌 Strong Reference (Prevents Garbage Collection)
class Example:
    def __del__(self):
        print("Object deleted")

obj = Example()  # ✅ Strong reference
del obj  # ❌ Deleted, but memory is freed only when no references exist


⏳ If other references exist, __del__() won't be called immediately.

📌 Weak Reference (Allows Garbage Collection)
We use Python’s weakref module to create weak references.

import weakref

class Example:
    def __del__(self):
        print("Object deleted")

obj = Example()  # ✅ Strong reference
weak_ref = weakref.ref(obj)  # ✅ Weak reference

print(weak_ref())  # ✅ Returns the object

del obj  # 🔥 Object is deleted as weak references don’t prevent GC

print(weak_ref())  # ✅ Returns None (object is garbage collected)

✅ Output:
<__main__.Example object at 0x...>
Object deleted
None

✔ Since weak_ref is not a strong reference, the object gets garbage collected when obj is deleted.

✅ Real-World Example: Caching
Weak references are commonly used in caching scenarios where objects should be automatically removed when no longer needed.

import weakref

class User:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"User {self.name} deleted")

cache = weakref.WeakValueDictionary()  # ✅ Dictionary with weak references

# Creating objects
user1 = User("Alice")
user2 = User("Bob")

cache["user1"] = user1
cache["user2"] = user2

print(cache.keys())  # ✅ dict_keys(['user1', 'user2'])

# Deleting strong references
del user1
del user2

print(cache.keys())  # ✅ Now empty (objects are deleted)

✅ Output:
    
dict_keys(['user1', 'user2'])
User Alice deleted
User Bob deleted
dict_keys([])


✔ Without weak references, the cache would hold references, preventing garbage collection.
✔ With WeakValueDictionary, the cache automatically removes objects when they are deleted.

🔹 Summary
Feature	Strong Reference	Weak Reference
Prevents GC	✅ Yes	❌ No
Increases Reference Count	✅ Yes	❌ No
Use Case	Keeping objects in memory	Caching, avoiding memory leaks
Example	obj = Example()	weakref.ref(obj)

q22)How does Python handle multiple inheritance?
🔹 Multiple Inheritance in Python
Python supports multiple inheritance, meaning a class can inherit attributes and methods from more than one parent class.

✅ Example: Basic Multiple Inheritance

class A:
    def show(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A, B):  # ✅ Multiple Inheritance
    pass

obj = C()
obj.show()      # ✅ Inherited from A
obj.display()   # ✅ Inherited from B

✅ Output:
 Class A
Class B


✔ C inherits both A and B.
✔ obj.show() calls show() from A.
✔ obj.display() calls display() from B.

🔹 Method Resolution Order (MRO)
When a method is called on an object, Python follows the Method Resolution Order (MRO) to determine which method to invoke.
MRO follows the C3 Linearization (C3 Algorithm), which ensures a consistent order.
📌 Example: Understanding MRO

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # ✅ Multiple Inheritance
    pass

obj = D()
obj.show()  # ✅ Resolves based on MRO
print(D.__mro__)  # ✅ Check MRO order


✅ Output:

B
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


✔ Python looks for show() in D → B → C → A → object.
✔ Since B has show(), it is executed.



🔹 Using super() in Multiple Inheritance
The super() function calls the next method in the MRO order.

📌 Example: super() in Multiple Inheritance

class A:
    def show(self):
        print("A")
        super().show()  # Calls next method in MRO

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

obj = D()
obj.show()  # Calls methods in MRO order


✅ Output (Following MRO Order):
    
D
B
C
A



🔹 Diamond Problem in Python
When two parent classes have the same method, Python ensures each method is executed only once using MRO.

📌 Example: Diamond Problem


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

obj = D()
obj.show()

output:
D
B
C
A


✔ Python prevents calling A.show() twice (no duplicate execution).

🔹 Summary
Concept	Explanation
Multiple Inheritance	Class inherits from multiple parent classes.
MRO (Method Resolution Order)	Follows C3 Linearization algorithm.
Diamond Problem	Python ensures methods are called only once using super().
super() in Multiple Inheritance	Calls the next method in the MRO order.

q23) What is monkey patching in Python?
🔹 Monkey Patching in Python
Monkey patching is a technique in Python where we dynamically modify or extend a class or module at runtime without altering its original source code.

This is commonly used for: ✔ Fixing bugs in third-party libraries
✔ Modifying library behavior
✔ Adding features to existing modules
✔ Testing by mocking functions


✅ Example: Monkey Patching a Class Method
class Animal:
    def speak(self):
        return "Original Sound"

# ✅ New function to replace the original method
def new_speak():
    return "Monkey Patched Sound"

# ✅ Apply the monkey patch
Animal.speak = new_speak  

obj = Animal()
print(obj.speak())  # 🔥 Output: Monkey Patched Sound


✔ The speak() method is overwritten at runtime.
✔ Now, all instances of Animal use the new function.

✅ Monkey Patching Built-in Modules
You can modify built-in modules without editing the source code.
📌 Example: Patching time.sleep for Faster Executio

import time

def fast_sleep(seconds):
    print(f"Skipping sleep for {seconds} seconds")

# ✅ Monkey patching time.sleep
time.sleep = fast_sleep  

time.sleep(5)  # 🔥 Output: Skipping sleep for 5 seconds

✔ Useful for testing, where actual delays are undesirable.

✅ Monkey Patching for Unit Testing
In unit tests, we patch external dependencies to control their behavior.

📌 Example: Patching requests.get()

import requests

# ✅ Dummy function to mock API response
def mock_get(url):
    return "Mocked API Response"

# ✅ Monkey patch requests.get
requests.get = mock_get  

print(requests.get("https://example.com"))  
# 🔥 Output: Mocked API Response


✔ Helps test code without making actual API calls.

🔹 Risks of Monkey Patching
⚠ Hard to Maintain – Future updates can break patches
⚠ Global Effect – Affects all instances of a class/module
⚠ Debugging Issues – Unexpected behavior due to modifications

🔹 Safer Alternatives:
✅ Use Inheritance – Extend classes instead of modifying them
✅ Use Mocking Libraries – Use unittest.mock for safer testing

Note : few more concept:


🔹 @property Decorator in Python
The @property decorator in Python is used to define a getter method for a class attribute,
 making it behave like an attribute while still allowing customization of its behavior.

It allows:

Encapsulation – Provides controlled access to private variables.
Read-only Properties – Prevents direct modification of attributes.
Automatic Computation – Computes values dynamically.


✅ Example 1: Basic Usage of @property


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private variable

    @property
    def radius(self):
        """Getter method for radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method for radius"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Read-only property for computed area"""
        return 3.1416 * self._radius * self._radius

# ✅ Example Usage
c = Circle(5)
print(c.radius)  # 🔥 Output: 5
print(c.area)    # 🔥 Output: 78.54 (Computed automatically)

c.radius = 10    # ✅ Updating radius
print(c.area)    # 🔥 Output: 314.16 (Updated value)

# c.area = 50  # ❌ ERROR: 'area' is read-only


🔹 Explanation:

radius has getter and setter, allowing controlled access.
area is a read-only property (no setter), so it cannot be assigned.


✅ Example 2: Using @property for Data Validation

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """Getter for age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age with validation"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# ✅ Example Usage
p = Person("Alice", 25)
print(p.age)  # 🔥 Output: 25

p.age = 30   # ✅ Update age
print(p.age) # 🔥 Output: 30

# p.age = -5  # ❌ ERROR: Age cannot be negative


✅ Example 3: Using @property to Compute Dynamic Attributes
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        """Converts Celsius to Fahrenheit"""
        return (self._celsius * 9/5) + 32

# ✅ Example Usage
temp = Temperature(0)
print(temp.fahrenheit)  # 🔥 Output: 32.0 (Computed automatically)

# temp.fahrenheit = 100  # ❌ ERROR: Cannot assign to read-only property

🔹 Here, fahrenheit is a computed attribute and does not need explicit storage.


🔹 When to Use @property?
Encapsulation – Hide internal details while exposing controlled access.
Computed Properties – Return dynamically calculated values.
Read-Only Attributes – Prevent direct modification of certain properties.
Validation – Enforce rules when setting attribute values.


🔹 @property with Class Variables
Normally, the @property decorator works with instance attributes, but we can also use it to create computed properties based on class variables

✅ Example 1: Using @property with a Class Variable

class Company:
    _company_name = "Tech Corp"  # Class Variable (Private)

    @property
    def company_name(self):
        """Getter for class variable"""
        return Company._company_name

# ✅ Example Usage
emp1 = Company()
emp2 = Company()

print(emp1.company_name)  # 🔥 Output: Tech Corp
print(emp2.company_name)  # 🔥 Output: Tech Corp

# emp1.company_name = "New Corp"  # ❌ ERROR: Read-only property


🔹 Key Points:

_company_name is a class variable.
@property allows read-only access to it.
We cannot directly modify it via an instance.

✅ Example 2: Using @classmethod with @property for Class-Level Access

class Company:
    _company_name = "Tech Corp"

    @classmethod
    @property
    def company_name(cls):
        """Getter for class variable"""
        return cls._company_name

    @classmethod
    def set_company_name(cls, new_name):
        """Setter for class variable"""
        cls._company_name = new_name

# ✅ Example Usage
print(Company.company_name)  # 🔥 Output: Tech Corp

Company.set_company_name("New Tech Corp")
print(Company.company_name)  # 🔥 Output: New Tech Corp


🔹 Key Points:

@classmethod allows us to modify class variables.
The getter remains a property, but setter is a class method.

✅ Example 3: Using @property with Static Variables
A static variable (class variable) is shared among all instances

class Counter:
    _count = 0  # Static (Class) Variable

    def __init__(self):
        Counter._count += 1  # Increment count when a new instance is created

    @property
    def count(self):
        """Getter for static variable"""
        return Counter._count

# ✅ Example Usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print(obj1.count)  # 🔥 Output: 3 (Shared across all instances)
print(obj2.count)  # 🔥 Output: 3
print(obj3.count)  # 🔥 Output: 3

🔹 Key Points:

_count is shared across all instances.
@property allows instances to access it without modifying it.

🔹 When to Use @property with Class/Static Variables?
When you want a computed attribute based on class-level data.
When you need read-only access to a shared variable.
When you want encapsulation, preventing direct modification.

🔹 Using @property for Caching in Python
In some cases, computing a property repeatedly can be expensive (e.g., fetching data from a database, performing heavy calculations).
 We can use caching to store the computed value and return it on subsequent calls.
 
 ✅ Example 1: Simple Caching with @property
 class DataFetcher:
    def __init__(self):
        self._data = None  # Cached value

    @property
    def expensive_computation(self):
        """Simulating an expensive computation"""
        if self._data is None:  # Compute only if not cached
            print("Fetching data...")  # Simulate delay
            self._data = sum(range(1000000))  # Expensive computation
        return self._data

# ✅ Example Usage
fetcher = DataFetcher()

print(fetcher.expensive_computation)  # 🔥 Fetching data... (Expensive computation)
print(fetcher.expensive_computation)  # 🔥 Returns cached value instantly

🔹 Key Points:

The first call triggers computation.
Subsequent calls return the cached value instantly.

✅ Example 2: Resetting the Cached Property with a Setter
We can allow resetting the cached value by implementing a setter.

class DataFetcher:
    def __init__(self):
        self._data = None  # Cached value

    @property
    def expensive_computation(self):
        """Simulating an expensive computation"""
        if self._data is None:
            print("Fetching data...")
            self._data = sum(range(1000000))
        return self._data

    @expensive_computation.setter
    def expensive_computation(self, value):
        """Manually reset the cached value"""
        print("Resetting cache...")
        self._data = value

# ✅ Example Usage
fetcher = DataFetcher()

print(fetcher.expensive_computation)  # 🔥 Fetching data...
print(fetcher.expensive_computation)  # 🔥 Cached value returned

fetcher.expensive_computation = None  # 🔥 Reset cache
print(fetcher.expensive_computation)  # 🔥 Fetching data... (Recomputed)


 Key Points:

We added a setter to allow manual cache reset.
Assigning None clears the cached data.

✅ Example 3: Using functools.lru_cache for Automatic Caching
Instead of manually handling caching, Python’s functools.lru_cache decorator can automatically cache results.

from functools import lru_cache

class Fibonacci:
    @staticmethod
    @lru_cache(maxsize=128)  # Cache up to 128 results
    def compute(n):
        """Compute Fibonacci using caching"""
        if n < 2:
            return n
        return Fibonacci.compute(n - 1) + Fibonacci.compute(n - 2)

# ✅ Example Usage
print(Fibonacci.compute(40))  # 🔥 Fast due to caching
print(Fibonacci.compute(41))  # 🔥 Uses previous cache for efficiency


🔹 Key Points:

@lru_cache automatically stores computed values.
The second time a value is requested, it returns instantly.
This is useful for recursive computations like Fibonacci
 When to Use Cached Properties?
 
Expensive computations (e.g., database queries, API calls, large calculations).
When data rarely changes, caching improves performance.
Recursive functions (like Fibonacci, Factorial, etc.).
Reducing redundant computations in a program.

***
Context Managers in Python (with Statement)
A context manager is a Python construct that allows resource management, ensuring that certain setup and cleanup operations are performed automatically. 
It is commonly used to manage files, database connections, threading locks, etc.


 Using contextlib for a Simpler Context Manager
The contextlib module provides a cleaner way to create context managers using a generator function.

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering")
    yield  # Code inside `with` runs here
    print("Exiting")

with my_context():
    print("Inside the block")


output:
Entering
Inside the block
Exiting

How It Works?

The function runs up to the yield statement when entering the block.
Code inside the with block executes.
After the with block, the function resumes after yield and handles cleanup.


Real-World Example: Database Connection
Context managers are useful for managing database connections.

import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        yield cursor  # Allows executing queries
        conn.commit()
    finally:
        conn.close()

# Usage
with database_connection("mydb.sqlite") as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")





Handling Exceptions in __exit__
If an error occurs inside the with block, __exit__ receives the exception details.

class HandleError:
    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception caught: {exc_value}")
            return True  # Suppress the exception
        print("Exiting")

# Example usage
with HandleError():
    print("Inside block")
    raise ValueError("Something went wrong!")  # Exception is handled

out:
Entering
Inside block
Exception caught: Something went wrong!

Summary
Method	How It Works	Example
Built-in (with open())	Manages files, sockets, etc.	with open("file.txt") as f:
Class-based (__enter__/__exit__)	More control over setup/cleanup	Custom resource management
Function-based (contextlib.contextmanager)	Simplifies context managers using yield	@contextmanage



1. Creating a Basic Custom Exception

Define a custom exception by subclassing Exception:

class CustomError(Exception):
    """Custom exception for specific errors."""
    pass

# Raising the custom exception
raise CustomError("This is a custom error!")

output:
    
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
__main__.CustomError: This is a custom error!

2. Custom Exception with Additional Attributes

You can add attributes to store extra information.

class InvalidAgeError(Exception):
    """Exception raised for invalid age input."""

    def __init__(self, age, message="Age must be between 18 and 60"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. Given: {age}")

# Usage
def check_age(age):
    if not (18 <= age <= 60):
        raise InvalidAgeError(age)
    return "Valid age"

try:
    print(check_age(15))
except InvalidAgeError as e:
    print(f"Error: {e}")


output:

Error: Age must be between 18 and 60. Given: 15

3. Handling Multiple Custom Exceptions
You can define multiple custom exceptions for different error types.

class NegativeValueError(Exception):
    pass

class ZeroValueError(Exception):
    pass

def process_number(num):
    if num < 0:
        raise NegativeValueError("Number cannot be negative!")
    elif num == 0:
        raise ZeroValueError("Number cannot be zero!")
    else:
        return f"Processing number: {num}"

try:
    print(process_number(-5))
except NegativeValueError as e:
    print(f"Negative Error: {e}")
except ZeroValueError as e:
    print(f"Zero Error: {e}")

Negative Error: Number cannot be negative!

4. Using __str__ for Custom Error Messages
Override __str__ for a better error message format.

class FileReadError(Exception):
    def __init__(self, filename, message="Error reading file"):
        self.filename = filename
        self.message = message

    def __str__(self):
        return f"{self.message}: {self.filename}"

try:
    raise FileReadError("data.txt")
except FileReadError as e:
    print(e)

output:
Error reading file: data.txt

5. Using a Custom Base Exception Class
For multiple related exceptions, create a base exception class.

class ApplicationError(Exception):
    """Base class for all application-related errors."""
    pass

class DatabaseError(ApplicationError):
    """Raised when a database operation fails."""
    pass

class APIError(ApplicationError):
    """Raised when an API request fails."""
    pass

try:
    raise DatabaseError("Database connection failed!")
except ApplicationError as e:  # Catches both DatabaseError and APIError
    print(f"Application Error: {e}")

output:
Application Error: Database connection failed!

6. Raising Custom Exceptions in Real-World Scenarios
Example: Custom Authentication Exception

class AuthenticationError(Exception):
    def __init__(self, user, message="Invalid credentials"):
        self.user = user
        self.message = message
        super().__init__(f"User '{user}': {message}")

def login(user, password):
    if password != "securepassword":
        raise AuthenticationError(user)
    return "Login successful"

try:
    print(login("john_doe", "wrongpassword"))
except AuthenticationError as e:
    print(f"Login failed: {e}")

out:
Login failed: User 'john_doe': Invalid credentials

Feature	Example
Basic Custom Exception	class MyError(Exception): pass
Adding Attributes	def __init__(self, message, code):
Handling Multiple Exceptions	except (Error1, Error2) as e:
Custom __str__ Method	Better error messages
Using a Base Exception Class	Organize related errors


1️⃣ Handling Exceptions Using try-except

✅ Basic Example

try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")


Outpu:
    
You can't divide by zero!

2️⃣ Handling Multiple Exceptions
✅ Catching Multiple Errors

try:
    num = int(input("Enter a number: "))  # Might raise ValueError
    result = 10 / num  # Might raise ZeroDivisionError
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You can't divide by zero!")

✅ Catching Multiple Exceptions in One Block

try:
    x = int("abc")  # Raises ValueError
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")

Output:
An error occurred: invalid literal for int() with base 10: 'abc'

3️⃣ Using else and finally
✅ else Block Executes When No Exception Occurs

try:
    num = 5
    result = 10 / num  # No error
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful:", result)

output:
    
Division successful: 2.0

✅ finally Always Executes (Useful for Cleanup)

try:
    file = open("test.txt", "w")
    file.write("Hello, World!")
except IOError:
    print("File operation failed.")
finally:
    file.close()  # Ensures file is closed even if an error occurs

4️⃣ Raising Exceptions Using raise
✅ Manually Raising an Exception

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return "Allowed"

print(check_age(20))  # Allowed
print(check_age(16))  # Raises ValueError


 Using assert for Debugging
✅ assert Raises an Exception If Condition is False
x = 10
assert x > 5  # No error
assert x < 5, "x must be less than 5"  # Raises AssertionError


 Best Practices for Exception Handling
✅ Catch Specific Exceptions (Avoid except Exception: unless necessary).
✅ Use finally to release resources.
✅ Log Errors instead of printing them.
✅ Use Custom Exceptions when needed for clarity.



In Python, dictionary keys must be immutable (unchangeable) types.
This means the key can be:

Strings ✅
Numbers (integers, floats) ✅
Tuples (if they contain only immutable elements) ✅
However, the key cannot be a list or another dictionary ❌ because lists and dictionaries are mutable.


Valid and Invalid Dictionary Keys with Examples
Key Type	Valid as Dictionary Key?	Example
String	✅ Yes	{"name": "Alice"}
Integer	✅ Yes	{1: "One", 2: "Two"}
Float	✅ Yes	{3.14: "Pi"}
Tuple (Immutable)	✅ Yes	{(1, 2): "Point"}
List (Mutable)	❌ No	{["a", "b"]: "Invalid"} → ❌ Error
Dictionary (Mutable)	❌ No	{{"key": "value"}: "Invalid"} → ❌ Error



# ✅ Valid keys
valid_dict = {
    "name": "Alice",  # String key
    42: "Answer",  # Integer key
    3.14: "Pi",  # Float key
    (1, 2, 3): "Tuple Key"  # Tuple key
}

print(valid_dict)

# ❌ Invalid keys - Uncommenting these lines will cause an error
# invalid_dict = {
#     ["list_key"]: "Invalid",  # ❌ TypeError: unhashable type: 'list'
#     {1: "value"}: "Invalid"   # ❌ TypeError: unhashable type: 'dict'
# }


Key Takeaways
✅ Use immutable types as keys: str, int, float, and tuple (only immutable elements).
❌ Avoid mutable types: list, dict, set.


Python provides built-in string methods to check if a string consists only of letters, numbers, or a mix of both. These methods are:

isalpha() → Returns True if the string contains only letters (a-z, A-Z).
isdigit() → Returns True if the string contains only digits (0-9).
isalnum() → Returns True if the string contains only letters or numbers (no spaces or special characters).

Examples of isalpha(), isdigit(), and isalnum()

# isalpha() - Only letters (no numbers or special characters)
print("Hello".isalpha())  # ✅ True
print("Hello123".isalpha())  # ❌ False (contains numbers)
print("Hello!".isalpha())  # ❌ False (contains special character)

# isdigit() - Only digits (no letters or special characters)
print("12345".isdigit())  # ✅ True
print("123abc".isdigit())  # ❌ False (contains letters)
print("12.34".isdigit())  # ❌ False (contains a decimal point)

# isalnum() - Letters and numbers only (no spaces or special characters)
print("Hello123".isalnum())  # ✅ True (letters + numbers)
print("123".isalnum())  # ✅ True (only numbers)
print("Hello World".isalnum())  # ❌ False (contains space)
print("Hello@123".isalnum())  # ❌ False (contains special character '@')

When to Use These Methods
✅ isalpha() → Validating names (e.g., checking if a user entered only letters in a name field).
✅ isdigit() → Validating age, phone numbers, or numerical inputs (without decimal points).
✅ isalnum() → Validating usernames or passwords (only letters and numbers, no special characters).



Great question! Here's a clear and concise explanation of the difference between the Python Interpreter and Python Virtual Machine (PVM):

🔹 1. Python Interpreter
✅ Definition:
The Python interpreter is the program that reads and executes Python code.

✅ Function:
It takes your .py (source) file and processes it line by line.

It handles:

Syntax checking

Compiling source code to bytecode (.pyc)

Passing bytecode to the Python Virtual Machine (PVM)

✅ Role:
Converts high-level code into intermediate bytecode

Example: turns print("Hello") into a set of instructions the VM can understand

🔹 2. Python Virtual Machine (PVM)

✅ Definition:
The PVM is a part of the interpreter that executes the bytecode.

✅ Function:
It reads .pyc (bytecode) files and executes instructions on the CPU.

This is where the actual program runs.

✅ Role:
Acts like a runtime engine

Responsible for memory management, garbage collection, and executing instructions.


Summary Table

| Feature        | Python Interpreter                | Python Virtual Machine (PVM)     |
| -------------- | --------------------------------- | -------------------------------- |
| **What it is** | Interface for running `.py` files | Bytecode execution engine        |
| **Main Job**   | Converts source code to bytecode  | Executes bytecode                |
| **Output**     | Bytecode (`.pyc` files)           | Final execution of the program   |
| **Stage**      | Compilation (source → bytecode)   | Execution (bytecode → CPU ops)   |
| **Part of**    | Entire Python execution process   | Component inside the interpreter |



🔁 Execution Flow in Python
.py (source code)
  ↓  [Interpreter]
.pyc (bytecode)
  ↓  [Python Virtual Machine]
Machine execution (program runs)

🧠 Analogy:
Think of the interpreter as a translator that converts your language (Python) into a secret code (bytecode).

The PVM is the executor that understands this secret code and performs actions on your computer.

d.popitem() in Python:
✅ Definition:
    
d.popitem() is a dictionary method that removes and returns the last inserted key-value pair from the dictionary.

🔧 Syntax:
dict.popitem()

📌 Return Value:
Returns a tuple: (key, value)

Removes that key-value pair from the dictionary.


⚠️ Behavior Notes:
| Version      | Behavior                            |
| ------------ | ----------------------------------- |
| Python ≤ 3.6 | Removes a **random** key-value pair |
| Python ≥ 3.7 | Removes the **last inserted** item  |

🧪 Example:
  d = {'a': 1, 'b': 2, 'c': 3}
item = d.popitem()
print(item)  # ('c', 3)
print(d)     # {'a': 1, 'b': 2}



❌ Raises Error:
If the dictionary is empty, it raises a KeyError.
d = {}
d.popitem()  # KeyError


✅ Use Case:
When you want to safely remove items one by one from the end of a dictionary (like a stack), especially in LRU cache or similar use cases.


🔄 What is LRU Cache?
It keeps the most recently used items in memory.

If the cache exceeds its size, it evicts the least recently used item (the one used the longest time ago).


✅ Simple Implementation Using dict.popitem()

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}            # Main dictionary to store key-value pairs
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the key to the end to mark it as recently used
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old key to update its position
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item (first one inserted)
            self.cache.popitem(last=False)  # `last=False` requires OrderedDict
        self.cache[key] = value



⚠️ Wait! Why popitem(last=False)?
Python dict does not support last=False in popitem() by default.

So to use popitem(last=False) for evicting the oldest item, we need to use collections.OrderedDict (which is built into Pytho


✅ Full Example with OrderedDict

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end to show it's recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used item (first item)
            self.cache.popitem(last=False)
        self.cache[key] = value


🧪 Usage Example:
lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
print(lru.get(1))  # 10
lru.put(3, 30)     # Evicts key 2
print(lru.get(2))  # -1 (not found)


✅ 1. Using Only dict (Python ≥ 3.7+ maintains insertion order)
⚠️ Limitation:
Native dict.popitem() always removes the last item, not the oldest, so we have to manually handle usage order using a list.


✅ Code: LRU Cache with plain dict + usage tracking

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.usage = []  # Tracks usage order (most recent at end)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the key to the end to mark it as recently used
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove from usage to re-insert at the end
            self.usage.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item
            lru_key = self.usage.pop(0)
            self.cache.pop(lru_key)
        self.cache[key] = value
        self.usage.append(key)


✅ Usage:
lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
print(lru.get(1))  # Output: 10
lru.put(3, 30)     # Evicts key 2
print(lru.get(2))  # Output: -1



✅ 2. Using functools.lru_cache (built-in decorator)

If your goal is to cache results of a function, Python provides a ready-made solution:
from functools import lru_cache

@lru_cache(maxsize=2)
def get_data(x):
    print(f"Fetching {x}")
    return x * 2


print(get_data(1))  # Fetches and caches
print(get_data(2))  # Fetches and caches
print(get_data(1))  # Uses cache
print(get_data(3))  # Evicts least recently used (2), caches 3
print(get_data(2))  # Refetches 2 (it was evicted)


✅ Output:
 Fetching 1
2
Fetching 2
4
2
Fetching 3
6
Fetching 2
4


🔁 Summary of All 3 Methods:
    
    
 | Approach                      | Type             | Manual Work Needed | Use Case                            |
| ----------------------------- | ---------------- | ------------------ | ----------------------------------- |
| `dict + list`                 | Manual LRU       | ✅ Yes              | Custom behavior or learning         |
| `OrderedDict`                 | Semi-native      | ❌ No               | Real use-case in apps, clean logic  |
| `@lru_cache` from `functools` | Native Decorator | ❌ No               | Function memoization, quick caching |


Great! Let’s now look at how LRU Cache is applied in real-world systems like web caching and databases, and how to make your LRU Cache thread-safe in Python.


✅ 1. Real-World Use Cases of LRU Cache
🔸 Web Caching
Browser Cache: Keeps the most recently viewed pages.

CDNs (Cloudflare, Akamai): Cache the most requested resources like images, JS, CSS.

API Gateway: Caches frequent API responses to reduce backend load.

📌 Example:
If you request /user/123 multiple times, the cache stores it.
When the cache is full, it removes the least recently accessed user.


🔸 Databases (e.g., Redis, PostgreSQL)
Caches recently accessed rows, queries, or index pages.

Avoids disk I/O for repeated reads.

LRU eviction is commonly used in Redis.




🔸 Machine Learning
Caches preprocessed data or feature embeddings to save CPU/GPU time.




✅ 2. Making LRU Cache Thread-Safe in Python
In multi-threaded applications (like a Django/Flask backend), you may have concurrent reads/writes. Let’s use threading.Lock to protect critical sections.

🔒 Thread-Safe LRUCache with OrderedDict

from collections import OrderedDict
from threading import Lock

class ThreadSafeLRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.lock = Lock()

    def get(self, key):
        with self.lock:
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        with self.lock:
            if key in self.cache:
                self.cache.pop(key)
            elif len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value



✅ Usage Example:
 
 import threading

cache = ThreadSafeLRUCache(2)

def worker_put():
    for i in range(4):
        cache.put(i, i * 100)

def worker_get():
    for i in range(4):
        print(f"Key {i}: {cache.get(i)}")

# Launch threads
t1 = threading.Thread(target=worker_put)
t2 = threading.Thread(target=worker_get)

t1.start()
t2.start()
t1.join()
t2.join()


🔁 Summary

| Feature             | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| **Thread-safe LRU** | Ensures correct behavior in multithreaded apps                   |
| **Web cache**       | Stores frequently accessed web/API data                          |
| **DB cache**        | Avoids repeated computation or disk reads                        |
| **@lru\_cache**     | Best for caching function outputs (e.g., expensive calculations) |




Great question! The __init__.py file is quite important in Python packages. Here's what you can write or do inside it:

What can you write inside __init__.py?
1. Make a directory a package
Simply having an __init__.py (even an empty file) tells Python this folder is a package.

Without it, Python 2.x and some tools wouldn't recognize the folder as a package (Python 3.3+ supports implicit namespace packages, but it's still good practice).




2. Initialize package-level variables
You can define variables/constants that belong to the package:
    
# __init__.py
package_version = "1.0.0"
author = "Murli"


3. Import modules or classes for convenient access
To allow users to import package components more easily:

# __init__.py
from .addition import add
from .subtraction import subtract

Now users can do:
from mypackage import add, subtract

instead of:
from mypackage.addition import add
from mypackage.subtraction import subtract


4. Package-level setup code
You can run code that needs to be executed when the package is first imported:

print("mypackage initialized")

(Be careful with this; avoid heavy or side-effect code.)


5. Define __all__ for controlled imports
The __all__ list controls what from package import * imports:

__all__ = ["add", "subtract"]



6. Expose only a subset of the package
You can hide internal modules and expose only what you want via imports in __init__.py.

Summary:
    
| Purpose                   | Example/Usage                              |
| ------------------------- | ------------------------------------------ |
| Mark directory as package | Empty `__init__.py`                        |
| Package-level variables   | `version = "1.0"`                          |
| Import submodules/classes | `from .module import ClassName`            |
| Setup code on import      | `print("Initializing package")`            |
| Control wildcard imports  | `__all__ = ["foo", "bar"]`                 |
| Hide internal details     | Import only what’s needed in `__init__.py` |

































    
    