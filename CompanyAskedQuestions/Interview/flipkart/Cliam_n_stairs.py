# Here, you can climb 1 step, 2 steps, or 3 steps at a time.
# We need to find how many distinct ways you can climb to the top of n stairs.

# Recursive + Memoization (Top-Down DP)

def climbStairs(n, memo={}):
    # Base cases
    if n == 0:  # exactly reached
        return 1
    if n < 0:   # overshoot
        return 0
    
    if n in memo:
        return memo[n]
    
    # Choices: take 1 step, 2 steps, or 3 steps
    memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo) + climbStairs(n-3, memo)
    return memo[n]


# Example usage
n = 5
print(f"Number of ways to climb {n} stairs:", climbStairs(n))

# Iterative DP (Bottom-Up)
# This is more efficient (O(n) time, O(1) space).


def climbStairs(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2  # base cases

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


# Example usage
n = 5
print(f"Number of ways to climb {n} stairs:", climbStairs(n))

# ✅ Example outputs:

# n=3 → 4 ways (111, 12, 21, 3)

# n=4 → 7 ways

# n=5 → 13 ways
