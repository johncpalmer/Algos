import collections
# return true if word contains all unique characters
def isUnique(word):
	# brute force is that for each character, check if it's in the rest of the string (n^2)

	# optimal
	letters = collections.Counter()

	for i in xrange(len(word)):
		letters[word[i]] += 1

	for i in xrange(len(word)):
		if letters[word[i]] > 1:
			return False

	return True

# tests

print(isUnique("a"))
print(isUnique("ab"))
print(isUnique("abc"))
print(isUnique("aa"))
print(isUnique("abcdea"))
print(isUnique(""))
