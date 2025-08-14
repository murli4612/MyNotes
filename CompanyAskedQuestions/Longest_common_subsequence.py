# def longestCommonSubSequence(text1, text2):
#     n1 = len(text1)
#     n2 = len(text2)
#     dp = [[ 0 for i in range(n1 + 1)] for j in range(n2 + 1)]
    
#     for i in range (n1 -1,-1,-1):
#         for j in range (n2 -1,-1,-1):
#             if text1[i] == text2[j]:
#                 dp[i][j] = 1 + dp[i + 1][j + 1]
#             else:
#                 dp[i][j] = max(dp[i][j+1], dp[i+1][j])
#     return dp[0][0]



# text1 ="ace"
# text2 ="abcde"

# print(longestCommonSubSequence(text1, text2))
    
    
    
def longestCommonSubSequence(text1, text2):
    n1 = len(text1)
    n2 = len(text2)
    
    # dp[i][j] will hold the LCS length for text1[i:] and text2[j:]
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    print(dp)
    
    for i in range(n1 - 1, -1, -1):
        # print(i)
        for j in range(n2 - 1, -1, -1):
            
            if text1[i] == text2[j]:
               
                # print("k")
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                # print("l")
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    print(dp)
    
    return dp[0][0]

# Example usage
text1 = "ace"
text2 = "abcde"
print(longestCommonSubSequence(text1, text2))  # Output should be 3
