# BACKTRACKING SOLUTION
def wordBreak(s, wordDict):
    def backtrack(rem):
        if rem == '':
            return True

        for i in range(len(rem)):
            if rem[:i + 1] in wordDict:
                if backtrack(rem[i + 1:]):
                    return True

        return False

    return backtrack(s)

# TOP-DOWN MEMOIZATION SOLUTION
class Solution:
    def wordBreak(self, s: str, wordDict):
        memo = {}
        
        def solution(rem_string, wordDict):
            if not rem_string:
                return True
            
            for idx in range(len(rem_string)):
                prefix = rem_string[:idx+1]
                if prefix in wordDict:
                    new_rem_string = rem_string[idx+1:]
                    val = memo.get(new_rem_string, None)
                    if val is None:
                        val = solution(new_rem_string, wordDict)
                        memo[new_rem_string] = val
                    if val:
                        return True
            
            return False
        
        return solution(s, set(wordDict))

# BFS SOLUTION
from collections import deque
class Solution2:
    def wordBreak(self, s: str, wordDict):
        queue = deque([s])
        seen = set()
        seen.add(s)
        while queue:
            node = queue.popleft()
            for word in wordDict:
                if node.startswith(word):
                    new_node = node[len(word):]
                    if len(new_node) == 0:
                        return True
                    if new_node not in seen:
                        seen.add(new_node)
                        queue.append(new_node)
                        
        return False

# USING BOTTOM-UP DP
class Solution3:
    def wordBreak(self, s: str, wordDict):
        #DP Solution
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp = [False] * (len(s) + 1) 

        dp[0] = True
        for i in range(len(s)): # leetcode ['leet', 'code']
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]


# WORD SEARCH 2
from collections import defaultdict
def word_break_2(s, wordDict):

    word_set = set(wordDict)
    memo = defaultdict(list)

    def word_break_topdown(s):
        if not s:
            return [[]]

        if s in memo:
            return memo[s]

        for end_idx in range(1, len(s)+1):
            word = s[:end_idx]
            if word in word_set:
                # move forwards to break the postfix into words
                for subsentence in word_break_topdown(s[end_idx:]):
                    memo[s].append([word] + subsentence)

        return memo[s]

    word_break_topdown(s)

    # chain up the lists of words into sentences
    return [" ".join(words) for words in memo[s]]