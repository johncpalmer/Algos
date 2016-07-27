def countPathsCaching(m,n):
    cache = [[0]*m for x in xrange(n)]
    def countPathsHelper(m,n):
        for i in xrange(m):
            cache[0][i] = 1
            cache[i][0] = 1

        for i in xrange(1,m):
            for j in xrange(1,n):
                cache[i][j] = cache[i-1][j] + cache[i][j-1]

        return cache[m-1][n-1]

    return countPathsHelper(m, n)

print countPathsCaching(5,5)

def countPathsRecursive(m, n):
    def countPathsHelper(currRow, currCol, m, n):
        if currRow == m-1 and currCol == n-1:
            return 1
        if currRow != m-1 and currCol != n-1:
            return countPathsHelper(currRow+1, currCol, m, n) + countPathsHelper(currRow, currCol+1, m, n)
        if currRow == m-1:
            return countPathsHelper(currRow, currCol+1, m, n)
        else:
            return countPathsHelper(currRow+1, currCol, m, n)

    return countPathsHelper(0, 0, m, n)

print countPathsRecursive(5,5)
