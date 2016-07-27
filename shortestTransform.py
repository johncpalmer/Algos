shortestHistory = []

def shortestTransform(startWord, targetWord, dict):
	global shortestHistory
	helper(startWord, targetWord, dict, [startWord])
	return shortestHistory


def helper(currWord, targetWord, dict, history):
	global shortestHistory

	if currWord == targetWord:
		if not shortestHistory or len(history) < len(shortestHistory):
			shortestHistory = history

	for i in xrange(len(currWord)):
		for x in dict:
			if x[:i] == currWord[:i] and x[i+1:] == currWord[i+1:]:
				if not (x in history):
					helper(x, targetWord, dict, history + [x])

mydict = {"aaa", "baa", "bba", "bbb"}
print shortestTransform("aaa","bbb",mydict)

shortestHistory = []

dict2 = {"aaa", "aga", "bga", "bfa", "bfb", "bbb"}
print shortestTransform("aaa","bbb",dict2)