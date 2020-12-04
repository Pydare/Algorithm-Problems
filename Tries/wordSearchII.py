def find_words(board,words):
    WORD_KEY = '$'

    trie = {}
    for word in words:
        node = trie
        for letter in word:
            #retrieve next node; if not found, create an empty node
            node = node.setdefault(letter,{})
        #mark the existence of a word in trie node
        node[WORD_KEY] = word 
        print(trie)

    row_num, col_num = len(board), len(board[0])
    matched_words = []

    def backtracking(row,col,parent):
        letter = board[row][col]
        curr_node = parent[letter]

        #check if we find a match of word
        word_match = curr_node.pop(WORD_KEY,False)
        if word_match:
            #also we removed the matched word to avoid duplicates,
            #as well as avoiding using set() for results.
            matched_words.append(word_match)

        #before exploration, mark the cell as visited
        board[row][col] = '#'

        #explore the neighbors in 4 directions
        for row_offset, col_offset in [(-1,0),(0,1),(1,0),(0,-1)]:
            new_row, new_col = row+row_offset, col+col_offset
            if new_row < 0 or new_row >= row_num or new_col < 0  or new_col >= col_num:
                continue
            if not board[new_row][new_col] in curr_node:
                continue
            backtracking(new_row,new_col,curr_node)

        #end of exploration, we restore the cell
        board[row][col] = letter

        #optimization: incrementally remove the matched leaf node in trie
        if not curr_node:
            parent.pop(letter)

    for row in range(row_num):
        for col in range(col_num):
            #starting from each of the cells
            if board[row][col] in trie:
                backtracking(row,col,trie)

    return matched_words

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
res = find_words(board, words)
print(res)