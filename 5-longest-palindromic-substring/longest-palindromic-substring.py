class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        start, max_length = 0, 1
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1  # valid palindrome bounds
        
        for i in range(len(s)):
            # Odd length palindromes
            l1, r1 = expand_around_center(i, i)
            # Even length palindromes
            l2, r2 = expand_around_center(i, i + 1)
            
            # Update max
            len1 = r1 - l1 + 1
            len2 = r2 - l2 + 1
            if max(len1, len2) > max_length:
                start = l1 if len1 > len2 else l2
                max_length = max(len1, len2)
        
        return s[start:start + max_length]

