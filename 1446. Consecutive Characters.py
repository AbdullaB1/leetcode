class Solution:
    def maxPower(self, s: str) -> int:
        power = curr = 0
        prev = None
        for c in s:
            if c != prev:
                power = max(power, curr)
                curr = 1
            else:
                curr += 1
            prev = c
        power = max(power, curr)
        return power
