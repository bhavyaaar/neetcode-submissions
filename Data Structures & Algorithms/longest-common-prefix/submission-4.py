class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #we use the first word as the base and compare every word at the matching index until we either run out of  characters or there is a mismatch and append by strs[0][i]
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i ==len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res




        