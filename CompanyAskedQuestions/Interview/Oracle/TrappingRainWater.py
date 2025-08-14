
# Here’s a clean two-pointer approach in Python (O(n) time, O(1) space):


# How it works:
# 1)Two pointers start at both ends (left, right).

# 2)Maintain max height seen so far from both ends (left_max, right_max).

# 3)Move the pointer with the smaller max height inward:

# 4)Water trapped = (current max height) − (current bar height).

# 5)Continue until pointers meet.


def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            trapped_water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped_water += right_max - height[right]

    return trapped_water


# Example usage:
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
