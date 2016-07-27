def robotPaths(m,n):
	counts = [[0]*(m) for i in range (n)]
	for i in xrange(m):
		counts[0][i] = 1
		counts[i][0] = 1
	print counts

	for i in xrange(1,m):
		for j in xrange(1,n):
			counts[i][j] = counts[i-1][j] + counts[i][j-1]
	return counts[m-1][n-1]

print robotPaths(5,5)