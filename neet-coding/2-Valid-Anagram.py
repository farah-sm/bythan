# String Manipulation

class Solution(object):
    def isAnagram(self, s, t):
        s_w = ''.join(sorted(s))
        t_w = ''.join(sorted(t))

        if t_w == s_w: return True

