class Solution:  
    def longestPalindromicSubstring(self,s):
        if not s:
            return []
        
        max_len = 0
        result = set()
        
        for i in range(len(s)):
            #check odd length palindrom
            p1 = self.expandAroundCenter(i, i ,s)
            #check even lenth palindrome
            p2 = self.expandAroundCenter(i, i + 1,s)
            
            for p in [p1,p2]:
                if len(p) > max_len:
                    max_len = len(p)
                    result = {p}
                elif len(p) == max_len:

                    result.add(p)
        return list(result)
        
    def expandAroundCenter(self,left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left + 1:right]


sol = Solution()
print(sol.longestPalindromicSubstring("mumxyzili"))  # Output: ['bab', 'aba']