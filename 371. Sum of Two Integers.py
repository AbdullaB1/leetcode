class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers
            print("sum of two positive integers")
            print(f'x = {x:08b}')
            print(f'y = {y:08b}')
            while y:
                x, y = x ^ y, (x & y) << 1
                print(f'x = {x:08b}')
                print(f'y = {y:08b}')
        else:
            # difference of two positive integers
            print("difference of two positive integers")
            print(f'x = {x:08b}')
            print(f'y = {y:08b}')
            while y:
                x, y = x ^ y, ((~x) & y) << 1
                print(f'x = {x:08b}')
                print(f'y = {y:08b}')

        return x * sign


s = Solution()
print(
    s.getSum(
        2, 15
    )
)
