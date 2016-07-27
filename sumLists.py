class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def myPrint(self):
		curr = self
		while curr:
			print("%s -> " %(curr.data))
			curr = curr.next

	def insert(self, data):
		myNode = Node(data)
		myNode.next = self
		return myNode
		

# 2 linked listed in reverse order representing decimal numbers
def sumLists(list1,list2):
	newHead = None
	newTail = None
	carry = 0

	while(list1 or list2):
		sum = 0
		if list1 and list2:
			sum = list1.data + list2.data + carry
			list1 = list1.next
			list2=list2.next
		elif list1:
			sum = list1.data + carry
			list1 = list1.next
		else:
			sum = list2.data + carry
			list2=list2.next

		myNode = Node(sum)
		if sum > 9:
			myNode.data = sum-10
			carry = 1
		else:
			carry = 0
		
		if newTail:
			newTail.next = myNode
			newTail = myNode
		else:
			newHead = myNode
			newTail = myNode

	return newHead
	


twentyNine = Node(2)
twentyNine = twentyNine.insert(9)

fortyEight = Node(4)
fortyEight = fortyEight.insert(8)

twentyNine.myPrint()
fortyEight.myPrint()

# works
sumLists(twentyNine, fortyEight).myPrint()

twoNinety = twentyNine.insert(0)

# works when different lengths
sumLists(twoNinety, fortyEight).myPrint()
