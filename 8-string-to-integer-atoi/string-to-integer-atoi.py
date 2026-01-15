class Solution:
    def myAtoi(self, s):
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        # Step 1: Skip whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Handle sign
        sign = 1
        if i < len(s) and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read digits
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # Overflow check before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
