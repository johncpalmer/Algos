# rotates a square matrix clockwise
def rotate(matrix):
	length = len(matrix)

	numLayers = length / 2

	for offset in xrange(numLayers):
		temp = matrix[offset][offset]

		# rotate each entry in left column upward
		for j in xrange(0,length-1-(2*offset)):
			matrix[offset+j][offset] = matrix[offset+j+1][offset]

		#rotate each entry on bottom row leftward
		for j in xrange(0, length-1-(2*offset)):
			matrix[length-1-offset][offset+j] = matrix[length-1-offset][offset+j+1]

		# rotate each entry on the right column dowmwards
		for j in xrange(0, length-1-(2*offset)):
			matrix[length-1-offset-j][length-1-offset] = matrix[length-1-offset-j-1][length-1-offset]

		# rotate each entry on top row to the right (so set each thing to be the thing to the left of it)
		for j in xrange(0, length-1-(2*offset)):
			matrix[offset][length-1-offset-j] = matrix [offset][length-1-offset-j-1]

		matrix[offset][offset+1] = temp

# matrix = [[1,2],[4,3]]
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)

# matrix = [[1,2,3],[8,9,4],[7,6,5]]
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)

# matrix = [[1,2,3,4],[12,1,2,5],[11,4,3,6],[10,9,8,7]]
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)
# rotate(matrix)
# print(matrix)





