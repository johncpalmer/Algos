# A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the least significant bit,
# and the bit at index 63 corresponding to the most significant bit. Implement code that takes as input a 64-bit integer x
# and swaps the bits at indices i and j.


def bitSwap(x,i,j):
	jBit = x[j]
	x[j] = x[i]
	x[i] = jBit
	return x



test1 = []
test2 = []
test3 = []

# create some test integers
for i in range(0,64):
	if i % 2 == 0:
		test1.append(0)
	else:
		test1.append(1)
	if i < 20:
		test3.append(0)
	else:
		test3.append(1)
	test2.append(0)



test1swapped = test1
test1swapped[0] = 1
test1swapped[63] = 0

test3swapped = test3
test3swapped[5] = 1
test3swapped[40] = 0


print(len(test1))
print(bitSwap(test1,0,63) == test1swapped)
print(bitSwap(test2,5,6) == test2)
print(bitSwap(test3,5,40) == test3swapped)
