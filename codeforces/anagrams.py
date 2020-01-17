def groupAnagrams(strs):
   sorted_strs = map(lambda e: ''.join(sorted(e)), strs)
   zipped = zip(sorted_strs,strs) 
   from collections import defaultdict
   anagram_dict = defaultdict(list)
   for sorted_strs, orig_str in zipped:
       anagram_dict[sorted_strs].append(orig_str)
    return list(anagram_dict.values())