# Hash set

class Solution(object):
    def twoSum(self, numbers, target):
        hash = {}

        for i, e in enumerate(numbers):
            diff = target-e
            if diff in hash:
                return (hash[diff]+1, i+1)
            hash[e] = i
