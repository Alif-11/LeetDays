class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = dict()
        dic_t = dict()
        for c in s:
            if c in dic_s:
                dic_s[c] = dic_s[c] + 1
            else:
                dic_s[c] = 0
        for c in t:
            if c in dic_t:
                dic_t[c] = dic_t[c] + 1
            else:
                dic_t[c] = 0
        if len(dic_s) != len(dic_t):
            return False
        for e in dic_s:
            if e not in dic_t or dic_s[e] != dic_t[e]:
                return False
        return True

