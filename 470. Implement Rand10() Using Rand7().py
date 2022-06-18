# The rand7() API is already defined for you.
def rand7():
    # @return a random integer in the range 1 to 7
    pass


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()
        print(a, b)
        res = a + (b - 1) * 7
        while res > 40:
            a = rand7()
            b = rand7()
            print(a, b)
            res = a + (b - 1) * 7
        return res % 10 + 1
