def intersect(nums1, nums2):
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
        if nums1[x] in dic1:
            dic1[nums1[x]] = dic1[nums1[x]] + 1
        else:
             dic1[nums1[x]] = 1
        x = x+1
    
    while y < len(nums2):
        if nums2[y] in dic2:
            dic2[nums2[y]] = dic2[nums2[y]] + 1
        else:
             dic2[nums2[y]] = 1
        y = y+1
             
    for z in dic1.keys():
        if z in dic1 and z in dic2:
            currCount = min(dic1[z], dic2[z])
            for i in range(currCount):
                ans.append(z)
        
    return ans
        
    
print(intersect([1],[1]) == [1])
print(intersect([],[]) == [])
print(intersect([1,1],[1,1]) == [1,1])
print(intersect([1,2,2,1], [2,2]) == [2,2])