from collections import defaultdict

def word_break(s, word_dict):
    word_set = set(word_dict)
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

    return [" ".join(words) for words in memo[s]]
