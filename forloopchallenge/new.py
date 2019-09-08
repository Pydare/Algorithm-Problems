def letterCombinations(digits):
        if not digits: return []
        answer, nums, letters = [''], [int(d) for d in digits], ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for pos in range(len(nums)):
            answer = [prev + letter for prev in answer for letter in letters[nums[pos]]]
        print((answer))

letterCombinations('23')