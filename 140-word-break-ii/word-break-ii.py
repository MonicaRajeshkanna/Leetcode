class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    rest = dfs(end)

                    for sentence in rest:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return dfs(0)