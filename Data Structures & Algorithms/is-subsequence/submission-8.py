class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False
        p1 = 0
        for p2 in range(len(t)):
            if s[p1] == t[p2]:
                p1 += 1
            if p1 == len(s):
                return True
        return False       