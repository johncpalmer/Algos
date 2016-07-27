# given a string, see if its letter can be made into a palindrome (ignore any spaces)
#input: string
# output: Boolean
import collections


# nlogn time, constant space
def palPerm(s):
	myChars = sorted(s)
	currChar = ""
	currCount = 0
	hasHitOdd = False
	for i in xrange(len(myChars)):
		if i != " ":
			if myChars[i] == currChar:
				currCount = currCount + 1
			else:
				if currCount % 2 != 0:
					if hasHitOdd:
						return False
					else:
						hasHitOdd = True
						currChar = myChars[i]
				else:
					currCount = 1
					currChar = myChars[i]
	if currCount % 2 !=0 and hasHitOdd:
		return False
	else:
		return True

# n time, n space
def palPerm2(s):
	hasOneOdd = False
	charCounts = collections.Counter()
	for i in xrange(len(s)):
		if s[i] != " ":
			charCounts[s[i]] +=1

	for key in charCounts.keys():
		if charCounts[key] % 2 != 0:
			if hasOneOdd:
				return False
			else:
				hasOneOdd = True
	return True

print(palPerm2("") == True)
print(palPerm2("a") == True)
print(palPerm2("aa") == True)
print(palPerm2("aab") == True)
print(palPerm2("ab") == False)
print(palPerm2("abc") == False)
