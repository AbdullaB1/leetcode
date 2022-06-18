class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # jewels_set = set(jewels)
        # return sum(s in jewels_set for s in stones)

        jewels_count = 0
        jewels_set = set(jewels)
        for s in stones:
            if s in jewels_set:
                jewels_count += 1
        return jewels_count
