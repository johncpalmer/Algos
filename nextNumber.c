#include <stdlib.h>
#include <stdio.h>

// prints the next largest number whose binary representation contains the same number of 1's
int nextNumber(int n) {
	// find next biggest numbber
	int have_passed_1 = 0;
	int a = n;
	int i, j;
	for(i = 0; i<16; i++) {
		if(n & (1 << i)) {
			have_passed_1 = 1;
		} else {
			if(have_passed_1) {
				break;
			}
		}
	}
	// i is 4
	for(j = 0; j<=i; j++) {
		if(n & (1 << (i-j))) {
			break;
		}
	}

	return (n | 1 << i) ^ (1 << (i-j));

}

int main() {
	printf("%d\n", nextNumber(8));
	printf("%d\n", nextNumber(16));
	printf("%d\n", nextNumber(3));

}