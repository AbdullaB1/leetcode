class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
        # return not diffs or (len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]])

        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
            if len(diffs) > 2:
                return False
        if not diffs:
            return True
        if len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]:
            return True
        return False
