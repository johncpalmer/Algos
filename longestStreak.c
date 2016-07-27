// Problem 5.3 from Cracking the Coding Interview
// You have an integer and you can flip exactly one bit from a 0 to a 1. 
// Write code to find the length of the longest sequence of 1s you could create.

// EXAMPLE
// Input: 1775 or 11011101111
// Output: 8

// just have a bitmask at the least significant bit.
// keep track of maximum streak while right shifting the number and masking with the least significant bit
// kill the streak when you've hit 2 0's in a row
// number is at most 32 bits long
#include <stdio.h>

// given a number, count count how many 1's are in its binary represention before reaching a 0
// starting with the least significant bit
int countOnes(int num) {
	int mask = 1;
	int count = 0;
	while(num & mask) {
		count++;
		num = num >> 1;
	}
	return count;
}

// return the max of 2 integers
int max(int a, int b) {
	if (a > b) {
		return a;
	} else {
		return b;
	}
}

// get the longest streak of 1's that could be created in the binary representation of a number,
// given that you are allowed to flip any single 0 to a 1
int getStreak(int num) {
	int longestStreak = 0;
	int currStreak = 0;
	int myMask = 1;
	int hitZero = 0;
	int started = 0;

	for(int i = 0; i < 33; i++) {
		// if we still have a 1, just increment the current streak
		if(num & myMask) {
			started = 1;
			currStreak++;	
			if (currStreak > longestStreak) {
				longestStreak = currStreak;
			}		
		} else {
			if(started) {
				// we hit a 0. so our max is either created by flipping this 0, or by going elsewhere in the string.
				return max(longestStreak + countOnes(num >> 1) + 1, getStreak(num >> 1));
			}
		}

		num = num >> 1;
	}

	return longestStreak;
}



int main() {
	printf("%d\n", countOnes(7));
	printf("%d\n", countOnes(2));
	printf("%d\n", countOnes(15));
	printf("%d\n", getStreak(1775));
	printf("%d\n", getStreak(70));
}
