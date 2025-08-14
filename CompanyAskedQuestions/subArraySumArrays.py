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