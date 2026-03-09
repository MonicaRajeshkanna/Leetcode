class Solution:
    def titleToNumber(self, columnTitle):
        num = 0
        for c in columnTitle:
            num = num * 26 + (ord(c) - ord('A') + 1)
        return num