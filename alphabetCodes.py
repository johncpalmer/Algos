def charInt(letter):
	return ord(letter) - 96

def toLetter(num):
	return chr(num+96)

# prints the list, returns the len of the list
def alphabetStrings(code):
	answer = helper("", code)
	print(answer)
	return len(answer)


# return all the possible strings that can be made out of the rest of the string,
# each prepended by prefix
def helper(prefix, remainingNums):
	bigList = []

	if len(remainingNums) == 1:
		return [prefix+toLetter(int(remainingNums))]
	elif len(remainingNums) == 0:
		return [prefix]
	else:
		# add first letter to prefix
		prefix1 = prefix + toLetter(int(remainingNums[0]))

		if 0 < int(remainingNums[0:2]) < 27:
			prefix2 = prefix + toLetter(int(remainingNums[0:2]))
			return helper(prefix1, remainingNums[1:]) + helper(prefix2, remainingNums[2:])
		else:
			return helper(prefix1, remainingNums[1:])

alphabetStrings("1123")


