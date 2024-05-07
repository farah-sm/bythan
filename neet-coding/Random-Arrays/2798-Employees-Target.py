class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0

        for i, e in enumerate(hours):
            if e >= target:
                count +=1
        return count
