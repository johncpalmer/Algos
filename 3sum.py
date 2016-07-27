import collections

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        myVals = collections.Counter()
        answer = []
        for x in nums:
            myVals[x] += 1
        
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                currSum = nums[i] + nums[j]
                requiredCount = 1
                if -currSum == nums[i]:
                    requiredCount += 1
                if -currSum == nums[j]:
                    requiredCount += 1
                
                if myVals[-currSum] >= requiredCount:
                    triplet = sorted([nums[i], nums[j], -currSum])
                    if not(triplet in answer):
                        answer.append(triplet)
        return answer