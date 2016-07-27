import math

# counts the number of 1's in the binary representation of a number
def countOnes(num):
	count = 0
	mask = 1
	numToCheck = int(math.log(num, 2)) + 1
	# print(numToCheck)
	for i in xrange(numToCheck):
		if mask & num:
			count += 1
		mask = mask << 1
	return count


print(countOnes(1))
print(countOnes(2))
print(countOnes(3))
print(countOnes(16))

