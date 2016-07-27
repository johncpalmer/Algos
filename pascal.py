def generate(input):
    result = []
    for x in range(input):
    	if x == 0:
    		result.append([1])
    	elif x == 1:
    		result.append([1,1])
    	else:
	        result.append([1]*(x+1))
	        for j in range(1,x):
	            result[x][j] = result[x-1][j-1] + result[x-1][j]
    return result
	# ^ if this is print(result), it works. but reuturn is fucking it up. idk why.

print(generate(0))
print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(5))
print(generate(6))



# ANALYSIS

# Time: O(n^2), where n is the input to the function (the number of rows to be printed)
#    Each ith row that needs to be printed requires roughly i constant time calculations to create,
#    along with another i constant operations to be printed.
#    In order to print n rows, that means there will be a total of (n*(n+1))/2 total operations.
#    This puts this algorithm in O(n^2) time


# Space: O(n^2)
#    For each constant operation involved in the creation of the triangle (mentioned in time analysis),
#    we use 1 space.