# Hash Map

class Solution(object):
    def twoSum(self, nums, target):

        hash = {}

        for i, a in enumerate(nums):
            diff = target - a
            if diff in hash:
                return (hash[diff], i)
            hash[a] = i
