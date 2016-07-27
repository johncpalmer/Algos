# return a list of all unique k-tuples in 1...n inclusive
def kTuples(k, n):
	bigList = []
	myHelper(1, n, k, [], bigList, 0)
	return bigList


def myHelper(minVal, maxVal, k, currList, bigList, length):
	if length == k: # constant
		bigList.append(currList) #linear time to copy a slice
	elif (maxVal+1) - minVal < (length - k):
		return
	else:
		for i in xrange(minVal, maxVal+1):
			myHelper(i+1, maxVal, k, currList + [i], bigList, length+1)

print(kTuples(2,4))
