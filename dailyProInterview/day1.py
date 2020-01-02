def lengthOfLongestSubstring(s):
        s = [i for i in s]
        first_pointer = 0
        second_pointer = 0
        max_counter = 0
        tracker = {}
        l = []
        while second_pointer < len(s)+1:
            if s[second_pointer] not in tracker:
                tracker[s[second_pointer]] = second_pointer
                second_pointer += 1
                max_counter += 1
            else:
                s.pop(first_pointer)
                first_pointer += 1
                l.append(max_counter)
                max_counter = 0
                second_pointer += 1
        return (l)

print(lengthOfLongestSubstring('pwwkew'))