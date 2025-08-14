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