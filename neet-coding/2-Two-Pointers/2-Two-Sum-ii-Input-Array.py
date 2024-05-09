# Hash set

class Solution(object):
    def twoSum(self, numbers, target):
        hash = {}

        for i, e in enumerate(numbers):
            diff = target-e
            if diff in hash:
                return (hash[diff]+1, i+1)
            hash[e] = i


class Solution(object):
    def twoSum(self, numbers, target):

        l = 0
        r = len(numbers) -1
        ans = 0
        while l < r:
            ans = numbers[r]+ numbers[l]
            if ans == target:
                return [l+1, r+1]
            # IF THE ANS IS SMALLER THAN THE TARGET WE NEED TO INCREMENT L BY 1
            elif ans < target:
                # THE REASON WHY IS, IN A SORTED ARRAY THE LEFT MOST NUMBERS ARE SMALLER SO WE SHIFT IT UP TO INCREASE OUR SUM
                l +=1
                # OR ELSE IF ITS BIGGER THAN OUR TARGET WE SHIFT THE RIGHT ELEMENT DOWN BY 1, DECREASING THE VALUE OF THE OVERALL SUM
            else:
                r -=1
