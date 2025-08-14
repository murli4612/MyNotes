# d = {"a": 1, "b": 2}
# print(d.get("a"))          # 1
# print(d.items())           # dict_items([('a', 1), ('b', 2)])
# d.pop("b")
# d.update({"c": 3})
# print("c" in d)            # True
# print(d.items()) # dict_items([('a', 1), ('c', 3)])


# def outer():
#     x = 10  # <-- 'x' is in the enclosing scope for 'inner'

#     def inner():
#         print(x)  # 'inner' can access 'x' from 'outer'
    
#     inner()
# # outer()

# import functools

# def my_decorator(func):
#     # @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def example():
#     """This is an example function."""
#     print("Example function running")

# print(example.__name__)  # Output: example
# print(example.__doc__)   # Output: This is an example function.


# def filter_nested(d, threshold=50):
#     if isinstance(d, dict):
#         return {k: filter_nested(v, threshold) for k, v in d.items() if isinstance(v, dict) or v >= threshold}
#     return d

# data = {
#     "A": {"math": 80, "science": 90},
#     "B": {"math": 45, "science": 55},
#     "C": {"math": 60, "science": {"physics": 40, "chemistry": 85}},
# }

# filtered_data = filter_nested(data, 50)
# print(filtered_data)


# def dailyTemperatures(temperatures):
#     n = len(temperatures)
#     result = [0] * n
#     stack = []  # stores indices of temperatures

#     for i in range(n - 1, -1, -1):  # traverse from right to left
#         while stack and temperatures[i] >= temperatures[stack[-1]]:
#             stack.pop()

#         if stack:
#             result[i] = stack[-1] - i  # number of days to wait

#         stack.append(i)  # push current day's index

#     return result

# input = [73, 74, 75, 71, 69, 72, 76, 73]
# print(dailyTemperatures(input))


# import logging

# # 🔧 Configure logging: log only errors to a file named 'error.log'
# logging.basicConfig(filename='error.log', level=logging.ERROR ,format='%(asctime)s - %(levelname)s - %(message)s')

# # 🎯 Decorator to log exceptions
# def log_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             error_message = f"Error in {func.__name__}: {str(e)}"
#             logging.error(error_message)      # log the error to the file
#             # print(error_message)              # print to console (optional)
#             # raise e  # Optional: re-raise the exception
#     return wrapper

# # 👇 Apply the decorator to functions

# @log_exceptions
# def divide(a, b):
#     return a / b

# @log_exceptions
# def open_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# # ✅ Successful call
# result1 = divide(10, 2)     # returns 5.0
# print(result1)

# # ❌ Will raise and log "division by zero"
# result2 = divide(10, 0)     # prints error, logs to 'error.log'


# # import logging

# # # Configure logging to create and write to 'error.log'
# # logging.basicConfig(
# #     filename='error.log',         # 🔹 Log file name
# #     level=logging.ERROR,          # 🔹 Only log ERROR and above
# #     format='%(asctime)s - %(levelname)s - %(message)s'  # 🔹 Format with timestamp
# # )

# # # Log a test error message
# # logging.error("An unexpected error occurred!")


# with open('error.log') as f:
#     print(f.read())



import logging

# 🔧 Configure logging to log only errors to 'error.log'
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 🎯 Decorator to log exceptions
def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            error_message = f"Error in {func.__name__}: {str(e)}"
            logging.error(error_message)
            # Optionally, return something or re-raise the error
            return None
    return wrapper

# 👇 Apply the decorator to functions

@log_exceptions
def divide(a, b):
    return a / b

# @log_exceptions
# def open_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# ✅ Successful call
result1 = divide(10, 2)
print("Result1:", result1)

# ❌ This will cause division by zero and be logged
result2 = divide(10, 0)
print("Result2:", result2)  # Will print None

# 🔍 Read and print the log file content at the end
print("\n--- Contents of error.log ---")
with open('error.log') as f:
    print(f.read())
