class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        all_chars = [
            'abc', 'def', 'ghi', 'jkl',  'mno', 'pqrs', 'tuv', 'wxyz',
        ]
        self.loop_chars = []
        for d in digits:
            self.loop_chars.append(all_chars[int(d) - 2])
        self.results = []
        self.travers(0, [])
        return self.results
            
        
    def travers(self, idx: int, curr_res: list[str]) -> None:
        if idx >= len(self.loop_chars):
            self.results.append(''.join(curr_res))
            return
        
        # print(self.results, idx)
        for c in self.loop_chars[idx]:
            # можно просто вызвать self.travers(idx + 1, curr_res + [c])
            # но такой способ не оптимален с точки зрения того, что конструироуется новый list после + [c]
            curr_res.append(c)
            self.travers(idx + 1, curr_res)
            curr_res.pop()
