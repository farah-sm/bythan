# Counter Function

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)

        return (key for key, _ in count.most_common(k))
