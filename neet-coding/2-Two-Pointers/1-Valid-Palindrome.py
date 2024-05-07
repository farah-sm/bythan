# Two Pointers

class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        s = s.lower()

        while r > l:
            if s[r] == s[l]:
                l +=1
                r -=1
            elif not s[r].isalnum():
                r -=1
            elif not s[l].isalnum():
                l +=1
            else:
                return False
        return True
