class Solution:
    # this solution was my best attempt. It worked on 111 out of 119 test 
cases.
    # helper function
    def isAnagram(self, s, t):
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
        if len(dic_t) != len(dic_s):
            return False
        for ele in dic_s:
            if ele not in dic_t or dic_t[ele] != dic_s[ele]:
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = Solution()
        ret = [ [strs[0]] ]
        for s in strs[1:]:
            wasAppended = False
            for i in range(len(ret)):
                if sol.isAnagram(s, ret[i][0]):
                    ret[i].append(s)
                    wasAppended = True
                    continue
            if wasAppended:
                continue
            else:
                ret.append([s])
        return ret
