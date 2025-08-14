# Design a stack that supports:

#     push(x)

#     pop()

#     top()

#     getMin() — Retrieve the minimum element in constant time.

# All operations must be O(1) time complexity.

# ✅ Solution Approach: Use Two Stacks
# We use:

#    --> Main Stack (stack) – stores all values

#     -->Min Stack (min_stack) – keeps track of current minimums



# ✅ Key Insight:
# Every time we push, we also check:

#     If the new value is less than or equal to the current minimum (min_stack[-1])

#     If so, we also push it onto the min_stack

# When we pop, we do:

#     Pop from the main stack

#     If that value is also the top of min_stack, we pop from min_stack too.

# This way, min_stack always has the current minimum at the top.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Stores current minimum

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack: either it's the first element or the new min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())  # ➝ -3
# minStack.pop()
# print(minStack.top())     # ➝ 0
# print(minStack.getMin())  # ➝ -2


def test_min_stack():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
