class Solution:
    def reverseWords(self, s):
        # Split by spaces and filter out empty strings
        words = s.split()
        # Reverse the list
        reversed_words = words[::-1]
        # Join with a single space
        return ' '.join(reversed_words)