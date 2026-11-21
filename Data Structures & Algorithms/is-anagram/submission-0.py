class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            c=sorted(s)
            d=sorted(t)
            return c==d
        else:
            return False