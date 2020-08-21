"""
anchor -> the start position
input: ["a","a","b","b","c","c","c"]

read = 2   anchor = 0   write = 1
chars = ["a", ""]

output: ["a","2","b","2","c","3"] length=6
"""

def compress(chars):
    anchor = write = 0

    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read+1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    print(digit)
                    chars[write] = digit
                    write += 1
            anchor = read + 1

    return write

ans = compress(["a","a","b","b","c","c","c"])
print(ans)

