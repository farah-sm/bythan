# Hash set

class Solution(object):
    def longestConsecutive(self, nums):

        hash = set(nums)
        longest = 0
        length = 0

        for i in nums:
            if i-1 not in hash:
                while i+length in hash:
                    length +=1
                longest = max(length, longest)
        return longest
                
                
        
