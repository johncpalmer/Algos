def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ans = []
    dic1 = {}
    dic2 = {}
    x = 0
    y = 0

    while x < len(nums1):
    	curr = nums1[x]
    	if not(curr in dic1):
    		dic1[curr] = 1
    	x = x+1

    while y < len(nums2):
    	curr = nums2[y]
    	if not(curr in dic2):
    		dic2[curr] = 1
    	y = y+1

    for z in dic1.keys():
    	if z in dic2:
    		ans.append(z)
    return ans


print(intersection([],[]) == [])
print(intersection([1],[1]) == [1])
print(intersection([1,1,1],[1,1,1]) == [1])
print(intersection([1,2,3,4],[3,4,5,6]) == [3,4])