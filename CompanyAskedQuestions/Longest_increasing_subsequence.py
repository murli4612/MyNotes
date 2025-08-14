# def longestIncreasingSubsequence(nums):
#     LIS = [1] * len(nums)
    
#     for i in range(len(nums) - 1 , -1 , -1):
#         for j in range( i + 1 , len(nums)):
#             if nums[i] < nums[j]:
#                 LIS[i] = max(LIS[i], 1 + LIS[j])
#     return max(LIS)

# nums = [1,2 ,4,3]
# print(longestIncreasingSubsequence(nums))


def longestIncreasingSubsequences(nums):
    n = len(nums)
    dp = [1] * n
    # Step 1: Calculate LIS length for each index
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    max_len = max(dp)

    # Step 2: Use DFS to collect all sequences
    result = []

    def dfs(index, path):
        if len(path) == max_len:
            result.append(path[:])
            return
        for next_index in range(index + 1, n):
            if nums[next_index] > nums[index] and dp[next_index] == dp[index] - 1:
                dfs(next_index, path + [nums[next_index]])

    # Start DFS from all indexes with dp[i] == max_len
    for i in range(n):
        if dp[i] == max_len:
            dfs(i, [nums[i]])

    print("Length of LIS:", max_len)
    print("All Longest Increasing Subsequences:")
    for seq in result:
        print(seq)

# Example usage
nums = [1, 2, 4, 3]
longestIncreasingSubsequences(nums)
