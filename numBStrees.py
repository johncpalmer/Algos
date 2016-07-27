import math

# for a number of values N, count the number of ways you could make a binary search tree with n values
def numBStrees(n):
	# if n is 0, return 0
	# if n is 1, return 1
	# otherise
		# the count is n * SUM ( (n-1,m)*(f(m) + f(n-1-m))
	totalCount = 0
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		for i in xrange(0,n):
			totalCount += numBStrees(n-1-i) * numBStrees(i)
		return totalCount

def choose(a,b):
	if a == 0 or b == 0:
		return 0
	return math.factorial(a) / math.factorial(b) / math.factorial(a-b)

print choose(2,1)
print choose(3,1)
print choose(3,3)
print choose(3,2)

print(numBStrees(1))
print(numBStrees(2))
print(numBStrees(3))
print(numBStrees(4))
print(numBStrees(5))
print(numBStrees(6))
print(numBStrees(7))
print(numBStrees(8))