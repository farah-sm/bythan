class Solution(object):
    def findWordsContaining(self, words, x):

        word = ""
        w = []

        for i, e in enumerate(words):
            if x in e: #<---
                w.append(i)
        return w
