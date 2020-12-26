"""We can use counting sort since scores are in the range [0, 100].

Python Solution
Time complexity: O(n)
Space Complexity: O(1)

Eg: cutOffRank = 4

num=5

scores=[2,2,3,4,5]
"""
def count_num_players_to_level_up(cut_off_rank, scores):
    if cut_off_rank <= 0:
        return 0

    frequencies = [0 for i in range(100 + 1)]
    for score in scores:
        frequencies[score] += 1

    ans = 0
    current_rank = 1
    for i in range(100, -1, -1):
        if frequencies[i] == 0:
            continue
        ans += frequencies[i]
        current_rank += frequencies[i]
        if current_rank > cut_off_rank:
            break
    return ans