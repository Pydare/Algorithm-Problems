# https://leetcode.com/discuss/interview-question/428240/Audible-Onlie-Assessment-for-New-Graduate-Number-of-characters-escaped

def escape(instr):
	escape_time = 0
	nows = 0
	thises = 0
	for i in range(len(instr)):
		if instr[i] == "#":
			nows = not nows
			if nows == 0:
				escape_time += thises
				thises = 0
		else:
			if nows == 1:
				if instr[i-1] ==" !" and ord(instr[i]) >= ord("a") and ord(instr[i]) <= ord("z"):
					thises += 1
	return escape_time

print(escape("##!r#po#"))
print(escape("#ab!c#de!f"))
print(escape("a!de#dwx!re!e##!##sdc!a!f"))


def find_char(char_string):
    if not char_string or len(char_string) < 4:
        return 0
    ans = 0
    temp_counter = 0
    pound_flag = False

    for i, ch in enumerate(char_string):
        if ch == '#':
            pound_flag = not(pound_flag)
            # If closing pound is found and you have a live counter add it to ans
            # Also reset temp_counter
            if not pound_flag and temp_counter > 0:
                ans += temp_counter
                temp_counter = 0
            continue

        if pound_flag:
            # Only interested in characters when pound flag is up
            if ch.isalpha() and ch.islower() and i != len(char_string) - 1 and char_string[i - 1] == '!':
                temp_counter += 1

    return ans