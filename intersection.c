#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct Node {
	int val;
	struct Node *next;
}

struct Node *do_intersect(struct Node *list_a, struct Node *list_b) {
	int count_a = 1;
	int count_b = 1;
	struct Node *curr_a_node = list_a;
	struct Node *curr_b_node = list_b;

	while(curr_a_node->next) {
		count_a++;
		curr_a_node = curr_a_node->next;
	}

	while(curr_b_node->next) {
		count_b++;
		curr_b_node = curr_b_node->next;
	}

	if(curr_a_node == curr_b_node) {
		int diff;
		curr_a_node = list_a;
		curr_b_node = list_b;
		// we are intersecting, use lenghts to find intersecting node
		if(count_a > count_b) {
			diff = count_a - count_b;
			for(int i =0; i<diff; i++) {
				curr_a_node = curr_a_node->next;
			}
		} else {
			diff = count_b - count_a;
			for(int i =0; i<diff; i++) {
				curr_b_node = curr_b_node->next;
			}
		}

		while(curr_a_node != curr_b_node) {
			curr_a_node = curr_a_node->next;
			curr_b_node = curr_a_node->next;
		}

		return curr_a_node;
	} else {
		return 0;
	}
}

int main() {
	
}