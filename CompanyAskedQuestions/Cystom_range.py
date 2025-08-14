def my_range(start, stop=None, step=1):
    # Handle case where only one argument is provided (like range(stop))
    if stop is None:
        stop = start
        start = 0
    
    # Raise an error if step is zero
    if step == 0:
        raise ValueError("Step cannot be zero")

    result = []  # Store values in a list
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        result.append(start)
        start += step  # Increment by step
    
    return result  # Return the final list

# Usage examples:
print(my_range(5))          # Output: [0, 1, 2, 3, 4]
print(my_range(2, 10, 2))   # Output: [2, 4, 6, 8]
print(my_range(10, 2, -2))  # Output: [10, 8, 6, 4]

for i in my_range(2,10,2):
    print("murli" ,i)


# different method:
def my_range(start, stop=None, step=1):
    # Handle case where only one argument is provided (like range(stop))
    if stop is None:
        stop = start
        start = 0
    
    # Raise error if step is zero to avoid infinite loop
    if step == 0:
        raise ValueError("Step cannot be zero")

    # Generate numbers lazily using yield
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step  # Increment by step

# Usage examples:
print(list(my_range(5)))          # Output: [0, 1, 2, 3, 4]
print(list(my_range(2, 10, 2)))   # Output: [2, 4, 6, 8]
print(list(my_range(10, 2, -2)))  # Output: [10, 8, 6, 4]


for i in my_range(2,10,2):
    print("murli man" ,i)

# /Class based

class MyRange:
    def __init__(self, start, stop=None, step=1):
        # Handle case where only one argument is provided (like range(stop))
        if stop is None:
            stop = start
            start = 0
        
        if step == 0:
            raise ValueError("Step cannot be zero")

        self.start = start
        self.stop = stop
        self.step = step
        self.current = start  # Store current value for iteration

    def __iter__(self):
        return self  # An iterable should return itself

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration  # Stop when out of range

        value = self.current
        self.current += self.step  # Move to the next value
        return value

# Usage examples:
print(list(MyRange(5)))          # Output: [0, 1, 2, 3, 4]
print(list(MyRange(2, 10, 2)))   # Output: [2, 4, 6, 8]
print(list(MyRange(10, 2, -2)))  # Output: [10, 8, 6, 4]

for i in my_range(2,10,2):
    print("murli debo" ,i)

