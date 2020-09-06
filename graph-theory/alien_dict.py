from collections import defaultdict, Counter, deque

class Solution(object):
  def alienOrder(self, words):
      """
      :type words: List[str]
      :rtype: str
      """
      #step 0, create data structures + the indegree of each unique letter to be 0
      adj_list = defaultdict(set)
      indegree = Counter({c:0 for word in words for c in word})
      
      #step 1 populate the adj_list and indegree
      #for each pair of adjacent words
      for first_word, second_word in zip(words, words[1:]):
          for c, d in zip(first_word, second_word):
              if c != d:
                  if d not in adj_list[c]:
                      adj_list[c].add(d)
                      indegree[d] += 1
                  break
          else: #check that second word isn't a prefix of first word
              if len(second_word) < len(first_word): return ""
              
      #step 2: need to repeatedly pick off nodes with an indegree of 0
      output = []
      q = deque([c for c in indegree if indegree[c] == 0])
      while q:
          c = q.popleft()
          output.append(c)
          for d in adj_list[c]:
              indegree[d] -= 1
              if indegree[d] == 0:
                  q.append(d)
                  
      #if not all letters are in output, that means there was a cycle and so no valid ordering
      return "".join(output) if len(output) == len(indegree) else ""