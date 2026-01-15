class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        cur_row, direction = 0, -1  # -1 down, 1 up
        
        for char in s:
            rows[cur_row].append(char)
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1  # reverse at top/bottom
            cur_row += direction
        
        return ''.join(''.join(row) for row in rows)
