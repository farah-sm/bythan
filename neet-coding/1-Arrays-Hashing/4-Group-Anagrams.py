# Hash Map (Default Dict)


class Solution(object):
    def groupAnagrams(self, strs):
        hash = defaultdict(list)

        for a in strs:
            w = ''.join(sorted(a))
            hash[w].append(a)
        return hash.values()
